import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText

def long_put(strike, spot, op_price):
    return -op_price if strike > spot else (spot-strike- op_price)

def short_put(strike, spot, op_price):
    return op_price if strike > spot else (strike - spot + op_price)

def long_call(strike, spot, op_price):
    return (strike - op_price - spot) if strike > spot else -op_price

def short_call(strike, spot, op_price):
    return op_price if strike < spot else (spot - strike + op_price)

def stock_profit(spot,current_price, stock_info):
    if stock_info.casefold() == "alım".casefold():
        return spot - current_price
    else:
        return current_price - spot
def print_arbitrage_opportunities(option_data,spot_price):
    for i, option in enumerate(option_data):
        option_type = option["option_type"]
        option_info = option["option_info"]
        strike_price = option["strike_price"]
        option_price = option["option_price"]

        if option_type.casefold() == "put".casefold():
            if option_info.casefold() == "alım".casefold() and option_price+strike_price >  spot_price:
                print(f"Put Alım opsiyonunda arbitraj fırsatı tespit edildi. Opsiyon {i+1}")
        elif option_type.casefold() == "call".casefold():
            if option_info.casefold() == "alım".casefold() and option_price +strike_price< spot_price :
                print(f"Call Alım opsiyonunda arbitraj fırsatı tespit edildi. Opsiyon {i+1}")

def print_arbitrage_opportunities(option_data, spot_price):
    for i, option in enumerate(option_data):
        option_type = option["option_type"]
        option_info = option["option_info"]
        strike_price = option["strike_price"]
        option_price = option["option_price"]

        if option_type.casefold() == "put".casefold():
            if option_info.casefold() == "alım".casefold() and option_price+strike_price >  spot_price and option_price > max(other_option["option_price"] for other_option in option_data if other_option["option_type"].casefold() == "put".casefold() and  other_option["option_info"].casefold() == "alım".casefold() and other_option["strike_price"] < strike_price):
                print(f"Put Alım opsiyonunda arbitraj fırsatı tespit edildi. Opsiyon {i+1}")
        elif option_type.casefold() == "call".casefold():
            if option_info.casefold() == "alım".casefold() and option_price +strike_price< spot_price and option_price > max(other_option["option_price"] for other_option in option_data if other_option["option_type"].casefold() == "call".casefold() and other_option["option_info"].casefold() == "alım".casefold() and other_option["strike_price"] > strike_price):
                print(f"Call Alım opsiyonunda arbitraj fırsatı tespit edildi. Opsiyon {i+1}")

def main():
    option_quantity = int(input("Kaç opsiyon kullanacaksınız: "))
    stock_quantity = int(input("Kaç hisse senedi kullanacaksınız: "))
    while stock_quantity < 0:
        stock_quantity = int(input("Hisse senedi sayısı en az 1 olmalıdır: "))
    spot_price = float(input("Hisse senedi Spot Fiyatı: "))
    stock_info = input("Hisse senedi bilgileri\n Alım/Satım: ")    
    
    option_data = []
    size = 10000
    stock_profit_x = np.zeros(size)
    option_profits = np.zeros((option_quantity, size))  # Modify to store separate option profits
    counter = 1

    while counter <= option_quantity:
        print("Opsiyon", counter, "Bilgileri")
        option_type = input("Tipi: ")
        option_info = input("Alım/Satım: ")
        strike_price = float(input("Strike Fiyatı: "))
        option_price = float(input("Opsiyon Fiyatı: "))
        option_data.append(
            {"option_type": option_type, "option_info": option_info, "strike_price": strike_price,
             "option_price": option_price})
        
        counter = counter + 1
     
    option_x = np.linspace(0, 2* spot_price, size)
    for i in range(size):
        stock_profit_val = 0
        for j, option in enumerate(option_data):  # Iterate over each option separately
            option_profit_val = 0
            if option["option_type"].casefold() == "put".casefold():
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_put(option_x[i],option["strike_price"], option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_put(option_x[i],option["strike_price"], option["option_price"]) * stock_quantity
                    
                    
            else:
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_call(option_x[i],option["strike_price"],  option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_call(option_x[i],option["strike_price"],  option["option_price"]) * stock_quantity
                   
            option_profits[j][i] = option_profit_val  # Store the option profit for each option
        
        stock_profit_val = stock_profit(option_x[i],spot_price,  stock_info) * stock_quantity
        stock_profit_x[i] = stock_profit_val
        
            
    print_arbitrage_opportunities(option_data,spot_price)
    if stock_profit_x[int(spot_price)] > 0:
        print("Arbitraj fırsatı tespit edildi.")
        
    plt.figure(figsize=(10, 6))
    for k in range(option_quantity):
        plt.plot(option_x, option_profits[k],color="black", label=f'Opsiyon {k+1} Kar', linestyle='dashed' ,dashes=(3, 3))  # Plot each option profit separately
        
    # Find intersection points
    sums = np.sum(option_profits, axis=0)
    
    is_zero = sums[0]==0
    for counter in range(len(sums)-1):
        if is_zero != (sums[counter]==0):
            plt.plot(option_x[counter], 0, 'o', markersize=5, color="purple")
            plt.text(option_x[counter], 0, f'({option_x[counter]:.2f}, 0)', ha='center', va='bottom', color="purple")
            is_zero = not is_zero
             
    
    sums = np.sum(option_profits, axis=0)+ stock_profit_x
    
    # Plot intersection points
    is_zero = sums[0]==0
    for counter in range(len(sums)-1):
        if is_zero != (sums[counter]==0):
            plt.plot(option_x[counter], 0, 'ro', markersize=5)
            plt.text(option_x[counter], 0, f'({option_x[counter]:.2f}, 0)', ha='center', va='bottom', color="red")
            is_zero = not is_zero
             
    
    plt.plot(spot_price, 0, 'o', markersize=5 ,color="blue")
    plt.text(spot_price, -10, f'({spot_price}, 0)', ha='center', va='bottom' ,color="blue")

    plt.plot(option_x, stock_profit_x, color='blue', label='Hisse Senedi Kar',linestyle='dashed',dashes=(3, 3))
    plt.plot(option_x, np.sum(option_profits, axis=0), color='purple', label='Opsiyon Karı')
    plt.plot(option_x, np.sum(option_profits, axis=0)+stock_profit_x, color='red', label='Toplam Kar')
    plt.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=plt.gcf().transFigure, prop={'size': 12})

    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)
    plt.xlabel("Streak Fiyatı")
    plt.ylabel("Kar")
    
    plt.show()



if __name__ == '__main__':
    main()  