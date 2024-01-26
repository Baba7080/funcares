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


def all_nse_bse_indices(request):

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
    print("callingdfghhhgff NSE_BSE_data func")

    try:
        response_nse = requests.post(url, json=data, headers=headers)
        print('response nse', response_nse)

        INDEX =""

        if response_nse.status_code == 200:
          
            try:
                json_data = response_nse.json()
                print("JSON response:", json_data)

                responce_data = json_data.get('data', [])
                print("data json form", responce_data)
                for dt in responce_data:
                    if dt["exchangename"] == "NSE":
                        INDEX = dt["exchangename"]
                        print("index data", INDEX)
                        return render(request, 'market_dashboard/template/all_indices.html', {"ind_data": INDEX})
            except json.JSONDecodeError as e:
      
                print(f"JSONDecodeError: {e}")
                print("Response Content:", responce_data.content.decode())

            return HttpResponseServerError("Error decoding JSON response.")
        else:
            # If the request was not successful, handle the error
            error_message = f"Error: {responce_data.status_code} - {responce_data.text}"
            print(error_message)
            # You might want to handle the error in a way that makes sense for your application
            return render(request, 'market_dashboard/template/error_page.html', {"error_message": error_message})
    
    except Exception as e:
        print("An error occurred:", e)
        return JsonResponse({"error": "An error occurred: " + str(e)})
