from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
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
# Create your views here.
# import matplotlib.pyplot as plt
from io import BytesIO

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
    password = "abcd"
    apiKey = "abc"
    authtoken = "d3bcc86824264c689bf18052bb724fa5_M"

    # Define the URL for the production environment
    url = f"https://invest.motilaloswal.com/OpenAPI/Login.aspx?apikey={apikey}"

    # Calculate the SHA-256 hash of the password and apiKey
    combined_string = password + apiKey
    hash_object = hashlib.sha256(combined_string.encode())
    hashed_password = hash_object.hexdigest()

    # Prepare the request data
    request_data = {
        "userid": "AA017",
        "password": hashed_password,
        "2FA": "18/10/1988",
        "totp": "Authenticator 6 digit Code"
    }
    print(request_data)
   
   # Send a GET request with the request data as parameters
    try:
        response = requests.get(url, params=request_data, headers={'authtoken': authtoken})

        if response.status_code == 200:
            # Successful response
            data = response.json()  # If the response is in JSON format
            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
    
    return JsonResponse({"message": "Login request sent."})


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
        response = requests.get(url, params=order_data_placed, headers=headers)

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



def mosl_place_odr(request):
    url = "https://uatopenapi.motilaloswal.com/rest/trans/v1/placeorder"

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
        # "User-Agent": "frenchise/1.0",
    }

    print(order_data_placed)

    # Send a POST request with JSON data
    try:
        response = requests.post(url, order_data_placed,headers)
        response_load = json.loads(response.content)
        print(response_load)

        # if response_load.status_code == 200:
        #     # Successful response
        #     print(response_load)
        # else:
        #     print(f"Request failed with status code: {response_load.status_code}")
        #     print(response_load)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
        response_load = {"error": str(e)}
    
    return render(request, 'market/mosl_index.html', {'response_load': response_load})


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
    return render(request, 'market/mosl_index.html')

def nifty_chart(request):
    return render(request, 'market/chart.html')


def get_stock_data(symbol):
    # Make a request to Motilal Oswal API
    # Handle authentication and other necessary details
    response = requests.get(f'https://api.motilaloswal.com/stocks/{symbol}/')

    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def stock_chart(request, symbol):
    stock_data = get_stock_data(symbol)
    return render(request, 'stock_chart.html', {'stock_data': stock_data})


























































