from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/asc/stockupdater/', consumers.StockConsumer.as_asgi()),
    path('ws/jwc/', consumers.ChartConsumer.as_asgi(), name='web_conn'),
]