import pandas as pd
from datetime import date
class Business():
    
    def __init__(self) :
        return self

    class PortfolioBusiness():
        def calculate_profit(stocks, start_date,end_date):
            
            if len(stocks) == 0:
                return "error"
            
            if len(stocks) == 1:
                return stocks[0].price

            df_stock = pd.DataFrame(stocks)
            calculated_stock = df_stock.iloc[:len(stocks)-1]
            #obtener el ultimo valor del periodo consultado
            last_stock = df_stock.iloc[-1]
            #calcular el valor por la cantidad de acciones por el precio de la accion
            actual_price = last_stock['price'] * len(stocks)
            #calcular el valor de las acciones en el periodo consultado
            accumulated_price = calculated_stock['price'].sum()

            return actual_price - accumulated_price

        def calculate_annualy_return(stocks, start_date,end_date):
            if len(stocks) == 0:
                return "error"
            
            if len(stocks) == 1:
                return stocks[0].price

            df_stock = pd.DataFrame(stocks)

            calculated_stock = df_stock.iloc[:len(stocks)-1]
            last_stock = df_stock.iloc[-1]
            
            #calculate total of years
            start_date = min(df_stock['date'])
            end_date = min(df_stock['date'])
            total_years = end_date - start_date
            # if total_years == 0 and len(stocks) >= 1:
            #     total_years = 1
            if total_years.days == 0 and len(stocks) >= 1:   
                total_years = 1

            #calculate the annnualy return  of the stocks  
            annualy_return = (pow((last_stock['price'] / calculated_stock.iloc[0]['price']),(1/total_years))-1)*100
            return annualy_return
