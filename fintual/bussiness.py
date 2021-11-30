
class Bussiness():

    def calculate_profit(self, stocks, start_date_,end_date, stock_cost):

        profit = stocks.apply(lambda x: x.calculate_profit(start_date_,end_date, x.price))
        return (stock_price - stock_cost) * stock_quantity()
