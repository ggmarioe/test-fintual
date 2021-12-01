import pandas as pd

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
            last_stock = df_stock.iloc[-1]
            
            return calculated_stock['price'].mean() - last_stock['price'] 

        def calculate_annualy_return(stocks, start_date,end_date):
            if len(stocks) == 0:
                return "error"
            
            if len(stocks) == 1:
                return stocks[0].price

            df_stock = pd.DataFrame(stocks)
            calculated_stock = df_stock.iloc[:len(stocks)-1]
            last_stock = df_stock.iloc[-1]
            
            return (calculated_stock['price'].mean() - last_stock['price']) / last_stock['price']