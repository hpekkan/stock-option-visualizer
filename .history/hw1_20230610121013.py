import numpy as np

def buy_put(strike, spot, op_price):
   if strike > spot:
        return strike - spot - op_price
   else:
        return -op_price
def sell_put(strike, spot, op_price):
    if strike > spot:
          return op_price
    else:
          return spot - strike - op_price
def buy_call(strike, spot, op_price):
    if strike < spot:
          return spot - strike - op_price
    else:
          return -op_price
def sell_call(strike, spot, op_price):
    if strike < spot:
          return op_price
    else:
          return strike - spot - op_price

def main():
    option_quantity = input("Kaç opsiyon kullanacaksınız: ")
    stock_quantity = input("Kaç hisse senedi kullanacaksınız: ")
    spot_price = input("Hisse senedi Spot Fiyatı: ")
    
    


if __name__ == '__main__':
    main()  