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
    option_quantity = int(input("Kaç opsiyon kullanacaksınız: "))
    stock_quantity = int(input("Kaç hisse senedi kullanacaksınız: "))
    spot_price = int(input("Hisse senedi Spot Fiyatı: "))
    stock_info = input("Hisse senedi bilgileri\n Alım/Satım: ")
    options=[]
    counter = 1
    while counter<=option_quantity:
        print("Opsiyon",counter,"Bilgileri")
        option_type = input("Tipi: ")
        option_info = input("Alım/Satım: ")
        strike_price = int(input("Strike Fiyatı: "))
        option_price = int(input("Opsiyon Fiyatı: "))
        if option_type == "Put":
            if option_info == "Alım":
                options.append(long_put(strike_price, spot_price, option_price))
            else:
                options.append(short_put(strike_price, spot_price, option_price))
        else:
            if option_info == "Alım":
                options.append(long_call(strike_price, spot_price, option_price))
            else:
                options.append(short_call(strike_price, spot_price, option_price))
        counter = counter + 1
    print("Opsiyonlar: ",options)


if __name__ == '__main__':
    main()  