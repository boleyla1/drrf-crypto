from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({"message": "Hello, world!"})


# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world mehrshad in get !"})

    def post(self, request):
        return Response({"message": "Hello, world mehrshad in post!"})


class GetBestPrice(APIView):
    def get(self, request):
        coin = request.GET.get('coin')
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}")
        data = response.json()
        result = {
            "symbol": data['symbol'],
            "price": data['price'],
        }
        return Response(data=result)
