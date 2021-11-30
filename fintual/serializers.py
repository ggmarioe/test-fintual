from rest_framework import serializers
from fintual.models import Portfolio, Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['name', 'price', 'date']

   

class PortfolioSerializer(serializers.ModelSerializer):
    '''
    Retornar la ganancia y si es posible 
    el retorno anual(?) annualized return
    '''
    class Meta:
        model = Portfolio
        fields = '__all__' #['name', 'description', 'stocks']
    