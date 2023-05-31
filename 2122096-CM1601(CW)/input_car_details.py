def type_month():
    "function to enter the month that you are going to add details"
    month = 0
    while not (month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6 or month == 7 or month == 8 or month == 9 or month == 10 or month == 11 or month == 12):
        try:
            month = int(input("To enter the month just type the number according to the month, e.g. : if it is january enter 1: "))
            if not (
                    month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6 or month == 7 or month == 8 or month == 9 or month == 10 or month == 11 or month == 12):
                raise TypeError(
                    'Enter the correct number according to the related month e.g. : if it is january enter 1')
        except ValueError:
            print('Only enter integers according to the related month e.g. : if it is january enter 1')
        except TypeError as e:
            print(e)
    return month

def type_make():
    "function to enter the car make"
    make = str(input("Enter the make: "))
    return make

def type_model():
    "function to enter the car model"
    model = str(input("Enter the model: "))
    return model

def type_year():
    "function to enter which year this car modle belongs to"
    year = ''
    while len(year) != 4:
        try:
            year = str(input("Enter the year e.g. 2021 format: "))
            if len(year) != 4:
                raise TypeError ('Enter the correct format of the year e.g. 2021')
        except TypeError as e:
            print(e)
    return year

def type_mileage():
    "function to enter the mileage"
    mileage = 0
    while type(mileage) != float:
        try:
            mileage = float(input("Enter the mileage: "))
        except ValueError:
            print('Only enter integer or float numbers to mileage')
    return mileage

def type_owner_info():
    "function to enter the owner information such as 1st owner, 2nd owner, etc."
    owner_info = str(input("Enter the owner information: "))
    return owner_info

def type_ask_price():
    "function to enter the bought price"
    ask_price = 0
    while type(ask_price) != float:
        try:
            ask_price = float(input("Enter the asking price: "))
        except ValueError:
            print('Only enter integer or float numbers to your company asked price')
    return ask_price

def type_sell_price():
    "function to enter the selling price of the car"
    sell_price = 0
    while type(sell_price) != float:
        try:
            sell_price = float(input("Enter the selling price: "))
        except ValueError:
            print('Only enter integer or float numbers to the price')
    return sell_price

def type_car_status():
    "function to enter is that car sold or not"
    car_status =''
    while not (car_status == 'sold' or car_status == 'not_sold'):
        try:
            car_status = str(input("Enter the status of the car e.g.: 'sold' or 'not_sold': "))
            if not (car_status == 'sold' or car_status == 'not_sold'):
                raise TypeError('Only enter "sold" or "not_sold"')
        except ValueError:
            print('Only string value "sold" or "not_sold"')
        except TypeError as e:
            print(e)
    return car_status

def type_last_price_status():
    "function to enter is this car price is under negotiations or not"
    last_price_status = ''
    while not(last_price_status == 'fixed' or last_price_status =='not_fixed'):
        try:
            last_price_status = str(input("Enter the sell price of car model is 'fixed' or 'not_fixed'"))
            if not (last_price_status == 'fixed' or last_price_status =='not_fixed'):
                raise TypeError ('Only enter "fixed" or "not_fixed"')
        except TypeError as e:
            print(e)
    return last_price_status

def type_last_price():
    "function to enter the last selling price if the car is under negotiations"
    last_price = 0
    while type(last_price) != float:
        try:
            last_price = float(input("Enter the last selling price: "))
        except ValueError:
            print('Only enter integer or float numbers to the last selling price')
    return last_price

def refer_month(month,workbook):
    if month == 1:
        sheet = workbook['2022JAN']

    if month == 2:
        sheet = workbook['2022FEB']

    if month == 3:
        sheet = workbook['2022MARCH']

    if month == 4:
        sheet = workbook['2022APRIL']

    if month == 5:
        sheet = workbook['2022MAY']

    if month == 6:
        sheet = workbook['2022JUNE']

    if month == 7:
        sheet = workbook['2021JULY']

    if month == 8:
        sheet = workbook['2021AUG']

    if month == 9:
        sheet = workbook['2021SEP']

    if month == 10:
        sheet = workbook['2021OCT']

    if month == 11:
        sheet = workbook['2021NOV']

    if month == 12:
        sheet = workbook['2021DEC']
    return sheet