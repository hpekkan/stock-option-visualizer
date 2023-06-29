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
    options = []
    option_data = []
    option_x = np.linspace(0, 2 * spot_price, 100)
    stock_profit_x = np.zeros(100)
    option_profits = np.zeros((option_quantity, 100))  # Modify to store separate option profits
    counter = 1
    while counter <= option_quantity:
        print("Opsiyon", counter, "Bilgileri")
        option_type = input("Tipi: ")
        option_info = input("Alım/Satım: ")
        strike_price = int(input("Strike Fiyatı: "))
        option_price = int(input("Opsiyon Fiyatı: "))
        option_data.append(
            {"option_type": option_type, "option_info": option_info, "strike_price": strike_price,
             "option_price": option_price})
        counter = counter + 1

    for i in range(100):
        stock_profit_val = 0
        for j, option in enumerate(option_data):  # Iterate over each option separately
            option_profit_val = 0
            if option["option_type"].casefold() == "put".casefold():
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_put(option["strike_price"], i, option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_put(option["strike_price"], i, option["option_price"]) * stock_quantity
            else:
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_call(option["strike_price"], i, option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_call(option["strike_price"], i, option["option_price"]) * stock_quantity
            option_profits[j][i] = option_profit_val  # Store the option profit for each option

        stock_profit_val = stock_profit(spot_price, option_x[i], stock_info) * stock_quantity
        stock_profit_x[i] = stock_profit_val

    for k in range(option_quantity):
        print("entered")
        plt.plot(option_x, option_profits[k], label=f'Opsiyon {k+1} Kar/Zarar')  # Plot each option profit separately

    plt.plot(option_x, stock_profit_x, color='blue', label='Hisse Senedi Kar/Zarar')
    plt.plot(option_x, np.sum(option_profits, axis=0), color='red', label='Toplam Kar/Zarar')
    plt.legend(loc='upper left')
    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)
    plt.xlabel("Spot Fiyatı")
    plt.ylabel("Kar/Zarar")
    plt.show()



if __name__ == '__main__':
    main()  