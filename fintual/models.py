from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField()
    date = models.DateField()
    
    def get_price(stock_date): 
        stock = Stock.objects.get(date=stock_date)
        return stock.price

class Portfolio(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stocks = models.ManyToManyField(Stock)    