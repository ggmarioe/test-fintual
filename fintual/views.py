from django.http import response
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from fintual.serializers import StockSerializer, PortfolioSerializer
from fintual.models import Portfolio, Stock
from dateutil.relativedelta import relativedelta


from rest_framework.decorators import action
import json
import datetime
from fintual.business import *

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    @action(detail=False, methods=['get'])
    def profit(self, request):
        previous_month = datetime.datetime.now() - relativedelta(months=2)
        next_month = datetime.datetime.now() + relativedelta(months=1)

        # obtener los datos en el portafolio
        portfolio_stocks = Portfolio.objects.get(id = 1).stocks.all().values()
        
        result = Business.PortfolioBusiness.calculate_profit(stocks = portfolio_stocks, 
                                                            start_date = previous_month, 
                                                            end_date = next_month)
        
        #realizar el cálculo del profit
        return  Response(result)


