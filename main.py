import numpy as np
from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

def long_put(strike, spot, op_price):
    return -op_price if strike > spot else (spot - strike - op_price)

def short_put(strike, spot, op_price):
    return op_price if strike > spot else (strike - spot + op_price)

def long_call(strike, spot, op_price):
    return (strike - op_price - spot) if strike > spot else -op_price

def short_call(strike, spot, op_price):
    return op_price if strike < spot else (spot - strike + op_price)

def stock_profit(spot, current_price, stock_info):
    if stock_info.lower() == "buy":
        return spot - current_price
    else:
        return current_price - spot

def print_arbitrage_opportunities(option_data, spot_price):
    for i, option in enumerate(option_data):
        option_type = option["option_type"]
        option_info = option["option_info"]
        strike_price = option["strike_price"]
        option_price = option["option_price"]

        if option_type.lower() == "put":
            if option_info.lower() == "buy" and option_price + strike_price > spot_price:
                print(f"Arbitrage opportunity detected in Put Buy option. Option {i+1}")
        elif option_type.lower() == "call":
            if option_info.lower() == "buy" and option_price + strike_price < spot_price:
                print(f"Arbitrage opportunity detected in Call Buy option. Option {i+1}")

def main():
    option_quantity = int(input("How many options will you use: "))
    stock_quantity = int(input("How many stocks will you use: "))
    
    while stock_quantity < 1:
        stock_quantity = int(input("Number of stocks must be at least 1: "))
    
    spot_price = float(input("Stock Spot Price: "))
    stock_info = input("Stock information (Buy/Sell): ")

    option_data = []
    size = 100000
    stock_profit_x = np.zeros(size)
    option_profits = np.zeros((option_quantity, size))
    counter = 1

    while counter <= option_quantity:
        print("Option", counter, "Information")
        option_type = input("Type: ")
        option_info = input("Buy/Sell: ")
        strike_price = float(input("Strike Price: "))
        option_price = float(input("Option Price: "))
        option_data.append({
            "option_type": option_type,
            "option_info": option_info,
            "strike_price": strike_price,
            "option_price": option_price,
        })
        counter += 1

    option_x = np.linspace(0, 2 * spot_price, size)
    for i in range(size):
        stock_profit_val = 0
        for j, option in enumerate(option_data):
            option_profit_val = 0
            if option["option_type"].lower() == "put":
                if option["option_info"].lower() == "buy":
                    option_profit_val = (long_put(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity)
                else:
                    option_profit_val = (short_put(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity)
            else:
                if option["option_info"].lower() == "buy":
                    option_profit_val = (long_call(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity)
                else:
                    option_profit_val = (short_call(option_x[i], option["strike_price"], option["option_price"]) * stock_quantity)

            option_profits[j][i] = option_profit_val

        stock_profit_val = (stock_profit(option_x[i], spot_price, stock_info) * stock_quantity)
        stock_profit_x[i] = stock_profit_val

    print_arbitrage_opportunities(option_data, spot_price)

    plt.figure(figsize=(10, 6))
    colors = ['pink','magenta', 'green', 'red', 'purple', 'orange', 'brown']

    for k in range(option_quantity):
        plt.plot(
            option_x,
            option_profits[k],
            color=colors[k % len(colors)],  # Use a color from the list based on k
            label=f"Option {k+1} Profit",
            linestyle="dashed",
            dashes=(3, 3),
        )

    plotted_stocks = []
    sums = np.sum(option_profits, axis=0)

    is_zero = sums[0] == 0
    for counter in range(len(sums) - 1):
        if is_zero != (sums[counter] == 0):
            plotted_stocks.append(counter)
            plt.plot(option_x[counter], 0, "o", markersize=5, color="purple")
            plt.text(
                option_x[counter],
                0,
                f"({option_x[counter]:.2f}, 0)",
                ha="center",
                va="bottom",
                color="purple",
            )
            is_zero = not is_zero
    intersections = np.where(np.diff(np.signbit(np.sum(option_profits, axis=0))) != 0)[0]

    for intersection in intersections:
        if intersection not in plotted_stocks:
            plotted_stocks.append(intersection)
            plt.plot(option_x[intersection], 0, "o", markersize=5)
            plt.text(
                option_x[intersection],
                0,
                f"({option_x[intersection]:.2f}, 0)",
                ha="center",
                va="bottom",
                color="purple",
            )

    plotted_stocks = []
    sums = np.sum(option_profits, axis=0) + stock_profit_x

    is_zero = sums[0] == 0
    for counter in range(len(sums) - 1):
        if is_zero != (sums[counter] == 0):
            plotted_stocks.append(counter)
            plt.plot(option_x[counter], 0, "ro", markersize=5)
            plt.text(
                option_x[counter],
                0,
                f"({option_x[counter]:.2f}, 0)",
                ha="center",
                va="bottom",
                color="red",
            )
            is_zero = not is_zero
    intersections = np.where(
        np.diff(np.signbit(np.sum(option_profits, axis=0) + stock_profit_x)) != 0
    )[0]

    for intersection in intersections:
        if intersection not in plotted_stocks:
            plotted_stocks.append(intersection)
            plt.plot(option_x[intersection], 0, "ro", markersize=5)
            plt.text(
                option_x[intersection],
                0,
                f"({option_x[intersection]:.2f}, 0)",
                ha="center",
                va="bottom",
                color="red",
            )

    sums = np.sum(option_profits, axis=0) + stock_profit_x

    plt.plot(spot_price, 0, "o", markersize=5, color="blue")
    plt.text(
        spot_price, -5, f"({spot_price}, 0)", ha="center", va="bottom", color="blue"
    )

    plt.plot(
        option_x,
        stock_profit_x,
        color="blue",
        label="Stock Profit",
        linestyle="dashed",
        dashes=(3, 3),
    )
    plt.plot(
        option_x,
        np.sum(option_profits, axis=0),
        color="purple",
        label="Option Profit",
    )
    plt.plot(
        option_x,
        np.sum(option_profits, axis=0) + stock_profit_x,
        color="red",
        label="Total Profit",
    )
    plt.legend(
        loc="upper left",
        bbox_to_anchor=(0, 1),
        bbox_transform=plt.gcf().transFigure,
        prop={"size": 12},
    )

    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.xlabel("Strike Price")
    plt.ylabel("Profit")

    plt.show()

if __name__ == "__main__":
    main()
