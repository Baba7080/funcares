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

    data_nse = {
        "clientcode": clientcode, 
        "exchangename": "NSE"
    }
    print("callingdfghhhgff NSE_BSE_data func")

    nse_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26009
                }
    
    nifty_100_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26012
                
                }
    nifty_200_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26065
                
                }
    nifty_500_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26003
                
                }
    nifty_auto_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26061
                
                }
    nifty_commidities_ohlc = {
                "clientcode": clientcode,
                "exchange":"NSE",
                "scripcode": 26066
                
                }
    nifty_consumption_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26067
                
                }
    nifty_div_opps_50_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26069
                
                }
    nifty_energy_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26054
                
                }
    nifty_fin_service_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26037
                
                }
    nifty_fmcg_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26055
                
                }
    nifty_infra_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26019
                
                }
    nifty_it_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26008
                
                }
    nifty_media_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26063
                
                }
    nifty_metal_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26062
                
                }
    nifty_midcap_100_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26010
                
                }
    nifty_mnc_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26056
                
                }
    nifty_50_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26000
                
                }
    nifty_next_50_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26013
                
                }
    nifty_pharma_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26057
                
                }
    nifty_pse_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26024
                
                }
    nifty_psu_bank_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26059
                
                }
    nifty_realty_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26052
                
                }
    nifty_serv_sector_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26060
                
                }
    nifty_smlcap_100_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26064
                
                }
    nifty_cpse_ohlc = {
                "clientcode": clientcode,
                "exchange":"NSE",
                "scripcode": 26027
                
                }
    # india_vix_ohlc = {
    #             "clientcode": clientcode,
    #             "exchange": "India VIX",
    #             "scripcode": 26051
                
    #             }
    nifty_liq_15_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26070
                
                }
    nifty_growsect_15_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26071
                
                }
    nifty_midcap_50_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26014
                
                }
    nifty_mid_select_ohlc = {
                "clientcode": clientcode,
                "exchange": "NSE",
                "scripcode": 26074
                
                }

    try:
        response_eod_data = requests.post(url_eod_data, json=data_nse, headers=headers)

        response_nse = requests.post(url, json=data_nse, headers=headers)

        response_nse_ohlc = requests.post(url_get_ltp, json=nse_ohlc, headers=headers)
        response_nifty_100_ohlc = requests.post(url_get_ltp, json=nifty_100_ohlc, headers=headers)
        response_nifty_200_ohlc = requests.post(url_get_ltp, json=nifty_200_ohlc, headers=headers)
        response_nifty_500_ohlc = requests.post(url_get_ltp, json=nifty_500_ohlc, headers=headers)
        response_nifty_auto_ohlc = requests.post(url_get_ltp, json=nifty_auto_ohlc, headers=headers)
        response_nifty_commidities_ohlc = requests.post(url_get_ltp, json=nifty_commidities_ohlc, headers=headers)
        response_nifty_consumption_ohlc = requests.post(url_get_ltp, json=nifty_consumption_ohlc, headers=headers)
        response_nifty_div_opps_50_ohlc = requests.post(url_get_ltp, json=nifty_div_opps_50_ohlc, headers=headers)
        response_nifty_energy_ohlc = requests.post(url_get_ltp, json=nifty_energy_ohlc, headers=headers)
        response_nifty_fin_service_ohlc = requests.post(url_get_ltp, json=nifty_fin_service_ohlc, headers=headers)
        response_nifty_fmcg_ohlc = requests.post(url_get_ltp, json=nifty_fmcg_ohlc, headers=headers)
        response_nifty_infra_ohlc = requests.post(url_get_ltp, json=nifty_infra_ohlc, headers=headers)
        response_nifty_it_ohlc = requests.post(url_get_ltp, json=nifty_it_ohlc, headers=headers)
        response_nifty_media_ohlc = requests.post(url_get_ltp, json=nifty_media_ohlc, headers=headers)
        response_nifty_metal_ohlc = requests.post(url_get_ltp, json=nifty_metal_ohlc, headers=headers)
        response_nifty_midcap_100_ohlc = requests.post(url_get_ltp, json=nifty_midcap_100_ohlc, headers=headers)
        response_nifty_mnc_ohlc = requests.post(url_get_ltp, json=nifty_mnc_ohlc, headers=headers)
        response_nifty_50_ohlc = requests.post(url_get_ltp, json=nifty_50_ohlc, headers=headers)
        response_nifty_next_50_ohlc = requests.post(url_get_ltp, json=nifty_next_50_ohlc, headers=headers)
        response_nifty_pharma_ohlc = requests.post(url_get_ltp, json=nifty_pharma_ohlc, headers=headers)
        response_nifty_pse_ohlc = requests.post(url_get_ltp, json=nifty_pse_ohlc, headers=headers)
        response_nifty_psu_bank_ohlc = requests.post(url_get_ltp, json=nifty_psu_bank_ohlc, headers=headers)
        response_nifty_realty_ohlc = requests.post(url_get_ltp, json=nifty_realty_ohlc, headers=headers)
        response_nifty_serv_sector_ohlc = requests.post(url_get_ltp, json=nifty_serv_sector_ohlc, headers=headers)
        response_nifty_smlcap_100_ohlc = requests.post(url_get_ltp, json=nifty_smlcap_100_ohlc, headers=headers)
        response_nifty_cpse_ohlc = requests.post(url_get_ltp, json=nifty_cpse_ohlc, headers=headers)
        response_nifty_liq_15_ohlc = requests.post(url_get_ltp, json=nifty_liq_15_ohlc, headers=headers)
        response_nifty_growsect_15_ohlc = requests.post(url_get_ltp, json=nifty_growsect_15_ohlc, headers=headers)
        response_nifty_midcap_50_ohlc = requests.post(url_get_ltp, json=nifty_midcap_50_ohlc, headers=headers)
        response_nifty_mid_select_ohlc = requests.post(url_get_ltp, json=nifty_mid_select_ohlc, headers=headers)

        print('response nse', response_nse)
        print('response nse ohlc', response_nse_ohlc)



        if [response_eod_data.status_code,
            response_nse.status_code, response_nse_ohlc.status_code,
            response_nifty_100_ohlc.status_code,response_nifty_200_ohlc.status_code,
            response_nifty_500_ohlc.status_code,response_nifty_auto_ohlc.status_code,
            response_nifty_commidities_ohlc.status_code,response_nifty_consumption_ohlc.status_code,
            response_nifty_div_opps_50_ohlc.status_code,response_nifty_energy_ohlc.status_code,
            response_nifty_fin_service_ohlc.status_code,response_nifty_fmcg_ohlc.status_code,
            response_nifty_infra_ohlc.status_code,response_nifty_it_ohlc.status_code,
            response_nifty_media_ohlc.status_code,response_nifty_metal_ohlc.status_code,
            response_nifty_midcap_100_ohlc.status_code,response_nifty_mnc_ohlc.status_code,
            response_nifty_50_ohlc.status_code,response_nifty_next_50_ohlc.status_code,
            response_nifty_pharma_ohlc.status_code,response_nifty_pse_ohlc.status_code,
            response_nifty_psu_bank_ohlc.status_code,response_nifty_realty_ohlc.status_code,
            response_nifty_serv_sector_ohlc.status_code,response_nifty_smlcap_100_ohlc.status_code,
            response_nifty_cpse_ohlc.status_code,response_nifty_liq_15_ohlc.status_code,
            response_nifty_growsect_15_ohlc.status_code,response_nifty_midcap_50_ohlc.status_code,
            response_nifty_mid_select_ohlc.status_code

            ] == 200:

            try:
                #convert to json
                json_eod_data = response_eod_data.json()

                json_data = response_nse.json()
                
                json_nse_ohlc = response_nse_ohlc.json()
                json_nifty_100_ohlc = response_nifty_100_ohlc.json()
                json_nifty_200_ohlc = response_nifty_200_ohlc.json()
                json_nifty_500_ohlc = response_nifty_500_ohlc.json()
                json_nifty_auto_ohlc = response_nifty_auto_ohlc.json()
                json_nifty_commidities_ohlc = response_nifty_commidities_ohlc.json()
                json_nifty_consumption_ohlc = response_nifty_consumption_ohlc.json()
                json_nifty_div_opps_50_ohlc = response_nifty_div_opps_50_ohlc.json()
                json_nifty_energy_ohlc = response_nifty_energy_ohlc.json()
                json_nifty_fin_service_ohlc = response_nifty_fin_service_ohlc.json()
                json_nifty_fmcg_ohlc = response_nifty_fmcg_ohlc.json()
                json_nifty_infra_ohlc = response_nifty_infra_ohlc.json()
                json_nifty_it_ohlc = response_nifty_it_ohlc.json()
                json_nifty_media_ohlc = response_nifty_media_ohlc.json()
                json_nifty_metal_ohlc = response_nifty_metal_ohlc.json()
                json_nifty_midcap_100_ohlc = response_nifty_midcap_100_ohlc.json()
                json_nifty_mnc_ohlc = response_nifty_mnc_ohlc.json()
                json_nifty_50_ohlc = response_nifty_50_ohlc.json()
                json_nifty_next_50_ohlc = response_nifty_next_50_ohlc.json()
                json_nifty_pharma_ohlc = response_nifty_pharma_ohlc.json()
                json_nifty_pse_ohlc = response_nifty_pse_ohlc.json()
                json_nifty_psu_bank_ohlc = response_nifty_psu_bank_ohlc.json()
                json_nifty_realty_ohlc = response_nifty_realty_ohlc.json()
                json_nifty_serv_sector_ohlc = response_nifty_serv_sector_ohlc.json()
                json_nifty_smlcap_100_ohlc = response_nifty_smlcap_100_ohlc.json()
                json_nifty_cpse_ohlc = response_nifty_cpse_ohlc.json()
                json_nifty_liq_15_ohlc = response_nifty_liq_15_ohlc.json()
                json_nifty_growsect_15_ohlc = response_nifty_growsect_15_ohlc.json()
                json_nifty_midcap_50_ohlc = response_nifty_midcap_50_ohlc.json()
                json_nifty_mid_select_ohlc = response_nifty_mid_select_ohlc.json()

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
               

                #get index json data
                response_eod_get = json_eod_data.get('data', [])
                print('response e=od data', response_eod_get)

                print("error")
                response_data = json_data.get('data', [])

                print("error")
                res_nse_ohlc = json_nse_ohlc.get('data')
                res_nifty_100_ohlc = json_nifty_100_ohlc.get('data')
                res_nifty_200_ohlc = json_nifty_200_ohlc.get('data')
                res_nifty_500_ohlc = json_nifty_500_ohlc.get('data')
                res_nifty_auto_ohlc = json_nifty_auto_ohlc.get('data')   
                res_nifty_commidities_ohlc = json_nifty_commidities_ohlc.get('data')
                res_nifty_consumption_ohlc = json_nifty_consumption_ohlc.get('data')
                res_nifty_div_opps_50_ohlc = json_nifty_div_opps_50_ohlc.get('data')
                res_nifty_energy_ohlc = json_nifty_energy_ohlc.get('data')
                res_nifty_fin_service_ohlc = json_nifty_fin_service_ohlc.get('data')
                res_nifty_fmcg_ohlc = json_nifty_fmcg_ohlc.get('data')
                res_nifty_infra_ohlc = json_nifty_infra_ohlc.get('data')
                res_nifty_it_ohlc = json_nifty_it_ohlc.get('data')
                res_nifty_media_ohlc = json_nifty_media_ohlc.get('data')
                res_nifty_metal_ohlc = json_nifty_metal_ohlc.get('data')
                res_nifty_midcap_100_ohlc = json_nifty_midcap_100_ohlc.get('data')
                res_nifty_mnc_ohlc = json_nifty_mnc_ohlc.get('data')
                res_nifty_50_ohlc = json_nifty_50_ohlc.get('data')
                res_nifty_next_50_ohlc = json_nifty_next_50_ohlc.get('data')
                res_nifty_pharma_ohlc = json_nifty_pharma_ohlc.get('data')
                res_nifty_pse_ohlc = json_nifty_pse_ohlc.get('data')
                res_nifty_psu_bank_ohlc = json_nifty_psu_bank_ohlc.get('data')
                res_nifty_realty_ohlc = json_nifty_realty_ohlc.get('data')
                res_nifty_serv_sector_ohlc = json_nifty_serv_sector_ohlc.get('data')
                res_nifty_smlcap_100_ohlc = json_nifty_smlcap_100_ohlc.get('data')
                res_nifty_cpse_ohlc = json_nifty_cpse_ohlc.get('data')
                res_nifty_liq_15_ohlc = json_nifty_liq_15_ohlc.get('data')
                res_nifty_growsect_15_ohlc = json_nifty_growsect_15_ohlc.get('data')
                res_nifty_midcap_50_ohlc = json_nifty_midcap_50_ohlc.get('data')
                res_nifty_mid_select_ohlc = json_nifty_mid_select_ohlc.get('data')
                
                
               
                # Nifty Bank OHLC start
                nifty_bank_op = res_nse_ohlc['open']
                nifty_bank_hg = res_nse_ohlc['high']
                nifty_bank_lw = res_nse_ohlc['low']
                nifty_bank_cl = res_nse_ohlc['close']
                nifty_bank_lt = res_nse_ohlc['ltp']
                nifty_bank_vlme = res_nse_ohlc['volume']
                nifty_bank_ak = res_nse_ohlc['ask']
                nifty_bank_bd = res_nse_ohlc['bid']
                # Nifty bank OHLC end

                # Nifty 100 OHLC start
                nifty_100_op = res_nifty_100_ohlc['open']
                nifty_100_hg = res_nifty_100_ohlc['high']
                nifty_100_lw = res_nifty_100_ohlc['low']
                nifty_100_cl = res_nifty_100_ohlc['close']
                nifty_100_lt = res_nifty_100_ohlc['ltp']
                nifty_100_vlme = res_nifty_100_ohlc['volume']
                nifty_100_ak = res_nifty_100_ohlc['ask']
                nifty_100_bd = res_nifty_100_ohlc['bid']
                # Nifty 100 OHLC end

                # Nifty 200 OHLC start
                nifty_200_op = res_nifty_200_ohlc['open']
                nifty_200_hg = res_nifty_200_ohlc['high']
                nifty_200_lw = res_nifty_200_ohlc['low']
                nifty_200_cl = res_nifty_200_ohlc['close']
                nifty_200_lt = res_nifty_200_ohlc['ltp']
                nifty_200_vlme = res_nifty_200_ohlc['volume']
                nifty_200_ak = res_nifty_200_ohlc['ask']
                nifty_200_bd = res_nifty_200_ohlc['bid']
                # Nifty 200 OHLC end

                # Nifty 500 OHLC start
                nifty_500_op = res_nifty_500_ohlc['open']
                nifty_500_hg = res_nifty_500_ohlc['high']
                nifty_500_lw = res_nifty_500_ohlc['low']
                nifty_500_cl = res_nifty_500_ohlc['close']
                nifty_500_lt = res_nifty_500_ohlc['ltp']
                nifty_500_vlme = res_nifty_500_ohlc['volume']
                nifty_500_ak = res_nifty_500_ohlc['ask']
                nifty_500_bd = res_nifty_500_ohlc['bid']
                # Nifty 500 OHLC end

                # Nifty auto OHLC start
                nifty_auto_op = res_nifty_auto_ohlc['open']
                nifty_auto_hg = res_nifty_auto_ohlc['high']
                nifty_auto_lw = res_nifty_auto_ohlc['low']
                nifty_auto_cl = res_nifty_auto_ohlc['close']
                nifty_auto_lt = res_nifty_auto_ohlc['ltp']
                nifty_auto_vlme = res_nifty_auto_ohlc['volume']
                nifty_auto_ak = res_nifty_auto_ohlc['ask']
                nifty_auto_bd = res_nifty_auto_ohlc['bid']
                # Nifty auto OHLC end

                # Nifty commodities OHLC start
                nifty_commodities_op = res_nifty_commidities_ohlc['open']
                nifty_commodities_hg = res_nifty_commidities_ohlc['high']
                nifty_commodities_lw = res_nifty_commidities_ohlc['low']
                nifty_commodities_cl = res_nifty_commidities_ohlc['close']
                nifty_commodities_lt = res_nifty_commidities_ohlc['ltp']
                nifty_commodities_vlme = res_nifty_commidities_ohlc['volume']
                nifty_commodities_ak = res_nifty_commidities_ohlc['ask']
                nifty_commodities_bd = res_nifty_commidities_ohlc['bid']
                # Nifty commodities OHLC end

                # Nifty consumption OHLC start
                nifty_consumption_op = res_nifty_consumption_ohlc['open']
                nifty_consumption_hg = res_nifty_consumption_ohlc['high']
                nifty_consumption_lw = res_nifty_consumption_ohlc['low']
                nifty_consumption_cl = res_nifty_consumption_ohlc['close']
                nifty_consumption_lt = res_nifty_consumption_ohlc['ltp']
                nifty_consumption_vlme = res_nifty_consumption_ohlc['volume']
                nifty_consumption_ak = res_nifty_consumption_ohlc['ask']
                nifty_consumption_bd = res_nifty_consumption_ohlc['bid']
                # Nifty consumption OHLC end

                # Nifty div_opps_50 OHLC start
                nifty_div_opps_50_op = res_nifty_div_opps_50_ohlc['open']
                nifty_div_opps_50_hg = res_nifty_div_opps_50_ohlc['high']
                nifty_div_opps_50_lw = res_nifty_div_opps_50_ohlc['low']
                nifty_div_opps_50_cl = res_nifty_div_opps_50_ohlc['close']
                nifty_div_opps_50_lt = res_nifty_div_opps_50_ohlc['ltp']
                nifty_div_opps_50_vlme = res_nifty_div_opps_50_ohlc['volume']
                nifty_div_opps_50_ak = res_nifty_div_opps_50_ohlc['ask']
                nifty_div_opps_50_bd = res_nifty_div_opps_50_ohlc['bid']
                # Nifty div_opps_50 OHLC end

                # Nifty energy OHLC start
                nifty_energy_op = res_nifty_energy_ohlc['open']
                nifty_energy_hg = res_nifty_energy_ohlc['high']
                nifty_energy_lw = res_nifty_energy_ohlc['low']
                nifty_energy_cl = res_nifty_energy_ohlc['close']
                nifty_energy_lt = res_nifty_energy_ohlc['ltp']
                nifty_energy_vlme = res_nifty_energy_ohlc['volume']
                nifty_energy_ak = res_nifty_energy_ohlc['ask']
                nifty_energy_bd = res_nifty_energy_ohlc['bid']
                # Nifty energy OHLC end

                # Nifty fin_service OHLC start
                nifty_fin_service_op = res_nifty_fin_service_ohlc['open']
                nifty_fin_service_hg = res_nifty_fin_service_ohlc['high']
                nifty_fin_service_lw = res_nifty_fin_service_ohlc['low']
                nifty_fin_service_cl = res_nifty_fin_service_ohlc['close']
                nifty_fin_service_lt = res_nifty_fin_service_ohlc['ltp']
                nifty_fin_service_vlme = res_nifty_fin_service_ohlc['volume']
                nifty_fin_service_ak = res_nifty_fin_service_ohlc['ask']
                nifty_fin_service_bd = res_nifty_fin_service_ohlc['bid']
                # Nifty fin_service OHLC end

                # Nifty fmcg OHLC start
                nifty_fmcg_op = res_nifty_fmcg_ohlc['open']
                nifty_fmcg_hg = res_nifty_fmcg_ohlc['high']
                nifty_fmcg_lw = res_nifty_fmcg_ohlc['low']
                nifty_fmcg_cl = res_nifty_fmcg_ohlc['close']
                nifty_fmcg_lt = res_nifty_fmcg_ohlc['ltp']
                nifty_fmcg_vlme = res_nifty_fmcg_ohlc['volume']
                nifty_fmcg_ak = res_nifty_fmcg_ohlc['ask']
                nifty_fmcg_bd = res_nifty_fmcg_ohlc['bid']
                # Nifty fmcg OHLC end

                # Nifty infra OHLC start
                nifty_infra_op = res_nifty_infra_ohlc['open']
                nifty_infra_hg = res_nifty_infra_ohlc['high']
                nifty_infra_lw = res_nifty_infra_ohlc['low']
                nifty_infra_cl = res_nifty_infra_ohlc['close']
                nifty_infra_lt = res_nifty_infra_ohlc['ltp']
                nifty_infra_vlme = res_nifty_infra_ohlc['volume']
                nifty_infra_ak = res_nifty_infra_ohlc['ask']
                nifty_infra_bd = res_nifty_infra_ohlc['bid']
                # Nifty infra OHLC end
                
                # Nifty it OHLC start
                nifty_it_op = res_nifty_it_ohlc['open']
                nifty_it_hg = res_nifty_it_ohlc['high']
                nifty_it_lw = res_nifty_it_ohlc['low']
                nifty_it_cl = res_nifty_it_ohlc['close']
                nifty_it_lt = res_nifty_it_ohlc['ltp']
                nifty_it_vlme = res_nifty_it_ohlc['volume']
                nifty_it_ak = res_nifty_it_ohlc['ask']
                nifty_it_bd = res_nifty_it_ohlc['bid']
                # Nifty it OHLC end

                # Nifty media OHLC start
                nifty_media_op = res_nifty_media_ohlc['open']
                nifty_media_hg = res_nifty_media_ohlc['high']
                nifty_media_lw = res_nifty_media_ohlc['low']
                nifty_media_cl = res_nifty_media_ohlc['close']
                nifty_media_lt = res_nifty_media_ohlc['ltp']
                nifty_media_vlme = res_nifty_media_ohlc['volume']
                nifty_media_ak = res_nifty_media_ohlc['ask']
                nifty_media_bd = res_nifty_media_ohlc['bid']
                # Nifty media OHLC end

                # Nifty metal OHLC start
                nifty_metal_op = res_nifty_metal_ohlc['open']
                nifty_metal_hg = res_nifty_metal_ohlc['high']
                nifty_metal_lw = res_nifty_metal_ohlc['low']
                nifty_metal_cl = res_nifty_metal_ohlc['close']
                nifty_metal_lt = res_nifty_metal_ohlc['ltp']
                nifty_metal_vlme = res_nifty_metal_ohlc['volume']
                nifty_metal_ak = res_nifty_metal_ohlc['ask']
                nifty_metal_bd = res_nifty_metal_ohlc['bid']
                # Nifty metal OHLC end

                # Nifty midcap_100 OHLC start
                nifty_midcap_100_op = res_nifty_midcap_100_ohlc['open']
                nifty_midcap_100_hg = res_nifty_midcap_100_ohlc['high']
                nifty_midcap_100_lw = res_nifty_midcap_100_ohlc['low']
                nifty_midcap_100_cl = res_nifty_midcap_100_ohlc['close']
                nifty_midcap_100_lt = res_nifty_midcap_100_ohlc['ltp']
                nifty_midcap_100_vlme = res_nifty_midcap_100_ohlc['volume']
                nifty_midcap_100_ak = res_nifty_midcap_100_ohlc['ask']
                nifty_midcap_100_bd = res_nifty_midcap_100_ohlc['bid']
                # Nifty midcap_100 OHLC end

                # Nifty mnc OHLC start
                nifty_mnc_op = res_nifty_mnc_ohlc['open']
                nifty_mnc_hg = res_nifty_mnc_ohlc['high']
                nifty_mnc_lw = res_nifty_mnc_ohlc['low']
                nifty_mnc_cl = res_nifty_mnc_ohlc['close']
                nifty_mnc_lt = res_nifty_mnc_ohlc['ltp']
                nifty_mnc_vlme = res_nifty_mnc_ohlc['volume']
                nifty_mnc_ak = res_nifty_mnc_ohlc['ask']
                nifty_mnc_bd = res_nifty_mnc_ohlc['bid']
                # Nifty mnc OHLC end

                # Nifty 50 OHLC start
                nifty_50_op = res_nifty_50_ohlc['open']
                nifty_50_hg = res_nifty_50_ohlc['high']
                nifty_50_lw = res_nifty_50_ohlc['low']
                nifty_50_cl = res_nifty_50_ohlc['close']
                nifty_50_lt = res_nifty_50_ohlc['ltp']
                nifty_50_vlme = res_nifty_50_ohlc['volume']
                nifty_50_ak = res_nifty_50_ohlc['ask']
                nifty_50_bd = res_nifty_50_ohlc['bid']
                # Nifty 50 OHLC end

                # Nifty next_50 OHLC start
                nifty_next_50_op = res_nifty_next_50_ohlc['open']
                nifty_next_50_hg = res_nifty_next_50_ohlc['high']
                nifty_next_50_lw = res_nifty_next_50_ohlc['low']
                nifty_next_50_cl = res_nifty_next_50_ohlc['close']
                nifty_next_50_lt = res_nifty_next_50_ohlc['ltp']
                nifty_next_50_vlme = res_nifty_next_50_ohlc['volume']
                nifty_next_50_ak = res_nifty_next_50_ohlc['ask']
                nifty_next_50_bd = res_nifty_next_50_ohlc['bid']
                # Nifty next_50 OHLC end

                # Nifty pharma OHLC start
                nifty_pharma_op = res_nifty_pharma_ohlc['open']
                nifty_pharma_hg = res_nifty_pharma_ohlc['high']
                nifty_pharma_lw = res_nifty_pharma_ohlc['low']
                nifty_pharma_cl = res_nifty_pharma_ohlc['close']
                nifty_pharma_lt = res_nifty_pharma_ohlc['ltp']
                nifty_pharma_vlme = res_nifty_pharma_ohlc['volume']
                nifty_pharma_ak = res_nifty_pharma_ohlc['ask']
                nifty_pharma_bd = res_nifty_pharma_ohlc['bid']
                # Nifty pharma OHLC end

                # Nifty pse OHLC start
                nifty_pse_op = res_nifty_pse_ohlc['open']
                nifty_pse_hg = res_nifty_pse_ohlc['high']
                nifty_pse_lw = res_nifty_pse_ohlc['low']
                nifty_pse_cl = res_nifty_pse_ohlc['close']
                nifty_pse_lt = res_nifty_pse_ohlc['ltp']
                nifty_pse_vlme = res_nifty_pse_ohlc['volume']
                nifty_pse_ak = res_nifty_pse_ohlc['ask']
                nifty_pse_bd = res_nifty_pse_ohlc['bid']
                # Nifty pse OHLC end

                # Nifty psu_bank OHLC start
                nifty_psu_bank_op = res_nifty_psu_bank_ohlc['open']
                nifty_psu_bank_hg = res_nifty_psu_bank_ohlc['high']
                nifty_psu_bank_lw = res_nifty_psu_bank_ohlc['low']
                nifty_psu_bank_cl = res_nifty_psu_bank_ohlc['close']
                nifty_psu_bank_lt = res_nifty_psu_bank_ohlc['ltp']
                nifty_psu_bank_vlme = res_nifty_psu_bank_ohlc['volume']
                nifty_psu_bank_ak = res_nifty_psu_bank_ohlc['ask']
                nifty_psu_bank_bd = res_nifty_psu_bank_ohlc['bid']
                # Nifty psu_bank OHLC end

                # Nifty realty OHLC start
                nifty_realty_op = res_nifty_realty_ohlc['open']
                nifty_realty_hg = res_nifty_realty_ohlc['high']
                nifty_realty_lw = res_nifty_realty_ohlc['low']
                nifty_realty_cl = res_nifty_realty_ohlc['close']
                nifty_realty_lt = res_nifty_realty_ohlc['ltp']
                nifty_realty_vlme = res_nifty_realty_ohlc['volume']
                nifty_realty_ak = res_nifty_realty_ohlc['ask']
                nifty_realty_bd = res_nifty_realty_ohlc['bid']
                # Nifty realty OHLC end

                # Nifty serv_sector OHLC start
                nifty_serv_sector_op = res_nifty_serv_sector_ohlc['open']
                nifty_serv_sector_hg = res_nifty_serv_sector_ohlc['high']
                nifty_serv_sector_lw = res_nifty_serv_sector_ohlc['low']
                nifty_serv_sector_cl = res_nifty_serv_sector_ohlc['close']
                nifty_serv_sector_lt = res_nifty_serv_sector_ohlc['ltp']
                nifty_serv_sector_vlme = res_nifty_serv_sector_ohlc['volume']
                nifty_serv_sector_ak = res_nifty_serv_sector_ohlc['ask']
                nifty_serv_sector_bd = res_nifty_serv_sector_ohlc['bid']
                # Nifty serv_sector OHLC end

                # Nifty smlcap_100 OHLC start
                nifty_smlcap_100_op = res_nifty_smlcap_100_ohlc['open']
                nifty_smlcap_100_hg = res_nifty_smlcap_100_ohlc['high']
                nifty_smlcap_100_lw = res_nifty_smlcap_100_ohlc['low']
                nifty_smlcap_100_cl = res_nifty_smlcap_100_ohlc['close']
                nifty_smlcap_100_lt = res_nifty_smlcap_100_ohlc['ltp']
                nifty_smlcap_100_vlme = res_nifty_smlcap_100_ohlc['volume']
                nifty_smlcap_100_ak = res_nifty_smlcap_100_ohlc['ask']
                nifty_smlcap_100_bd = res_nifty_smlcap_100_ohlc['bid']
                # Nifty smlcap_100 OHLC end

                # Nifty cpse OHLC start
                nifty_cpse_op = res_nifty_cpse_ohlc['open']
                nifty_cpse_hg = res_nifty_cpse_ohlc['high']
                nifty_cpse_lw = res_nifty_cpse_ohlc['low']
                nifty_cpse_cl = res_nifty_cpse_ohlc['close']
                nifty_cpse_lt = res_nifty_cpse_ohlc['ltp']
                nifty_cpse_vlme = res_nifty_cpse_ohlc['volume']
                nifty_cpse_ak = res_nifty_cpse_ohlc['ask']
                nifty_cpse_bd = res_nifty_cpse_ohlc['bid']
                # Nifty cpse OHLC end

                # Nifty india_vix OHLC start
                # nifty_india_vix_op = res_nse_ohlc['open']
                # nifty_india_vix_hg = res_nse_ohlc['high']
                # nifty_india_vix_lw = res_nse_ohlc['low']
                # nifty_india_vix_cl = res_nse_ohlc['close']
                # nifty_india_vix_lt = res_nse_ohlc['ltp']
                # nifty_india_vix_vlme = res_nse_ohlc['volume']
                # nifty_india_vix_ak = res_nse_ohlc['ask']
                # nifty_india_vix_bd = res_nse_ohlc['bid']
                # Nifty india_vix OHLC end

                # Nifty liq_15 OHLC start
                nifty_liq_15_op = res_nifty_liq_15_ohlc['open']
                nifty_liq_15_hg = res_nifty_liq_15_ohlc['high']
                nifty_liq_15_lw = res_nifty_liq_15_ohlc['low']
                nifty_liq_15_cl = res_nifty_liq_15_ohlc['close']
                nifty_liq_15_lt = res_nifty_liq_15_ohlc['ltp']
                nifty_liq_15_vlme = res_nifty_liq_15_ohlc['volume']
                nifty_liq_15_ak = res_nifty_liq_15_ohlc['ask']
                nifty_liq_15_bd = res_nifty_liq_15_ohlc['bid']
                # Nifty liq_15 OHLC end

                # Nifty growsect_15 OHLC start
                nifty_growsect_15_op = res_nifty_growsect_15_ohlc['open']
                nifty_growsect_15_hg = res_nifty_growsect_15_ohlc['high']
                nifty_growsect_15_lw = res_nifty_growsect_15_ohlc['low']
                nifty_growsect_15_cl = res_nifty_growsect_15_ohlc['close']
                nifty_growsect_15_lt = res_nifty_growsect_15_ohlc['ltp']
                nifty_growsect_15_vlme = res_nifty_growsect_15_ohlc['volume']
                nifty_growsect_15_ak = res_nifty_growsect_15_ohlc['ask']
                nifty_growsect_15_bd = res_nifty_growsect_15_ohlc['bid']
                # Nifty growsect_15 OHLC end

                # Nifty midcap_50 OHLC start
                nifty_midcap_50_op = res_nifty_midcap_50_ohlc['open']
                nifty_midcap_50_hg = res_nifty_midcap_50_ohlc['high']
                nifty_midcap_50_lw = res_nifty_midcap_50_ohlc['low']
                nifty_midcap_50_cl = res_nifty_midcap_50_ohlc['close']
                nifty_midcap_50_lt = res_nifty_midcap_50_ohlc['ltp']
                nifty_midcap_50_vlme = res_nifty_midcap_50_ohlc['volume']
                nifty_midcap_50_ak = res_nifty_midcap_50_ohlc['ask']
                nifty_midcap_50_bd = res_nifty_midcap_50_ohlc['bid']
                # Nifty midcap_50 OHLC end

                # Nifty mid_select OHLC start
                nifty_mid_select_op = res_nifty_mid_select_ohlc['open']
                nifty_mid_select_hg = res_nifty_mid_select_ohlc['high']
                nifty_mid_select_lw = res_nifty_mid_select_ohlc['low']
                nifty_mid_select_cl = res_nifty_mid_select_ohlc['close']
                nifty_mid_select_lt = res_nifty_mid_select_ohlc['ltp']
                nifty_mid_select_vlme = res_nifty_mid_select_ohlc['volume']
                nifty_mid_select_ak = res_nifty_mid_select_ohlc['ask']
                nifty_mid_select_bd = res_nifty_mid_select_ohlc['bid']
                # Nifty mid_select OHLC end

                for dt in response_data:
                    if dt["exchangename"] == "NSE":
                        INDEX = dt["exchangename"]

                    #Indexcode
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

                    # Indexname
                    if dt["indexname"] == "Nifty 50":
                        NIFTY_FIFTY = dt["indexname"]
                    if dt["indexname"] == "Nifty 100":
                        NIFTY_hundred = dt["indexname"]
                    if dt["indexname"] == "Nifty 200":
                        NIFTY_twohundred = dt["indexname"]
                    if dt["indexname"] == "Nifty Bank":
                        NIFTY_bank = dt["indexname"]
                    if dt["indexname"] == "Nifty Auto":
                        NIFTY_auto = dt["indexname"]
                    if dt["indexname"] == "Nifty FMCG":
                        NIFTY_fmcg = dt["indexname"]
                    if dt["indexname"] == "Nifty Pharma":
                        NIFTY_pharma = dt["indexname"]
                    if dt["indexname"] == "Nifty 500":
                        NIFTY_500 = dt["indexname"]
                    if dt["indexname"] == "Nifty Commodities":
                        NIFTY_COMMODITIES = dt["indexname"]
                    if dt["indexname"] == "Nifty Consumption":
                        NIFTY_CONSUMPTION = dt["indexname"]
                    if dt["indexname"] == "Nifty Div Opps 50":
                        NIFTY_DIV_OPPS_50 = dt["indexname"]
                    if dt["indexname"] == "Nifty Energy":
                        NIFTY_ENERGY = dt["indexname"]
                    if dt["indexname"] == "Nifty FIN SERVICE":
                        NIFTY_FIN_SERVICE = dt["indexname"]
                    if dt["indexname"] == "Nifty Infra":
                        NIFTY_INFRA = dt["indexname"]
                    if dt["indexname"] == "Nifty IT":
                        NIFTY_IT = dt["indexname"]
                    if dt["indexname"] == "Nifty Media":
                        NIFTY_MEDIA = dt["indexname"]
                    if dt["indexname"] == "Nifty Metal":
                        NIFTY_METAL = dt["indexname"]
                    if dt["indexname"] == "Nifty MIDCAP 100":
                        NIFTY_MIDCAP_100 = dt["indexname"]
                    if dt["indexname"] == "Nifty MNC":
                        NIFTY_MNC = dt["indexname"]
                    if dt["indexname"] == "Nifty Next 50":
                        NIFTY_NEXT_50 = dt["indexname"]
                    if dt["indexname"] == "Nifty PSE":
                        NIFTY_PSE = dt["indexname"]
                    if dt["indexname"] == "Nifty PSU Bank":
                        NIFTY_PSU_BANK = dt["indexname"]
                    if dt["indexname"] == "Nifty Realty":
                        NIFTY_REALITY = dt["indexname"]
                    if dt["indexname"] == "Nifty Serv Sector":
                        NIFTY_SERV_SECTOR = dt["indexname"]
                    if dt["indexname"] == "Nifty SMLCAP 100":
                        NIFTY_SMALLCAP_100 = dt["indexname"]
                    if dt["indexname"] == "Nifty CPSE":
                        NIFTY_CPSE = dt["indexname"]
                    if dt["indexname"] == "India VIX":
                        INDIA_VIX = dt["indexname"]
                    if dt["indexname"] == "Nifty100 Liq 15":
                        NIFTY100_LIQ_15 = dt["indexname"]
                    if dt["indexname"] == "Nifty GrowSect 15":
                        NIFTY_GROWSECT_15 = dt["indexname"]
                    if dt["indexname"] == "Nifty Midcap 50":
                        NIFTY_MIDCAP_50 = dt["indexname"]
                    if dt["indexname"] == "Nifty MID SELECT":
                        NIFTY_MID_SELECT = dt["indexname"]
                    
                context_indexname = {
                    "nifty50" : NIFTY_FIFTY,
                    "nifty100": NIFTY_hundred,
                    "nifty200": NIFTY_twohundred,
                    "niftybank": NIFTY_bank,
                    "niftyauto":NIFTY_auto,
                    "niftyfmcg": NIFTY_fmcg,
                    "niftypharma":NIFTY_pharma,
                    "nifty_mid_select": NIFTY_MID_SELECT,
                    "nifty_midcap_50": NIFTY_MIDCAP_50,
                    "nifty_growsect_15": NIFTY_GROWSECT_15,
                    "nifty_liq_15": NIFTY100_LIQ_15,
                    "india_vix": INDIA_VIX,
                    "nifty_cpse":NIFTY_CPSE,
                    "nifty_smallcap_100":NIFTY_SMALLCAP_100,
                    "nifty_serv_sector":NIFTY_SERV_SECTOR,
                    "nifty_realty": NIFTY_REALITY,
                    "nifty_psu_bank":NIFTY_PSU_BANK,
                    "nifty_pse": NIFTY_PSE,
                    "nifty_next_50": NIFTY_NEXT_50,
                    "nifty_mnc": NIFTY_MNC,
                    "nifty_metal": NIFTY_METAL,
                    "nifty_midcap_100":NIFTY_MIDCAP_100,
                    "nifty_media": NIFTY_MEDIA,
                    "nifty_it": NIFTY_IT,
                    "nifty_infra": NIFTY_INFRA,
                    "nifty_fin_service":NIFTY_FIN_SERVICE,
                    "nifty_energy": NIFTY_ENERGY,
                    "nifty_div_opps_50": NIFTY_DIV_OPPS_50,
                    "nifty_consumption": NIFTY_CONSUMPTION,
                    "nifty_commodities": NIFTY_COMMODITIES,
                    "nifty_500": NIFTY_500
                    }

                context_indexcode = {
                    "nifty_nse": INDEX,
                    "nifty50" : NIFTY_FIFTY,
                    "nifty100": NIFTY_hundred,
                    "nifty200": NIFTY_twohundred,
                    "niftybank": NIFTY_bank,
                    "niftyauto":NIFTY_auto,
                    "niftyfmcg": NIFTY_fmcg,
                    "niftypharma":NIFTY_pharma,
                    "nifty_mid_select": NIFTY_MID_SELECT,
                    "nifty_midcap_50": NIFTY_MIDCAP_50,
                    "nifty_growsect_15": NIFTY_GROWSECT_15,
                    "nifty_liq_15": NIFTY100_LIQ_15,
                    "india_vix": INDIA_VIX,
                    "nifty_cpse":NIFTY_CPSE,
                    "nifty_smallcap_100":NIFTY_SMALLCAP_100,
                    "nifty_serv_sector":NIFTY_SERV_SECTOR,
                    "nifty_realty": NIFTY_REALITY,
                    "nifty_psu_bank":NIFTY_PSU_BANK,
                    "nifty_pse": NIFTY_PSE,
                    "nifty_next_50": NIFTY_NEXT_50,
                    "nifty_mnc": NIFTY_MNC,
                    "nifty_metal": NIFTY_METAL,
                    "nifty_midcap_100":NIFTY_MIDCAP_100,
                    "nifty_media": NIFTY_MEDIA,
                    "nifty_it": NIFTY_IT,
                    "nifty_infra": NIFTY_IT,
                    "nifty_fin_service":NIFTY_FIN_SERVICE,
                    "nifty_energy": NIFTY_ENERGY,
                    "nifty_div_opps_50": NIFTY_DIV_OPPS_50,
                    "nifty_consumption": NIFTY_CONSUMPTION,
                    "nifty_commodities": NIFTY_COMMODITIES,
                    "nifty_500": NIFTY_500
                    }
                
                context_nse_ohlc = {
                    # Nifty bank OHCL start
                    "nifty_bank_open": nifty_bank_op,
                    "nifty_bank_high": nifty_bank_hg,
                    "nifty_bank_low": nifty_bank_lw,
                    "nifty_bank_close": nifty_bank_cl,
                    "nifty_bank_ltp": nifty_bank_lt,
                    "nifty_bank_volume": nifty_bank_vlme,
                    "nifty_bank_ask": nifty_bank_ak,
                    "nifty_bank_bid": nifty_bank_bd,
                    # Nifty bank OHCL end

                    # Nifty 100 OHCL start
                    "nifty_100_open": nifty_100_op,
                    "nifty_100_high": nifty_100_hg,
                    "nifty_100_low": nifty_100_lw,
                    "nifty_100_close": nifty_100_cl,
                    "nifty_100_ltp": nifty_100_lt,
                    "nifty_100_volume": nifty_100_vlme,
                    "nifty_100_ask": nifty_100_ak,
                    "nifty_100_bid": nifty_100_bd,
                    # Nifty 100 OHCL end

                    # Nifty 200 OHCL start
                    "nifty_200_open": nifty_200_op,
                    "nifty_200_high": nifty_200_hg,
                    "nifty_200_low": nifty_200_lw,
                    "nifty_200_close": nifty_200_cl,
                    "nifty_200_ltp": nifty_200_lt,
                    "nifty_200_volume": nifty_200_vlme,
                    "nifty_200_ask": nifty_200_ak,
                    "nifty_200_bid": nifty_200_bd,
                    # Nifty 200 OHCL end

                    # Nifty 500 OHCL start
                    "nifty_500_open": nifty_500_op,
                    "nifty_500_high": nifty_500_hg,
                    "nifty_500_low": nifty_500_lw,
                    "nifty_500_close": nifty_500_cl,
                    "nifty_500_ltp": nifty_500_lt,
                    "nifty_500_volume": nifty_500_vlme,
                    "nifty_500_ask": nifty_500_ak,
                    "nifty_500_bid": nifty_500_bd,
                    # Nifty 500 OHCL end

                    # Nifty auto OHCL start
                    "nifty_auto_open": nifty_auto_op,
                    "nifty_auto_high": nifty_auto_hg,
                    "nifty_auto_low": nifty_auto_lw,
                    "nifty_auto_close": nifty_auto_cl,
                    "nifty_auto_ltp": nifty_auto_lt,
                    "nifty_auto_volume": nifty_auto_vlme,
                    "nifty_auto_ask": nifty_auto_ak,
                    "nifty_auto_bid": nifty_auto_bd,
                    # Nifty auto OHCL end

                    # Nifty commodities OHCL start
                    "nifty_commodities_open": nifty_commodities_op,
                    "nifty_commodities_high": nifty_commodities_hg,
                    "nifty_commodities_low": nifty_commodities_lw,
                    "nifty_commodities_close": nifty_commodities_cl,
                    "nifty_commodities_ltp": nifty_commodities_lt,
                    "nifty_commodities_volume": nifty_commodities_vlme,
                    "nifty_commodities_ask": nifty_commodities_ak,
                    "nifty_commodities_bid": nifty_commodities_bd,
                    # Nifty commodities OHCL end

                    # Nifty consumption OHCL start
                    "nifty_consumption_open": nifty_consumption_op,
                    "nifty_consumption_high": nifty_consumption_hg,
                    "nifty_consumption_low": nifty_consumption_lw,
                    "nifty_consumption_close": nifty_consumption_cl,
                    "nifty_consumption_ltp": nifty_consumption_lt,
                    "nifty_consumption_volume": nifty_consumption_vlme,
                    "nifty_consumption_ask": nifty_consumption_ak,
                    "nifty_consumption_bid": nifty_consumption_bd,
                    # Nifty consumption OHCL end

                    # Nifty div_opps_50 OHCL start
                    "nifty_div_opps_50_open": nifty_div_opps_50_op,
                    "nifty_div_opps_50_high": nifty_div_opps_50_hg,
                    "nifty_div_opps_50_low": nifty_div_opps_50_lw,
                    "nifty_div_opps_50_close": nifty_div_opps_50_cl,
                    "nifty_div_opps_50_ltp": nifty_div_opps_50_lt,
                    "nifty_div_opps_50_volume": nifty_div_opps_50_vlme,
                    "nifty_div_opps_50_ask": nifty_div_opps_50_ak,
                    "nifty_div_opps_50_bid": nifty_div_opps_50_bd,
                    # Nifty div_opps_50 OHCL end

                    # Nifty energy OHCL start
                    "nifty_energy_open": nifty_energy_op,
                    "nifty_energy_high": nifty_energy_hg,
                    "nifty_energy_low": nifty_energy_lw,
                    "nifty_energy_close": nifty_energy_cl,
                    "nifty_energy_ltp": nifty_energy_lt,
                    "nifty_energy_volume": nifty_energy_vlme,
                    "nifty_energy_ask": nifty_energy_ak,
                    "nifty_energy_bid": nifty_energy_bd,
                    # Nifty energy OHCL end

                    # Nifty fin_service OHCL start
                    "nifty_fin_service_open": nifty_fin_service_op,
                    "nifty_fin_service_high": nifty_fin_service_hg,
                    "nifty_fin_service_low": nifty_fin_service_lw,
                    "nifty_fin_service_close": nifty_fin_service_cl,
                    "nifty_fin_service_ltp": nifty_fin_service_lt,
                    "nifty_fin_service_volume": nifty_fin_service_vlme,
                    "nifty_fin_service_ask": nifty_fin_service_ak,
                    "nifty_fin_service_bid": nifty_fin_service_bd,
                    # Nifty fin_service OHCL end

                    # Nifty fmcg OHCL start
                    "nifty_fmcg_open": nifty_fmcg_op,
                    "nifty_fmcg_high": nifty_fmcg_hg,
                    "nifty_fmcg_low": nifty_fmcg_lw,
                    "nifty_fmcg_close": nifty_fmcg_cl,
                    "nifty_fmcg_ltp": nifty_fmcg_lt,
                    "nifty_fmcg_volume": nifty_fmcg_vlme,
                    "nifty_fmcg_ask": nifty_fmcg_ak,
                    "nifty_fmcg_bid": nifty_fmcg_bd,
                    # Nifty fmcg OHCL end

                    # Nifty infra OHCL start
                    "nifty_infra_open": nifty_infra_op,
                    "nifty_infra_high": nifty_infra_hg,
                    "nifty_infra_low": nifty_infra_lw,
                    "nifty_infra_close": nifty_infra_cl,
                    "nifty_infra_ltp": nifty_infra_lt,
                    "nifty_infra_volume": nifty_infra_vlme,
                    "nifty_infra_ask": nifty_infra_ak,
                    "nifty_infra_bid": nifty_infra_bd,
                    # Nifty infra OHCL end

                    # Nifty it OHCL start
                    "nifty_it_open": nifty_it_op,
                    "nifty_it_high": nifty_it_hg,
                    "nifty_it_low": nifty_it_lw,
                    "nifty_it_close": nifty_it_cl,
                    "nifty_it_ltp": nifty_it_lt,
                    "nifty_it_volume": nifty_it_vlme,
                    "nifty_it_ask": nifty_it_ak,
                    "nifty_it_bid": nifty_it_bd,
                    # Nifty it OHCL end

                    # Nifty media OHCL start
                    "nifty_media_open": nifty_media_op,
                    "nifty_media_high": nifty_media_hg,
                    "nifty_media_low": nifty_media_lw,
                    "nifty_media_close": nifty_media_cl,
                    "nifty_media_ltp": nifty_media_lt,
                    "nifty_media_volume": nifty_media_vlme,
                    "nifty_media_ask": nifty_media_ak,
                    "nifty_media_bid": nifty_media_bd,
                    # Nifty media OHCL end

                    # Nifty metal OHCL start
                    "nifty_metal_open": nifty_metal_op,
                    "nifty_metal_high": nifty_metal_hg,
                    "nifty_metal_low": nifty_metal_lw,
                    "nifty_metal_close": nifty_metal_cl,
                    "nifty_metal_ltp": nifty_metal_lt,
                    "nifty_metal_volume": nifty_metal_vlme,
                    "nifty_metal_ask": nifty_metal_ak,
                    "nifty_metal_bid": nifty_metal_bd,
                    # Nifty metal OHCL end

                    # Nifty midcap_100 OHCL start
                    "nifty_midcap_100_open": nifty_midcap_100_op,
                    "nifty_midcap_100_high": nifty_midcap_100_hg,
                    "nifty_midcap_100_low": nifty_midcap_100_lw,
                    "nifty_midcap_100_close": nifty_midcap_100_cl,
                    "nifty_midcap_100_ltp": nifty_midcap_100_lt,
                    "nifty_midcap_100_volume": nifty_midcap_100_vlme,
                    "nifty_midcap_100_ask": nifty_midcap_100_ak,
                    "nifty_midcap_100_bid": nifty_midcap_100_bd,
                    # Nifty midcap_100 OHCL end

                    # Nifty mnc OHCL start
                    "nifty_mnc_open": nifty_mnc_op,
                    "nifty_mnc_high": nifty_mnc_hg,
                    "nifty_mnc_low": nifty_mnc_lw,
                    "nifty_mnc_close": nifty_mnc_cl,
                    "nifty_mnc_ltp": nifty_mnc_lt,
                    "nifty_mnc_volume": nifty_mnc_vlme,
                    "nifty_mnc_ask": nifty_mnc_ak,
                    "nifty_mnc_bid": nifty_mnc_bd,
                    # Nifty mnc OHCL end

                    # Nifty 50 OHCL start
                    "nifty_50_open": nifty_50_op,
                    "nifty_50_high": nifty_50_hg,
                    "nifty_50_low": nifty_50_lw,
                    "nifty_50_close": nifty_50_cl,
                    "nifty_50_ltp": nifty_50_lt,
                    "nifty_50_volume": nifty_50_vlme,
                    "nifty_50_ask": nifty_50_ak,
                    "nifty_50_bid": nifty_50_bd,
                    # Nifty 50 OHCL end

                    # Nifty next_50 OHCL start
                    "nifty_next_50_open": nifty_next_50_op,
                    "nifty_next_50_high": nifty_next_50_hg,
                    "nifty_next_50_low": nifty_next_50_lw,
                    "nifty_next_50_close": nifty_next_50_cl,
                    "nifty_next_50_ltp": nifty_next_50_lt,
                    "nifty_next_50_volume": nifty_next_50_vlme,
                    "nifty_next_50_ask": nifty_next_50_ak,
                    "nifty_next_50_bid": nifty_next_50_bd,
                    # Nifty next_50 OHCL end

                    # Nifty pharma OHCL start
                    "nifty_pharma_open": nifty_pharma_op,
                    "nifty_pharma_high": nifty_pharma_hg,
                    "nifty_pharma_low": nifty_pharma_lw,
                    "nifty_pharma_close": nifty_pharma_cl,
                    "nifty_pharma_ltp": nifty_pharma_lt,
                    "nifty_pharma_volume": nifty_pharma_vlme,
                    "nifty_pharma_ask": nifty_pharma_ak,
                    "nifty_pharma_bid": nifty_pharma_bd,
                    # Nifty pharma OHCL end

                    # Nifty pse OHCL start
                    "nifty_pse_open": nifty_pse_op,
                    "nifty_pse_high": nifty_pse_hg,
                    "nifty_pse_low": nifty_pse_lw,
                    "nifty_pse_close": nifty_pse_cl,
                    "nifty_pse_ltp": nifty_pse_lt,
                    "nifty_pse_volume": nifty_pse_vlme,
                    "nifty_pse_ask": nifty_pse_ak,
                    "nifty_pse_bid": nifty_pse_bd,
                    # Nifty pse OHCL end

                    # Nifty psu_bank OHCL start
                    "nifty_psu_bank_open": nifty_psu_bank_op,
                    "nifty_psu_bank_high": nifty_psu_bank_hg,
                    "nifty_psu_bank_low": nifty_psu_bank_lw,
                    "nifty_psu_bank_close": nifty_psu_bank_cl,
                    "nifty_psu_bank_ltp": nifty_psu_bank_lt,
                    "nifty_psu_bank_volume": nifty_psu_bank_vlme,
                    "nifty_psu_bank_ask": nifty_psu_bank_ak,
                    "nifty_psu_bank_bid": nifty_psu_bank_bd,
                    # Nifty psu_bank OHCL end

                    # Nifty realty OHCL start
                    "nifty_realty_open": nifty_realty_op,
                    "nifty_realty_high": nifty_realty_hg,
                    "nifty_realty_low": nifty_realty_lw,
                    "nifty_realty_close": nifty_realty_cl,
                    "nifty_realty_ltp": nifty_realty_lt,
                    "nifty_realty_volume": nifty_realty_vlme,
                    "nifty_realty_ask": nifty_realty_ak,
                    "nifty_realty_bid": nifty_realty_bd,
                    # Nifty realty OHCL end

                    # Nifty serv_sector OHCL start
                    "nifty_serv_sector_open": nifty_serv_sector_op,
                    "nifty_serv_sector_high": nifty_serv_sector_hg,
                    "nifty_serv_sector_low": nifty_serv_sector_lw,
                    "nifty_serv_sector_close": nifty_serv_sector_cl,
                    "nifty_serv_sector_ltp": nifty_serv_sector_lt,
                    "nifty_serv_sector_volume": nifty_serv_sector_vlme,
                    "nifty_serv_sector_ask": nifty_serv_sector_ak,
                    "nifty_serv_sector_bid": nifty_serv_sector_bd,
                    # Nifty serv_sector OHCL end

                    # Nifty smlcap_100 OHCL start
                    "nifty_smlcap_100_open": nifty_smlcap_100_op,
                    "nifty_smlcap_100_high": nifty_smlcap_100_hg,
                    "nifty_smlcap_100_low": nifty_smlcap_100_lw,
                    "nifty_smlcap_100_close": nifty_smlcap_100_cl,
                    "nifty_smlcap_100_ltp": nifty_smlcap_100_lt,
                    "nifty_smlcap_100_volume": nifty_smlcap_100_vlme,
                    "nifty_smlcap_100_ask": nifty_smlcap_100_ak,
                    "nifty_smlcap_100_bid": nifty_smlcap_100_bd,
                    # Nifty smlcap_100 OHCL end

                    # Nifty cpse OHCL start
                    "nifty_cpse_open": nifty_cpse_op,
                    "nifty_cpse_high": nifty_cpse_hg,
                    "nifty_cpse_low": nifty_cpse_lw,
                    "nifty_cpse_close": nifty_cpse_cl,
                    "nifty_cpse_ltp": nifty_cpse_lt,
                    "nifty_cpse_volume": nifty_cpse_vlme,
                    "nifty_cpse_ask": nifty_cpse_ak,
                    "nifty_cpse_bid": nifty_cpse_bd,
                    # Nifty cpse OHCL end

                    # Nifty liq_15 OHCL start
                    "nifty_liq_15_open": nifty_liq_15_op,
                    "nifty_liq_15_high": nifty_liq_15_hg,
                    "nifty_liq_15_low": nifty_liq_15_lw,
                    "nifty_liq_15_close": nifty_liq_15_cl,
                    "nifty_liq_15_ltp": nifty_liq_15_lt,
                    "nifty_liq_15_volume": nifty_liq_15_vlme,
                    "nifty_liq_15_ask": nifty_liq_15_ak,
                    "nifty_liq_15_bid": nifty_liq_15_bd,
                    # Nifty liq_15 OHCL end

                    # Nifty growsect_15 OHCL start
                    "nifty_growsect_15_open": nifty_growsect_15_op,
                    "nifty_growsect_15_high": nifty_growsect_15_hg,
                    "nifty_growsect_15_low": nifty_growsect_15_lw,
                    "nifty_growsect_15_close": nifty_growsect_15_cl,
                    "nifty_growsect_15_ltp": nifty_growsect_15_lt,
                    "nifty_growsect_15_volume": nifty_growsect_15_vlme,
                    "nifty_growsect_15_ask": nifty_growsect_15_ak,
                    "nifty_growsect_15_bid": nifty_growsect_15_bd,
                    # Nifty growsect_15 OHCL end

                    # Nifty midcap_50 OHCL start
                    "nifty_midcap_50_open": nifty_midcap_50_op,
                    "nifty_midcap_50_high": nifty_midcap_50_hg,
                    "nifty_midcap_50_low": nifty_midcap_50_lw,
                    "nifty_midcap_50_close": nifty_midcap_50_cl,
                    "nifty_midcap_50_ltp": nifty_midcap_50_lt,
                    "nifty_midcap_50_volume": nifty_midcap_50_vlme,
                    "nifty_midcap_50_ask": nifty_midcap_50_ak,
                    "nifty_midcap_50_bid": nifty_midcap_50_bd,
                    # Nifty midcap_50 OHCL end

                    # Nifty mid_select OHCL start
                    "nifty_mid_select_open": nifty_mid_select_op,
                    "nifty_mid_select_high": nifty_mid_select_hg,
                    "nifty_mid_select_low": nifty_mid_select_lw,
                    "nifty_mid_select_close": nifty_mid_select_cl,
                    "nifty_mid_select_ltp": nifty_mid_select_lt,
                    "nifty_mid_select_volume": nifty_mid_select_vlme,
                    "nifty_mid_select_ask": nifty_mid_select_ak,
                    "nifty_mid_select_bid": nifty_mid_select_bd,
                    # Nifty mid_select OHCL end
                    
                    

                }
                                    
                return render(request, 'market_dashboard/template/all_indices.html', {"ind_code": context_indexcode, "ind_name":context_indexname, "nse_ohlc":context_nse_ohlc})
            except json.JSONDecodeError as e:
      
                print(f"JSONDecodeError: {e}")
                print("Response Content:", response_data.content.decode())

            return HttpResponseServerError("Error decoding JSON response.")
        else:
            # If the request was not successful, handle the error
            error_message = f"Error: {response_data.status_code} - {response_data.text}"
            print(error_message)
            # You might want to handle the error in a way that makes sense for your application
            return render(request, 'market_dashboard/template/404.html', {"error_message": error_message})
    
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": "An error occurred: "})