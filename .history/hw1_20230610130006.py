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
def stock_profit(spot,current_price, stock_info):
    if stock_info.casefold() == "alım".casefold():
        return spot - current_price
    else:
        return current_price - spot

def main():
    option_quantity = int(input("Kaç opsiyon kullanacaksınız: "))
    stock_quantity = int(input("Kaç hisse senedi kullanacaksınız: "))
    spot_price = int(input("Hisse senedi Spot Fiyatı: "))
    stock_info = input("Hisse senedi bilgileri\n Alım/Satım: ")
    options=[]
    option_data=[]
    option_x = np.linspace(0,2*spot_price,100)
    option_y = np.zeros(100)
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
    for i in range(100):
        profit = 0
        for option in option_data:
            if option["option_type"].casefold() == "put".casefold():
                if option["option_info"].casefold() == "alım".casefold():
                    profit = profit + long_put(option["strike_price"],option_x[i],option["option_price"])
                else:
                    profit = profit + short_put(option["strike_price"],option_x[i],option["option_price"])
            else:
                if option["option_info"].casefold() == "alım".casefold():
                    profit = profit + long_call(option["strike_price"],option_x[i],option["option_price"])
                else:
                    profit = profit + short_call(option["strike_price"],option_x[i],option["option_price"])
        profit = profit + stock_profit(spot_price,option_x[i],stock_info)*stock_quantity
        option_y[i] = profit
    plt.plot(option_x,option_y)
    plt.xlabel("Spot Fiyatı")
    plt.ylabel("Kar/Zarar")
    plt.show()
         
    


if __name__ == '__main__':
    main()  