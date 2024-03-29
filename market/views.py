from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseServerError, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.models import User
# from .models import frenchise_register_model,frenchise_employee_register_model,ProfileFrenchise
from django.contrib.auth.decorators import login_required
from fastapi.responses import RedirectResponse, HTMLResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from companystaff.models import *
# from .filters import frenchise_filter
from datetime import datetime
import requests
import hashlib
import json
from bs4 import BeautifulSoup
from PythonSDK.MOFSLOPENAPI import *
from PythonSDK.websocket import *
from .routing import *
from .consumers import ChartConsumer
# Create your views here.
# import matplotlib.pyplot as plt
from io import BytesIO
import asyncio
import websockets

   

# Create your views here.
def scrape_website(request):
    # Replace 'url_to_scrape' with the actual URL you want to scrape
    url_to_scrape = 'https://getbootstrap.com/docs/5.0/utilities/text/'
    
    try:
        # Make a GET request to the website
        response = requests.get(url_to_scrape)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract data from the HTML using BeautifulSoup
            # (Replace this with the actual data extraction code)
            extracted_data = soup.find('div', class_='header').text
            print(extracted_data)

            # Pass the extracted data to the template
            return render(request, 'market/home.html', {'data': extracted_data})
        else:
            return render(request, 'market/home.html', {'error_message': f'Request failed with status code {response.status_code}'})
    except Exception as e:
        return render(request, 'market/home.html', {'error_message': f'An error occurred: {str(e)}'})


# MOSL - authentication
# def mosl_login(request):
#     # Set the password, apiKey, and authtoken
#     password = "abcd"
#     apiKey = "abc"
#     authtoken = "d3bcc86824264c689bf18052bb724fa5_M"

#     # Define the URL for the production environment
#     url = f"https://invest.motilaloswal.com/OpenAPI/Login.aspx?apikey={apikey}"

#     # Calculate the SHA-256 hash of the password and apiKey
#     combined_string = password + apiKey
#     hash_object = hashlib.sha256(combined_string.encode())
#     hashed_password = hash_object.hexdigest()

#     # Prepare the request data
#     request_data = {
#         "userid": "AA017",
#         "password": hashed_password,
#         "2FA": "18/10/1988",
#         "totp": "Authenticator 6 digit Code"
#     }
#     print(request_data)



def mosl_home(request):
    return render (request, 'market/home.html')

def mosl_login(request):
    # Set the password, apiKey, and authtoken
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
    totp = input("Enter Input: ")
    loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)

    if loginmofsl['status'] == 'SUCCESS':
        print("Login successful")

        # Place order using the `place_order` method
        order_details = {
            # Order parameters
        }

        order_response = Mofsl.place_order(order_details)
        print("Order placed:", order_response)
    else:
        print("Login failed:", loginmofsl['message'])
    return render(request, 'market/home.html')

def mosl_logout(request):

    url = "https://uatopenapi.motilaloswal.com/rest/login/v1/logout"

    request_data = {
    "userid":"AA017"
    }
    
    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    print(request_data)

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=request_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Logout Successfully."})

#MOSL - Order
def mosl_place_order(request):
    api_key = "MHohVro9A0A1Q2Sw"
    url = "	https://uatopenapi.motilaloswal.com/rest/trans/v1/placeorder"

    order_data_placed = {
        "clientcode": "AA017",
        "symboltoken": 1660,
        "buyorsell": "BUY",
        "ordertype": "LIMIT",
        "producttype": "Normal",
        "orderduration": "DAY",
        "price": 235.5,
        "triggerprice": 0,
        "quantityinlot": 2,
        "disclosedquantity": 0,
        "amoorder": "N",
        "algoid": "",
        "goodtilldate": "30-Jan-2022",
        "tag": "",
        "participantcode": "218450147IH"
    }
    
    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    print(order_data_placed)

    # Send a POST request with JSON data
    try:
        response = requests.get(url,api_key, params=order_data_placed, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "order placed successfully."})



# def mosl_place_odr(request):
#     # api_key = "MHohVro9A0A1Q2Sw"
#     # api_instance = MOFSLOPENAPI()
#     ApiKey = "MHohVro9A0A1Q2Sw"
#     userid = "EBOM907310"
#     password = "@Massy512"
#     Two_FA = "Enable"
#     vendorinfo = ""
#     clientcode = "EBOM907310"
#     SourceID = "Desktop"
#     browsername = "chrome"
#     browserversion = "104"
#     totp = input("Enter Input: ")
#     print(totp)
#     print(type(totp))

#     Base_Url = "https://openapi.motilaloswal.com"

#     Mofsl = MOFSLOPENAPI(ApiKey, Base_Url, clientcode, SourceID, browsername, browserversion)

#     print("Initialization successful")

#     loginmofsl = Mofsl.login(userid, password, Two_FA, totp)
#     print(loginmofsl)
#     print("Login successful")
#     print(loginmofsl)

#     LTPData = {
#         "clientcode": None,
#         "exchange": "BSE",
#         "scripcode": 500317
#     }
#     print("LTPData:")
#     print(LTPData)

#     getltpdata = Mofsl.GetLtp(LTPData)
#     print("GetLTP successful")
#     print(getltpdata)
# # 
#     # ltp_data = Mofsl.GetLtp(request,api_data)
#     # api_data = {"symbol": "NIFTY50", "interval": "2600"}
    
   

