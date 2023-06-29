import numpy as np

def call_put(strike, spot, op_price):
    # Calculate the call/put price given the strike, spot, and option price
    # Input: Strike, Spot, OpPrice
    # Output: Call/Put price
    if strike > spot:
        return op_price + strike - spot
    else:
        return op_price 

def main():
    option_quantity = input("Kaç opsiyon kullanacaksınız: ")
    stock_quantity = input("Kaç hisse senedi kullanacaksınız: ")
    spot_price = input("Hisse senedi Spot Fiyatı: ")
    
    


if __name__ == '__main__':
    main()  