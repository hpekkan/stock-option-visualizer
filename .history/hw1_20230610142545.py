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

    # Check for option arbitrage opportunity
    for i in range(1, 100):
        if option_y[i] != option_y[i-1]:
            if option_y[i] > option_y[i-1]:
                print("Option arbitrage opportunity: Buy at option price",i-1, option_x[i-1], "and sell at spot price", option_x[i])
            else:
                print("Option arbitrage opportunity: Sell at option price",i-1, option_x[i-1], "and buy at spot price", option_x[i])

    # Check for stock arbitrage opportunity
    max_profit = max(option_y)
    min_profit = min(option_y)
    if max_profit != min_profit:
        max_index = np.argmax(option_y)
        min_index = np.argmin(option_y)
        if max_profit > min_profit:
            print("Stock arbitrage opportunity: Buy at option price",min_index, option_x[min_index], "and sell at spot price", option_x[max_index])
        else:
            print("Stock arbitrage opportunity: Sell at option price",min_index, option_x[min_index], "and buy at spot price", option_x[max_index])

    plt.plot(option_x,option_y)
    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)
    plt.xlabel("Spot Fiyatı")
    plt.ylabel("Kar/Zarar")
    plt.show()
         
    


if __name__ == '__main__':
    main()  