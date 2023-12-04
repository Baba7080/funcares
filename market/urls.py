from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('mosl-home/', scrape_website, name= 'mosl_home'),
    path('mofsllogin/',mofslloginfun,name='mofsllogin'),
    # MOSL - Pages Urls
    path('MOSL-index/', mosl_index, name= 'mosl_index'),
    path('MOSL-tradebook/', tradebook, name= 'tradebook'),
    path('MOSL-detailpage/<str:code>', getltpbycode, name= 'detailpage'),
    path('MOSL-NSE-BSE-alldata/', NSE_BSE_data, name= 'MOSL_NSE_BSE_alldata'),
#MOSL - Authentication
    path('MOSL-login/', mosl_login, name= 'mosl_login'),
    path('MOSL-logout/', mosl_logout, name= 'mosl_logout'),

# MOSL - Order
    # path('MOSL-order-placed/', mosl_place/_odr, name= 'placed_order'),
    path('MOSL-modify-order/', mosl_modify_order, name= 'Modify_order'),
    path('MOSL-cancel-order/', mosl_cancel_order, name= 'cancel_order'),
    path('MOSL-OrderBook/', mosl_order_book, name= 'orderbook'),
    path('MOSL-TradeBook/', mosl_trade_book, name= 'tradebook'),
    path('MOSL-OrderDetails/', mosl_orderdetails, name= 'orderdetails'),
    path('MOSL-TradeDetails/', mosl_tradedetails, name= 'tradedetails'),

# MOSL - Portfolio
    path('MOSL-Holdings/', mosl_holdings, name='holdings'),
    path('MOSL-Position/', mosl_position, name='position'),
    path('MOSL-PositionConversion/', mosl_position_conversion, name= 'position-conversion'),
    path('MOSL-PositionDetails/', mosl_position_details, name= 'position-details'),

# MOSL - Limit/Margin - Price/LTP
    path('MOSL-margin-summary/', mosl_margin_summary, name='margin_summary'),
    path('MOSL-margin-details/', mosl_margin_details, name='margin_details'),
    path('MOSL-price/', mosl_Price, name='Price'),

# MOSL - Master Data & DPR Data
    path('MOSL-scrips/', mosl_scrips, name='scrips'),
    # path('MOSL-margin-details/', mosl_margin_details, name='margin_details'),
    path('MOSL-DPR/', mosl_DPR, name='DPR'),
    # path('MOSL-margin-details/', mosl_margin_details, name='margin_details'),

# Charts
    path('MOSL-chart/', nifty_chart, name='chart'),
]