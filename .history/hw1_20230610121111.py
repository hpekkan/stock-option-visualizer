import numpy as np

def long_put(strike, spot, op_price):
   if strike > spot:
        return strike - spot - op_price
   else:
        return -op_price
def short_put(strike, spot, op_price):
    if strike > spot:
          return op_price
    else:
          return spot - strike - op_price
def long_call(strike, spot, op_price):
    if strike < spot:
          return spot - strike - op_price
    else:
          return -op_price
def short_call(strike, spot, op_price):
    if strike < spot:
          return op_price
    else:
          return strike - spot - op_price

def main():
    option_quantity = input("Kaç opsiyon kullanacaksınız: ")
    stock_quantity = input("Kaç hisse senedi kullanacaksınız: ")
    spot_price = input("Hisse senedi Spot Fiyatı: ")
    long_call_result = long_call(100, 105, 2.5)
    print("Long Call Sonucu: ", long_call_result)
    


if __name__ == '__main__':
    main()  