#     # mani = MOFSLOPENAPI.GetLtp(api_data)
#     print("4567898765678987656787678767")
#     # print(ltp_data)
#     # url = "https://uatopenapi.motilaloswal.com/rest/trans/v1/MHohVro9A0A1Q2Sw"

    


#     # Send a POST request with JSON data
    
    
#     return render(request, 'market/home.html')


    # API credentials
   

def mosl_modify_order(request):
    url = "	https://uatopenapi.motilaloswal.com/rest/trans/v2/modifyorder"
    modify_data = {
    "clientcode":"AA017", 
    "uniqueorderid ":"1101823KAL005",
    "newordertype":"LIMIT",
    "neworderduration":"DAY",
    " newquantityinlot ":100,
    "newdisclosedquantity":0,
    "newprice":235.50,
    "newtriggerprice":0,
    "newgoodtilldate":"",
    "lastmodifiedtime": "14-May-2022 11:31:25",
    "qtytradedtoday": 0
    }

    print(modify_data)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }


    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=modify_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Modify data successfully."})

def mosl_cancel_order(request):
    url = "https://uatopenapi.motilaloswal.com/rest/trans/v1/cancelorder"

    cancel_order_data = {
    "clientcode":"",
    "uniqueorderid":"1101823KAL005"
    }

    print(cancel_order_data)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=cancel_order_data, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Cancel Order successfully."})


