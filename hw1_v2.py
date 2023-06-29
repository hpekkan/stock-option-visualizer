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

def stock_profit(spot, current_price, stock_info):
    if stock_info.casefold() == "alım".casefold():
        return spot - current_price
    else:
        return current_price - spot

def calculate_arbitrage(option_quantity, stock_quantity, spot_price, stock_info, option_data):
    size = 1000
    option_profits = np.zeros((option_quantity, size))  # Modify to store separate option profits
    stock_profit_x = stock_profit(np.linspace(0, 3.25 * np.mean([option["strike_price"] for option in option_data]), size),
                                  spot_price, stock_info) * stock_quantity

    for i in range(size):
        for j, option in enumerate(option_data):  # Iterate over each option separately
            option_profit_val = 0
            if option["option_type"].casefold() == "put".casefold():
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_put(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_put(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity
            else:
                if option["option_info"].casefold() == "alım".casefold():
                    option_profit_val = long_call(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity
                else:
                    option_profit_val = short_call(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity
                   
            option_profits[j][i] = option_profit_val  # Store the option profit for each option

    # Calculate total profit including stock profit
    total_profits = np.sum(option_profits, axis=0) + stock_profit_x

    # Find intersection points
    intersections = np.where(np.diff(np.signbit(total_profits)) != 0)[0]

    return intersections

def plot_arbitrage(option_quantity, option_data, stock_quantity, spot_price, stock_info):
    option_x = np.linspace(0, 3.25 * np.mean([option["strike_price"] for option in option_data]), size)
    intersections = calculate_arbitrage(option_quantity, stock_quantity, spot_price, stock_info, option_data)

    plt.figure(figsize=(10, 6))
    for k in range(option_quantity):
        plt.plot(option_x, option_profits[k], color="black", label=f'Opsiyon {k+1} Kar', linestyle='dashed', dashes=(3, 3))  # Plot each option profit separately
        
    # Plot intersection points
    for intersection in intersections:
        plt.plot(option_x[intersection], 0, 'ro', markersize=5)
        plt.text(option_x[intersection], 0, f'({option_x[intersection]:.2f}, 0)', ha='center', va='bottom')

    plt.plot(option_x, stock_profit_x, color='blue', label='Hisse Senedi Kar', linestyle='dashed', dashes=(3, 3))
    plt.plot(option_x, np.sum(option_profits, axis=0), color='purple', label='Opsiyon Karı')
    plt.plot(option_x, total_profits, color='red', label='Toplam Kar')
    plt.legend(loc='upper left', bbox_to_anchor=(0, 1), bbox_transform=plt.gcf().transFigure, prop={'size': 12})

    plt.axhline(0, color='black', linewidth=.5)
    plt.axvline(0, color='black', linewidth=.5)
    plt.xlabel("Streak Fiyatı")
    plt.ylabel("Kar")

    plt.show()

def main():
    option_quantity = int(input("Kaç opsiyon kullanacaksınız: "))
    stock_quantity = int(input("Kaç hisse senedi kullanacaksınız: "))
    while stock_quantity < 0:
        stock_quantity = int(input("Hisse senedi sayısı en az 1 olmalıdır: "))
    spot_price = float(input("Hisse senedi Spot Fiyatı: "))
    stock_info = input("Hisse senedi bilgileri\n Alım/Satım: ")

    option_data = []
    counter = 1
    mean = 0
    while counter <= option_quantity:
        print("Opsiyon", counter, "Bilgileri")
        option_type = input("Tipi: ")
        option_info = input("Alım/Satım: ")
        strike_price = float(input("Strike Fiyatı: "))
        option_price = float(input("Opsiyon Fiyatı: "))
        option_data.append(
            {"option_type": option_type, "option_info": option_info, "strike_price": strike_price,
             "option_price": option_price})
        mean = mean + strike_price
        counter = counter + 1
    mean = mean / counter  

    plot_arbitrage(option_quantity, option_data, stock_quantity, spot_price, stock_info)


if __name__ == '__main__':
    main()
