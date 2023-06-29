import numpy as np
from matplotlib import pyplot as plt

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
    option_quantity = int(input("Kaç opsiyon kullanacaksınız: "))
    stock_quantity = int(input("Kaç hisse senedi kullanacaksınız: "))
    spot_price = int(input("Hisse senedi Spot Fiyatı: "))
    stock_info = input("Hisse senedi bilgileri\n Alım/Satım: ")
    options=[]
    option_data=[]
    option_x = np.linspace(0,2*spot_price,100)
    counter = 1
    while counter<=option_quantity:
        print("Opsiyon",counter,"Bilgileri")
        option_type = input("Tipi: ")
        option_info = input("Alım/Satım: ")
        strike_price = int(input("Strike Fiyatı: "))
        option_price = int(input("Opsiyon Fiyatı: "))
        option_data.append({"option_type":option_type,"option_info":option_info,"strike_price":strike_price,"option_price":option_price})
        
        counter = counter + 1
    print("Opsiyonlar: ",options)
    profit = np.sum(options)
    


if __name__ == '__main__':
    main()  