def mosl_order_book(request):
    url = "https://uatopenapi.motilaloswal.com/rest/book/v2/getorderbook"

    order_book = {
    "clientcode":"AA017" 
    }

    print(order_book)

    headers = {
        "Accept": "application/json",  # Indicate that you expect a JSON response
        "Content-Type": "application/json",  # Specify the format of your request data
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=order_book, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your order Book."})



def mosl_trade_book(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/gettradebook"

    trade_book = {
    "clientcode":"AA017"
    }

    print(trade_book)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=trade_book, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your trade Book."})


def mosl_orderdetails(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v2/getorderdetailbyuniqueorderid"

    order_details = {
    "clientcode":"", 
    "uniqueorderid":"1000001AA020"
    }

    print(order_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=order_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your order details Book."})



def mosl_tradedetails(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/gettradedetailbyuniqueorderid"

    trade_details = {
    "clientcode":"AA017",
    "uniqueorderid":"2700002AA020"
    }
    print(trade_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=trade_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your trade details Book."})

#Portfolio
def mosl_holdings(request):
    url = "	https://openapi.motilaloswal.com/rest/report/v1/getdpholding"

    holdings = {
    "clientcode":"AA017"
    }
    print(holdings)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=holdings, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Holdings"})


def mosl_position(request):
    url = "	https://openapi.motilaloswal.com/rest/book/v1/getposition"

    position = {
    "clientcode":"AA017"
    }
    print(position)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position"})


def mosl_position_conversion(request):
    url = "https://openapi.motilaloswal.com/rest/trans/v1/positionconversion"

    position_conversion = {
    "clientcode":"KAL005", 
    "exchange":"NSE",
    "scripcode":1660,
    "quantity":100,
    "oldproduct":"Normal",
    "newproduct":"ValuePlus"
    }
    print(position_conversion)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position_conversion, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position Conversion"})


def mosl_position_details(request):

    url = "	https://openapi.motilaloswal.com/rest/book/v1/getpositiondetail"

    position_details = {
    "clientcode":"AA020" 
    }

    print(position_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=position_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Position Details"})

# MOSL - Limit/Margin - Price/LTP
def mosl_margin_summary(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getreportmarginsummary"

    margin_summary = {
    "clientcode":"AA020" 
    }

    print(margin_summary)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=margin_summary, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Margin Summary"})

def mosl_margin_details(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getreportmargindetail"

    margin_details = {
    "clientcode":"AA020" 
    }

    print(margin_details)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=margin_details, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Your Margin Details"})

def mosl_Price(request):


    url = "https://openapi.motilaloswal.com/rest/report/v1/getltpdata"

    price = {
    "clientcode":"AA020",
    "scripcode":500317

    }
    print(price)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=price, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Price"})


# MOSL - Master data & DPR Data
def mosl_scrips(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getscripsbyexchangename"

    scrips_FO = {
    "clientcode":"AA020", 
    "exchangename":"NSEFO"
    }
    print(scrips_FO)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=scrips_FO, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Scrips"})

def mosl_DPR(request):

    url = "	https://openapi.motilaloswal.com/rest/report/v1/getdprvalues"

    DPR = {
    "clientcode":"",
    "symbol":"BANKNIFTY"
    }
    print(DPR)

    headers = {
        "Accept": "application/json", 
        "Content-Type": "application/json", 
        # "UserAgent": "frenchise/1.0",
    }

    # Send a POST request with JSON data
    try:
        response = requests.get(url, params=DPR, headers=headers)

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "DPR"})


# MOSL - index
def mosl_index(request):
    # ApiKey = "MHohVro9A0A1Q2Sw"
    # userid = "EBOM907310"
    # password = "@Massy512"
    # Two_FA = "05/01/2000"
    # vendorinfo = "EBOM907310"
    # clientcode = "EBOM907310"
    # SourceID = "Desktop"
    # browsername = "chrome"
    # browserversion = "104"

    # # Base URL for MOFSL API
    # Base_Url = "https://openapi.motilaloswal.com"
    # # Initialize MOFSL API
    # Mofsl = MOFSLOPENAPI(ApiKey, Base_Url, clientcode, SourceID, browsername, browserversion)

    # # Login to MOFSL
    # print("Logging in...")
    # print("Logging in...")
    # totp = input("Enter Input: ")
    # loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)
    # print("mzdcxv")
    # print(loginmofsl)

    print(loginmofsl["AuthToken"])
    url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"

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
        "clientcode": clientcode,  # In case of dealer else not required
        "exchangename": "NSE"
    }
    print("calling NSE_BSE_data func")
    # NSE_BSE_data(request)
    response = requests.post(url, json=data, headers=headers)
    if loginmofsl['status'] == 'SUCCESS':
        print("Login successful")

    return render(request, 'market/home.html')

def nifty_chart(request):
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
    totp = input("Enter Input: ")
    loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)


    if loginmofsl['status'] == 'SUCCESS':
        print("Login successful")
    dataTosend = {

    }
    # getinstruct = Mofsl.GetInstrumentFile('BSE',clientcode)
    # print("getinstruct")
    # # print(getinstruct)
    # file_path = "examplehg.json"

    # # Writing data to the JSON file
    # with open(file_path, 'w') as json_file:
    #     json.dump(getinstruct, json_file)

    # print(f'Data has been written to {file_path}')
    LTPData = {
        "clientcode":clientcode,
        "exchange":"NSE",
        "scripcode":26000
    }
    getltpdata = Mofsl.GetLtp(LTPData)
    print("grt ltp data")
    print(getltpdata)
    # url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"

    # headers = {
    #     "Content-Type": "application/json",
    #     "Accept": "application/json",
    #     "User-Agent":"MOSL/V.1.1.0"
    # 
    

    # data = {
    #     "clientcode": clientcode,  # In case of dealer else not required
    #     "exchangename": "NSE"
    # }

    # response = requests.post(url, json=data, headers=headers)
    # print(response)
    # print(response.text)
    # print("json")
    # print(response.json())

    # if response.status_code == 200:
    #     print("Request successful")
    #     print("Response JSON:", response.json())
    # else:
    #     print(f"Request failed with status code {response.status_code}")
    #     print("Response text:", response.text)
        # LTPData = {
        # "clientcode":"EBOM907310",
        # "exchangename":"NSE",
        # "scripcode":"500317"
        # }
        # Get_ltp_data = Mofsl.GetProfile(LTPData)
        # print("LTP DATA", Get_ltp_data)
    # elsen failed:", loginmofsl['message'])
    # return render(request, 'market/home.html')


    return render(request, 'market/home.html')

def mofslloginfun(request):
    global ApiKey
    global userid
    global password
    global Two_FA
    global vendorinfo
    global clientcode
    global SourceID
    global browsername
    global browserversion
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
    global Mofsl
    global loginmofsl
    
    Mofsl = MOFSLOPENAPI(ApiKey, Base_Url, clientcode, SourceID, browsername, browserversion)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(" OTP:", otp)
        try:
            loginmofsl = Mofsl.login(userid, password, Two_FA, otp, vendorinfo)
            print("loginmofsl:", loginmofsl)
            if loginmofsl and loginmofsl.get('status') == 'SUCCESS':
                return redirect('MOSL_NSE_BSE_alldata')
            else:
                return render(request, 'market_dashboard/template/market_login.html')
        except Exception as e:
            print("An error occurred:", e)
            return HttpResponseServerError("An error occurred during OTP submission.")
    return render(request,'market_dashboard/template/market_login.html')
    # Login to MOFSL
    print("Logging in...")
    print("Logging in...")
    totp = input("Enter Input: ")
    loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)
    print("mzdcxv")
    print(loginmofsl)

def get_stock_data(symbol):
    # Make a request to Motilal Oswal API
    # Handle authentication and other necessary details
    response = requests.get(f'https://api.motilaloswal.com/stocks/{symbol}/')

    if response.status_code == 200:
        return response.json()
    else:
        return None


def NSE_BSE_data(request):
    print("in nse bse")
    global context


    template_detail_page = 'market_dashboard/template/market_dash.html'
    template_all_indices = 'market_dashboard/template/all_indices.html'

    url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"

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
        "clientcode": clientcode, 
        "exchangename": "NSE"
    }
    print("calling NSE_BSE_data func")

    try:
        response_nse = requests.post(url, json=data, headers=headers)
        print('response nse', response_nse)

        if response_nse.status_code == 200:
            try:
                json_data = response_nse.json()
                print("JSON response:", json_data)

              
                NIFTY_FIFTY = ""
                NIFTY_hundred = ""
                NIFTY_twohundred = ""
                NIFTY_bank = ""
                NIFTY_auto = ""
                NIFTY_fmcg = ""
                NIFTY_pharma = ""
                
                NIFTY_500 = ""
                NIFTY_COMMODITIES = ""
                NIFTY_CONSUMPTION = ""
                NIFTY_DIV_OPPS_50 = ""
                NIFTY_ENERGY = ""
                NIFTY_FIN_SERVICE = ""
                NIFTY_INFRA = ""
                NIFTY_IT = ""
                NIFTY_MEDIA = ""
                NIFTY_METAL = ""
                NIFTY_MIDCAP_100 = ""
                NIFTY_MNC = ""
                NIFTY_NEXT_50 = ""
                NIFTY_PSE = ""
                NIFTY_PSU_BANK = ""
                NIFTY_REALITY = ""
                NIFTY_SERV_SECTOR = ""
                NIFTY_SMALLCAP_100 = ""
                NIFTY_CPSE = ""
                INDIA_VIX = ""
                NIFTY100_LIQ_15 = ""
                NIFTY_GROWSECT_15 = ""
                NIFTY_MIDCAP_50 = ""
                NIFTY_MID_SELECT = ""
               

                responce_data = json_data.get('data', [])
                print("data dict", responce_data)

                for dt in responce_data:
                    if dt["indexname"] == "Nifty 50":
                        NIFTY_FIFTY = dt["indexcode"]
                    if dt["indexname"] == "Nifty 100":
                        NIFTY_hundred = dt["indexcode"]
                    if dt["indexname"] == "Nifty 200":
                        NIFTY_twohundred = dt["indexcode"]
                    if dt["indexname"] == "Nifty Bank":
                        NIFTY_bank = dt["indexcode"]
                    if dt["indexname"] == "Nifty Auto":
                        NIFTY_auto = dt["indexcode"]
                    if dt["indexname"] == "Nifty FMCG":
                        NIFTY_fmcg = dt["indexcode"]
                    if dt["indexname"] == "Nifty Pharma":
                        NIFTY_pharma = dt["indexcode"]
                    if dt["indexname"] == "Nifty 500":
                        NIFTY_500 = dt["indexcode"]
                    if dt["indexname"] == "Nifty Commodities":
                        NIFTY_COMMODITIES = dt["indexcode"]
                    if dt["indexname"] == "Nifty Consumption":
                        NIFTY_CONSUMPTION = dt["indexcode"]
                    if dt["indexname"] == "Nifty Div Opps 50":
                        NIFTY_DIV_OPPS_50 = dt["indexcode"]
                    if dt["indexname"] == "Nifty Energy":
                        NIFTY_ENERGY = dt["indexcode"]
                    if dt["indexname"] == "Nifty FIN SERVICE":
                        NIFTY_FIN_SERVICE = dt["indexcode"]
                    if dt["indexname"] == "Nifty Infra":
                        NIFTY_INFRA = dt["indexcode"]
                    if dt["indexname"] == "Nifty IT":
                        NIFTY_IT = dt["indexcode"]
                    if dt["indexname"] == "Nifty Media":
                        NIFTY_MEDIA = dt["indexcode"]
                    if dt["indexname"] == "Nifty Metal":
                        NIFTY_METAL = dt["indexcode"]
                    if dt["indexname"] == "Nifty MIDCAP 100":
                        NIFTY_MIDCAP_100 = dt["indexcode"]
                    if dt["indexname"] == "Nifty MNC":
                        NIFTY_MNC = dt["indexcode"]
                    if dt["indexname"] == "Nifty Next 50":
                        NIFTY_NEXT_50 = dt["indexcode"]
                    if dt["indexname"] == "Nifty PSE":
                        NIFTY_PSE = dt["indexcode"]
                    if dt["indexname"] == "Nifty PSU Bank":
                        NIFTY_PSU_BANK = dt["indexcode"]
                    if dt["indexname"] == "Nifty Realty":
                        NIFTY_REALITY = dt["indexcode"]
                    if dt["indexname"] == "Nifty Serv Sector":
                        NIFTY_SERV_SECTOR = dt["indexcode"]
                    if dt["indexname"] == "Nifty SMLCAP 100":
                        NIFTY_SMALLCAP_100 = dt["indexcode"]
                    if dt["indexname"] == "Nifty CPSE":
                        NIFTY_CPSE = dt["indexcode"]
                    if dt["indexname"] == "India VIX":
                        INDIA_VIX = dt["indexcode"]
                    if dt["indexname"] == "Nifty100 Liq 15":
                        NIFTY100_LIQ_15 = dt["indexcode"]
                    if dt["indexname"] == "Nifty GrowSect 15":
                        NIFTY_GROWSECT_15 = dt["indexcode"]
                    if dt["indexname"] == "Nifty Midcap 50":
                        NIFTY_MIDCAP_50 = dt["indexcode"]
                    if dt["indexname"] == "Nifty MID SELECT":
                        NIFTY_MID_SELECT = dt["indexcode"]

                context = {
                    "nifty50": "N" + str(NIFTY_FIFTY),
                    "nifty100": "N" + str(NIFTY_hundred),
                    "nifty200": "N" + str(NIFTY_twohundred),
                    "niftybank": "N" + str(NIFTY_bank),
                    "niftyauto": "N" + str(NIFTY_auto),
                    "niftyfmcg": "N" + str(NIFTY_fmcg),
                    "niftypharma": "N" + str(NIFTY_pharma),
                    "nifty_mid_select": "N" + str(NIFTY_MID_SELECT),
                    "nifty_midcap_50": "N" + str(NIFTY_MIDCAP_50),
                    "nifty_growsect_15": "N" + str(NIFTY_GROWSECT_15),
                    "nifty_liq_15": "N" + str(NIFTY100_LIQ_15),
                    "india_vix": "N" + str(INDIA_VIX),
                    "nifty_cpse": "N" + str(NIFTY_CPSE),
                    "nifty_smallcap_100": "N" + str(NIFTY_SMALLCAP_100),
                    "nifty_serv_sector": "N" + str(NIFTY_SERV_SECTOR),
                    "nifty_realty": "N" + str(NIFTY_REALITY),
                    "nifty_psu_bank": "N" + str(NIFTY_PSU_BANK),
                    "nifty_pse": "N" + str(NIFTY_PSE),
                    "nifty_next_50": "N" + str(NIFTY_NEXT_50),
                    "nifty_mnc": "N" + str(NIFTY_MNC),
                    "nifty_metal": "N" + str(NIFTY_METAL),
                    "nifty_midcap_100": "N" + str(NIFTY_MIDCAP_100),
                    "nifty_media": "N" + str(NIFTY_MEDIA),
                    "nifty_it": "N" + str(NIFTY_IT),
                    "nifty_infra": "N" + str(NIFTY_INFRA),
                    "nifty_fin_service": "N" + str(NIFTY_FIN_SERVICE),
                    "nifty_energy": "N" + str(NIFTY_ENERGY),
                    "nifty_div_opps_50": "N" + str(NIFTY_DIV_OPPS_50),
                    "nifty_consumption": "N" + str(NIFTY_CONSUMPTION),
                    "nifty_commodities": "N" + str(NIFTY_COMMODITIES),
                    "nifty_500": "N" + str(NIFTY_500),
               
                }

                NSEData = {
                    "clientcode": clientcode,
                    "exchange": "NSE",
                    "scripcode": NIFTY_FIFTY
                }
      
                get_ltp = Mofsl.GetLtp(NSEData)
                print(get_ltp)

                context1 = BSEDATA(request)
                print(context1)

                context.update({
                    "sensex": "B" + str(context1.get('sensex', ''))
                })

                daata = {
                        "clientid": clientcode,
                        "authtoken": loginmofsl["AuthToken"],
                        "apikey": ApiKey
                    }
                manish = {'clientcode':clientcode,'api':ApiKey,'token':loginmofsl['AuthToken']}
                print("daataa")
                print(daata)

                print("res data")

                url_place = "https://openapi.motilaloswal.com/rest/trans/v1/placeorder"

                place_order_request = {
                    "clientcode": "clientcode",
                    "exchange": "NSE",
                    "symboltoken": 1660,
                    "buyorsell": "BUY",
                    "ordertype": "LIMIT",
                    "producttype": "DELIVERY",
                    "orderduration": "DAY",
                    "price": 235.5,
                    "triggerprice": 0,
                    "quantityinlot": 2,
                    "disclosedquantity": 0,
                    "amoorder": "N",
                    "algoid": "",
                    "goodtilldate": "",
                    "tag": " ",
                    "participantcode": ""
                }
                respo_place = requests.post(url_place, json=place_order_request, headers=headers)
                print("response place order")
                print(respo_place)
                print(respo_place.text)

                current_date_time = datetime.now()

                # Format the current date and time
                formatted_current_date_time = current_date_time.strftime('%d-%b-%Y %H:%M:%S')
                OrderBookInfo = {
                    "clientcode": clientcode,
                    "dateandtime": formatted_current_date_time
                }
                print("order book")
                print(OrderBookInfo)
                # Replace with your actual implementation
                orderbook = Mofsl.GetOrderBook(OrderBookInfo)
                print("response order book ")
                print(orderbook)

                print("res data")
                return render(request, template_detail_page, {'alldata': context, 'mani': manish})
            except ValueError as e:
                print("Error decoding JSON:", e)
                return JsonResponse({"error": "Error decoding JSON"})
        else:
            print("Request failed with status code:", response_nse.status_code)
            print("Response content:", response_nse.text)
            return JsonResponse({"error": "Request failed with status code " + str(response_nse.status_code)})

    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": "An error occurred: " + str(e)})

def stock_chart(request, symbol):
    stock_data = get_stock_data(symbol)
    return render(request, 'stock_chart.html', {'stock_data': stock_data})

# def NSE_BSE_data(request):
#     print("in nse bse")

#     url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"

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
#         "exchangename": "NSE"
#     }
#     print("calling NSE_BSE_data func")
#     # NSE_BSE_data(request)
#     response_nse = requests.post(url, json=data, headers=headers)
#     print('resonse nse', response_nse)
   
#     # file_path = "example3.json"

#     # Writing data to the JSON file
#     # with open(file_path, 'w') as json_file:
#     #     json.dump(response, json_file)
#     #     print("done in example ")
#     # print(response_nse)
#     # print(response_nse.text)
#     # print("json")
#     # print(response_nse.json())
#     NIFTY = ""
#     NIFTY_FIFTY = ""
#     NIFTY_bank = ""
#     NIFTY_twohundred =""
#     NIFTY_hundred =""
#     print("done")
#     res =  response_nse.json()
#     print(res['data'])
#     responce_data = res['data']
#     print("data dict", responce_data)
#     # print("parsed one")
#     scripc = ""
    
#     for dt in responce_data:
#         # print(dt["indexcode"])
#         # if dt == 'data':
#         #     for i in dt:
#         #         print(i)
#         if dt["indexname"] == "Nifty 50":
#             NIFTY_FIFTY = dt["indexcode"]
#             scripc = dt['indexcode']

#         if dt["indexname"] == "Nifty 100":
#             NIFTY_hundred = dt["indexcode"]

#         if dt["indexname"] == "Nifty 200":
#             NIFTY_twohundred = dt["indexcode"]

#         if dt["indexname"] == "Nifty Bank":
#             NIFTY_bank = dt["indexcode"]
        
#         if dt["indexname"] == "Nifty Auto":
#             NIFTY_auto = dt["indexcode"]
        
#         if dt["indexname"] == "Nifty FMCG":
#             NIFTY_fmcg = dt["indexcode"]

#         if dt["indexname"] == "Nifty Pharma":
#             NIFTY_pharma = dt["indexcode"]


#     # print(type(NIFTY))
#     context = {
#         "nifty50":NIFTY_FIFTY,
#         "nifty100":NIFTY_hundred,
#         "nifty200":NIFTY_twohundred,
#         "niftybank":NIFTY_bank,
#         "niftyauto":NIFTY_auto,
#         "niftyfmcg":NIFTY_fmcg,
#         "niftypharma":NIFTY_pharma
#     }
#     NSEData = {
#         "clientcode":clientcode,
#         "exchange":"NSE",
#         "scripcode":NIFTY_FIFTY
#     }
#     get_ltp = Mofsl.GetLtp(NSEData)
#     print(get_ltp)
#     context1 = BSEDATA(request)
#     # print("bse return ")
#     print(context1)
#     # print("N"+str(NIFTY_FIFTY))
#     context = {
#         "nifty50":"N"+str(NIFTY_FIFTY),
#         "nifty100":"N"+str(NIFTY_hundred),
#         "nifty200":"N"+str(NIFTY_twohundred),
#         "niftybank":"N"+str(NIFTY_bank),
#         "niftyauto":"N"+str(NIFTY_auto),
#         "niftyfmcg":"N"+str(NIFTY_fmcg),
#         "niftypharma":"N"+str(NIFTY_pharma),
#         "sensex":"B"+str(context1['sensex'])
#     }
#     # url_web = "wss://openapi.motilaloswal.com/"
    
#     # redirect('web_conn')
#     daata = {
#         "clientid": clientcode,
#         "authtoken": loginmofsl["AuthToken"],
#         "apikey": ApiKey
#     }
#     manish = {'clientcode':clientcode,'api':ApiKey,'token':loginmofsl['AuthToken']}
#     print("daataa")
#     print(daata)
#     # Mofsl.Broadcast_connect()
    
#     # res = request.get(url_web, json=daata, headers=headers)
#     # tcpconnect = Mofsl.TCPBroadcast_connect()
#     # print("tcp connection")
#     # print(tcpconnect)
#     # tcpcall = Mofsl.__TCPBroadcast_on_open()
#     # print("open")
#     # print(tcpcall)

#     # view_data = ChartConsumer()
#     # vie = view_data.connect()
#     # print(vie)

#     # async with websockets.connect(url_web) as websocket:
#     #     await websocket.send(json.dumps(daata))
#     #     response = await websocket.recv()

#     print("res data")
#     # print(response)
#     print("res data")
#     url_place = "https://openapi.motilaloswal.com/rest/trans/v1/placeorder"

#     place_order_request = {
#         "clientcode":clientcode,
#         "exchange":"NSE",
#         "symboltoken":1660,
#         "buyorsell":"BUY",
#         "ordertype":"LIMIT",
#         "producttype":"DELIVERY",
#         "orderduration":"DAY",
#         "price":235.5,
#         "triggerprice":0,
#         "quantityinlot":2,
#         "disclosedquantity":0,
#         "amoorder":"N",
#         "algoid":"",
#         "goodtilldate":"",
#         "tag":" ", 
#         "participantcode": ""
#     }
#     respo_place = requests.post(url_place, json=place_order_request, headers=headers)
#     print("response place order")
#     print(respo_place)
#     print(respo_place.text)
#     current_date_time = datetime.now()

#     # Format the current date and time
#     formatted_current_date_time = current_date_time.strftime('%d-%b-%Y %H:%M:%S')
#     OrderBookInfo = {
#         "clientcode":clientcode,
#         "dateandtime":formatted_current_date_time
#     }
#     print("order book")
#     print(OrderBookInfo)
#     orderbook = Mofsl.GetOrderBook(OrderBookInfo)
#     print("responce order book ")
#     print(orderbook)
#     # print(res)
#     # web_con = Mofsl.Websocket2_connect()
#     # print("web_connection")
#     # print(web_con)
    

#     # get_conn = ChartConsumer.connect()
#     # print(get_conn)

#     # triggerwebhook = tradingchart(request,loginmofsl["AuthToken"])

#     # print(triggerwebhook)

#     # for ct in triggerwebhook:
#     #     if 
#     # print(context)
#     return render(request, 'market_dashboard/template/market_dash.html',{'alldata':context, 'mani':manish})


#     # print(NIFTY_FIFTY)
#     # print(NIFTY_hundred)
#     # print(NIFTY_twohundred)
#     # print(NIFTY_bank)


def returningdatamofsl(request):
    print("in return")
    daata = {
    "clientid": clientcode,
    "authtoken": loginmofsl["AuthToken"],
    "apikey": ApiKey
    }

    return daata
def loginmofsl(request):
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

def getltpbycode(request,code):
    print(code)
    codeval = code[0]
    code = code[1:]
    print(codeval)
    print(code)
    exchage = ""
    if codeval == "N":
        exchage = "NSE"
    if codeval == "B":
        exchage = "BSE"
    LTPData = {
        "clientcode":clientcode,
        "exchange":exchage,
        "scripcode":int(code)
    }
    print(LTPData)
    get_ltp = Mofsl.GetLtp(LTPData)



    if get_ltp['status'] =="SUCCESS":
        detailLtpData = get_ltp['data']

        return render(request, 'market_dashboard/template/detail_page.html',{'alldata':detailLtpData})

    else:
        return render(request, 'market_dashboard/template/detail_page.html',{'alldata':get_ltp})




    print('json value')
    # response_data = Mofsl.GetLtp(LTPData).json()
    # ltpcontext = response_data.get('data', {})

    # print(getltp.json())
    # getjson = get_ltp.json()

    # ltpcontext = getjson['data']
    # print("ltp context")
    # print(ltpcontext)


    # print("ltp data")
    # print(getltp)
    # print(getltp.text)
    # print(getltp.json())
    
    
    
    # getting_bse_data = BSEDATA(request,url,clientcode,headers)
    # print("print bse ")
    # print(getting_bse_data)

    # nse_data = {
    #     "clientcode":clientcode,
    #     "exchange":"NSE",
    #     # "scripcode":26000
    # }

    # bse_data = {
    #     "clientcode":clientcode,
    #     "exchange":"BSE",
    #     # "scripcode":500317
    # }

    # response_bse = requests.post(url, json=bse_data, headers=headers)
    # response_nse = requests.post(url, json=nse_data, headers=headers)


    # totp = input("Enter Input: ")
    # loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)

    # if loginmofsl['status'] == 'SUCCESS':
    #     print("Login successful")
    
    # getinstrument = Mofsl.GetInstrumentFile('NSE',clientcode)
    # file_path = "example.json"

    # Writing data to the JSON file
    # with open(file_path, 'w') as json_file:
    #     json.dump(getinstrument, json_file)
    #     print("done in example ")
    # print("json bse")
    # print(response_bse.json())
    # print("json nse")
    # print(response_nse.json())

    # getindexdata = Mofsl.GetLtp(nse_data,bse_data)
    # print("grt ltp data")
    # print(getindexdata)

    return render(request, 'market/detailpage.html',{'alldata':ltpcontext})


def BSEDATA(request):
    # ApiKey = "MHohVro9A0A1Q2Sw"
    # userid = "EBOM907310"
    # password = "@Massy512"
    # Two_FA = "05/01/2000"
    # vendorinfo = "EBOM907310"
    # clientcode = "EBOM907310"
    # SourceID = "Desktop"
    # browsername = "chrome"
    # browserversion = "104"

    # # Base URL for MOFSL API
    # Base_Url = "https://openapi.motilaloswal.com"
    # # Initialize MOFSL API
    # Mofsl = MOFSLOPENAPI(ApiKey, Base_Url, clientcode, SourceID, browsername, browserversion)
    # totp = input("Enter Input: ")
    # loginmofsl = Mofsl.login(userid, password, Two_FA, totp,vendorinfo)
    print("login bse")
    url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"

    header = {
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

    jsondata = {
        "clientcode": clientcode,  # In case of dealer else not required
        "exchangename": "BSE"
    }
    response = requests.post(url, json=jsondata, headers=header)
    SENSEX = ""
    res1 =  response.json()
    print("responce bse")
    # print(res1)
    responce_bse = res1['data']
    print("data")
    # print(responce_bse)
    SENSEX =""
    for st in responce_bse:
        if st["indexname"] == "SENSEX":
            SENSEX = st["indexcode"]

    contexts1 = {
        "sensex":SENSEX,
    }
    # print(contexts1)
    # BSEData = {
    #     "clientcode":clientcode,
    #     "exchange":"BSE",
    #     "scripcode":SENSEX
    # }

    # get_bse_ltp = Mofsl.GetLtp(BSEData)
    # print(get_bse_ltp)
    return contexts1

    

    

def detailpage(request,code):
    print(code)
    return render(request, 'market/detailpage.html')


# Tradebook
def tradebook(request):
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
    print(loginmofsl)
    gettrade = Mofsl.TradeWebhook(clientcode)
    print("trade")
    print(gettrade)
   
    return render(request, 'market/home.html')



def stocksInfo(request):
    stock_list = request.GET.getlist('stock_list')
    request.session.create()
    stock_details = {}
    for stock in stock_list:
        stock_detail = get_quote_table(stock)
        stock_details.update({stock:stock_detail})
        
def tradingchart(request,authtoken):
    # print(loginmofsl["AuthToken"])
    print("in trading ")

 

    headers = {
        "Accept": "application/json",
        "User-Agent": "MOSL/V.1.1.0",
        "Authorization": authtoken,
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
    print(headers)

    url = "	https://openapi.motilaloswal.com/webhook"
    data = {
    "clientid": clientcode,
    "authtoken":authtoken ,
    "apikey": ApiKey
    }
    print(data)
    response_trade_webhook = requests.post(url, json=data, headers=headers)
    tradewebhook = Mofsl.TradeWebhook(userid)   
    print("trade webhook by id")
    print(tradewebhook)
    print(response_trade_webhook)
    print(response_trade_webhook.text)
    print("json")
    print(response_trade_webhook.json())
   
    print("done")
    res =  response_trade_webhook.json()
    print(res)
    print("parsed one")
    return res


    # return render(request, 'market/home.html')



def Portfolio(request):
    return render (request, 'market/portfolio.html')

def MutualFund(request):
    return render (request, 'market/mutualfund.html')

def option_store(request):
    return render (request, 'market/option_store.html')

def help_me_invest(request):
    return render (request, 'market/help_me_invest.html')

def fnoanalytics(request):
    url = "https://mcharts.motilaloswal.com/Find20/Derivatives/FNOFuture/Heatmap"
    response = requests.get(url)
    get_html = BeautifulSoup(response.content, "html.parser")
    print(get_html)

    return render (request, 'market/fnoanalytics.html', {"html_content": get_html})


def all_nse_bse_indices(request):

    url = "https://openapi.motilaloswal.com/rest/report/v1/getindexdatabyexchangename"
    url_get_ltp = "	https://openapi.motilaloswal.com/rest/report/v1/getltpdata"
    url_eod_data = "https://openapi.motilaloswal.com/rest/report/v1/geteoddatabyexchangename"
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

    nse_data = {
        "clientcode":clientcode, 
        "exchangename":"NSE"
        }
 
    response_nse_index = requests.post(url, json=nse_data, headers=headers )
    res_nse_index = response_nse_index.json()
    data_n = res_nse_index.get ('data', [])


    context = []
   
    for indices_data in data_n:
        nse_index_code = indices_data['indexcode']
        nse_index_name = indices_data['indexname']

        nse_ohlc_data = {
            "clientcode":clientcode,
            "exchange":"NSE",
            "scripcode":nse_index_code
        }
        response_scrip = requests.post(url_get_ltp, json=nse_ohlc_data, headers=headers )
        res_nse_scrip = response_scrip.json()
        data_n_scrip = res_nse_scrip.get ('data', [])

      


        open = data_n_scrip['open']
        high = data_n_scrip['high']
        low = data_n_scrip['low']
        close = data_n_scrip['close']
        ltp = data_n_scrip['ltp']
        volume = data_n_scrip['volume']
        ask = data_n_scrip['ask']
        bid = data_n_scrip['bid']

        

        context.append({
            "indexcode": nse_index_code,
            "indexname": nse_index_name,
            "open" : open,
            "high" : high,
            "low" : low,
            "close" : close,
            "ltp" : ltp,
            "volume" : volume,
            "ask" : ask,
            "bid" : bid,
        })

    return render(request, 'market_dashboard/template/all_indices.html',{"all_data":context})


def stock_options_data(request):

    context = []
    url_eod_data = "https://openapi.motilaloswal.com/rest/report/v1/geteoddatabyexchangename"

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

    eod_data =    {
            "clientcode":"AA020",
            "exchangename":"NSEFO"
            }
        
    response_eod = requests.post(url_eod_data, json=eod_data, headers=headers )
    res_nse_eod = response_eod.json()
    data_n_eod = res_nse_eod.get ('data', [])

    for stock_op_data in data_n_eod:
   

        open = stock_op_data['open']
        high = stock_op_data['high']
        low = stock_op_data['low']
        close = stock_op_data['close']
    
        volume = stock_op_data['volume']
        scrip_fullname = stock_op_data['scripfullname']
        exchange_name = stock_op_data['exchange']
        instrument_name = stock_op_data['instrumentname']
    
        expiry_date = stock_op_data['expirydate']
        date = stock_op_data['date']
        Scrip_shortname = stock_op_data['scripshortname']
        strike_price = stock_op_data['strikeprice']
        option_type = stock_op_data['optiontype']

        

        context.append({
            "scrip_fullname": scrip_fullname,
            "instrument_name": instrument_name,
            "open" : open,
            "high" : high,
            "low" : low,
            "close" : close,
            "exchange_name" : exchange_name,
            "volume" : volume,
            "expiry_date" : expiry_date,
            "date" : date,
            "Scrip_shortname" : Scrip_shortname,
            "strike_price" : strike_price,
            "option_type" : option_type,
        
        })

    return render(request, 'market_dashboard/template/derivative_data.html',{"all_data":context})

                                
    #             return render(request, 'market_dashboard/template/all_indices.html')
    #         except json.JSONDecodeError as e:
      
    #             print(f"JSONDecodeError: {e}")
    #             print("Response Content:", response_data.content.decode())

    #         return HttpResponseServerError("Error decoding JSON response.")
    #     else:
    #         # If the request was not successful, handle the error
    #         error_message = f"Error: {response_data.status_code} - {response_data.text}"
    #         print(error_message)
    #         # You might want to handle the error in a way that makes sense for your application
    #         return render(request, 'market_dashboard/template/404.html', {"error_message": error_message})
    
    # except Exception as e:
    #     print("An error occurred:", e)
    #     return JsonResponse({"error": "An error occurred: "})