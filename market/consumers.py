from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer,JsonWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from urllib.parse import parse_qs
# from .models import StockDetail, UserSessionIds
from PythonSDK.websocket import _http
from PythonSDK.MOFSLOPENAPI import *
from .views import *
# from .donkey import donkeymanish
# from PythonSDK.SampleMOFSLOPENAPI import *
import json
import copy

class StockConsumer(AsyncWebsocketConsumer):

    @sync_to_async
    def addToCeleryBeat(self, stock_list):
        task = PeriodicTask.objects.filter(name = 'every-10-seconds')
        if len(task)>0:
            task = task.first()
            args = json.loads(task.args)
            args = args[0]
            for x in stock_list:
                if x not in args:
                    args.append(x)
            task.args = json.dumps([args])
            task.save()
        else:
            schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
            task = PeriodicTask.objects.create(interval=schedule, name='every-10-seconds', task='stocks.tasks.update_stocks', args=json.dumps([stock_list]))

    @sync_to_async    
    def addToStockDetail(self, stock_list):
        session_id = self.scope['session'].session_key
        user, _ = UserSessionIds.objects.get_or_create(session_id = session_id)
        for i in stock_list:
            stock, created = StockDetail.objects.get_or_create(stock = i)
            stock.user.add(user)

    async def connect(self):
        await self.channel_layer.group_add('stockwatchers', self.channel_name)
        query_params = parse_qs(self.scope["query_string"].decode())
        stock_list = query_params['stock_list']
        await self.addToCeleryBeat(stock_list)
        await self.addToStockDetail(stock_list)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        await self.channel_layer.group_send(
            'stockwatchers', {"type": "send_stock_update", "message": message}
        )

    @sync_to_async
    def selectUserStocks(self):
        session_id = self.scope['session'].session_key
        session_id = UserSessionIds.objects.get(session_id = session_id)
        user_stocks = session_id.stockdetail_set.values_list('stock', flat = True)
        return list(user_stocks)
    
    async def send_stock_update(self, event):
        message = event["message"]
        message = copy.copy(message)
        user_stocks = await self.selectUserStocks()
        keys = message.keys()
        for key in list(keys):
            if key in user_stocks:
                pass
            else:
                del message[key]

        await self.send(text_data=json.dumps(message))
    
    @sync_to_async
    def helper_func(self):
        session_id = self.scope['session'].session_key
        session_id = UserSessionIds.objects.get(session_id = session_id)
        stocks = StockDetail.objects.filter(user__id = session_id.id)
        task = PeriodicTask.objects.get(name = "every-10-seconds")
        args = json.loads(task.args)
        args = args[0]
        for i in stocks:
            i.user.remove(session_id)
            if i.user.count() == 0:
                args.remove(i.stock)
                i.delete()
        session_id.delete()
        if args == None:
            args = []
        if len(args) == 0:
            task.delete()
        else:
            task.args = json.dumps([args])
            task.save()

    async def disconnect(self, close_code):
        await self.helper_func()
        await self.channel_layer.group_discard('stockwatchers', self.channel_name)

class ChartConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("websocket connected")
        global apikey
        global clientid
        global authtoken
        datafromview = donkeymanish(self)
        print(datafromview)
        apikey = datafromview['apikey']
        clientid = datafromview['clientid']
        authtoken = datafromview['authtoken']
        await self.start_background_task(self.websocket_handler)
        # if not await self.coo():
        #     print("manish")
        #     # dg = self.send({"msg":"this is websocket connection"})
        #     # print("abhi")
        #     # print(dg)
        #     sf = await self.close()
        #     print(sf)
        # else:
        #     # Assuming _http is an instance of some class with a connect method
        #     print("logged in connection web")
            
            # sf = self.connect()
            # print(sf)
     
            # websocket_conn = _http.connect()
            # print("websock connct 1")
            # print(websocket_conn)  
            # if websocket_conn:
            #     reg = MOFSLOPENAPI.IndexRegister("NSE")
            #     print("Success")
            #     reg.accept()
            # else:
            #     print("Connection failed")
        
            
        # return {'Mofsl':loginmofsl,'clientcode':clientcode}
        ttt = True
        # if ttt:

        #     url = "wss://openapi.motilaloswal.com/"
                
        #     headers = {
        #         "Accept": "application/json",
        #         "User-Agent": "MOSL/V.1.1.0",
        #         "Authorization": loginmofsl["AuthToken"],
        #         "ApiKey": "MHohVro9A0A1Q2Sw",
        #         "ClientLocalIp": "1.2.3.4",
        #         "ClientPublicIp": "1.2.3.4",
        #         "MacAddress": "00:00:00:00:00:00",
        #         "SourceId": "WEB",
        #         "vendorinfo": "T0240",
        #         "osname": "Windows 10",
        #         "osversion": "10.0.19041",
        #         "devicemodel": "AHV",
        #         'manufacturer': 'LENOVO',
        #         "installedappid": "AppID",
        #         "browsername": "Chrome",
        #         "browserversion": "105.0"
        #     }
        #     # print(headers)
        #     data = {
        #         "clientcode": clientcode,  # In case of dealer else not required
        #         "authtoken": loginmofsl["AuthToken"],
        #         "apikey": ApiKey

        #     }
        #     print("websocket connection successfully")
        #     # NSE_BSE_data(request)
        #     response_nse = requests.post(url, json=data, headers=headers)
        #     print(response_nse)


    async def disconnect(self, close_code):
        print('disconnect', close_code)
    async def receive_json(self, content, **kwargs):
        data = {
            "msg":"my connection"
        }
        text_data_json = json.loads(data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
        
        print("websocket recieve",content)

    def is_valid_token(self, token):
        # Validate the token (implement this method according to your needs)
        ApiKey = "MHohVro9A0A1Q2Sw"
        userid = "EBOM907310"
        password = "@Massy512"
        Two_FA = "05/01/2000"
        vendorinfo = "EBOM907310"
        clientcode = "EBOM907310"
        SourceID = "Desktop"
        browsername = "chrome"
        browserversion = "104"

        # Base URL for MOFSL API
        Base_Url = "https://openapi.motilaloswal.com"
        # Initialize MOFSL API
        Mofsl = MOFSLOPENAPI(ApiKey, Base_Url, clientcode, SourceID, browsername, browserversion)

        # Login to MOFSL
        print("Logging in...")
        print("Logging in...")
        totp = input("Enter Input: ")
        loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)
        return {'Mofsl':loginmofsl,'clientcode':clientcode}
    
    async def websocket_handler(self):
        url = "wss://openapi.motilaloswal.com/"
        headers = {
                "Accept": "application/json",
                "User-Agent": "MOSL/V.1.1.0",
                "Authorization": loginmofsl["AuthToken"],
                "ApiKey": "MHohVro9A0A1Q2Sw",
                "ClientLocalIp": "1.2.3.4",
                "ClientPublicIp": "1.2.3.4",
                "MacAddress": "00:00:00:00:00:00",
                "SourceId": "WEB",
                "vendorinfo": "T0240",
                "osname": "Windows 10",
                "osversion": "10.0.19041",
                "devicemodel": "AHV",
                'manufacturer': 'LENOVO',
                "installedappid": "AppID",
                "browsername": "Chrome",
                "browserversion": "105.0"
            }

        data = {
                "clientcode": clientid,  # In case of dealer else not required
                "authtoken":authtoken ,
                "apikey": apikey

            }
        print(data)

        async with websockets.connect(url, daata=data) as websocket:
            await websocket.send(json.dumps(data))

            while True:
                response = await websocket.recv()
                print("WebSocket received:", response)

      