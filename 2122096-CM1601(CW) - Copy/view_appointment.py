def enter_first_option():
    option_1 = 0
    while not (option_1 == 1 or option_1 == 2):
        try:
            option_1 = int(input("Enter your preference: "))
            if not (option_1 == 1 or option_1 == 2):
                raise TypeError("Please, enter an integer 1 or 2 ")
        except TypeError as e:
            print(e)
        except ValueError:
            print("Only integers are allowed(1 or 2)")
    return option_1

def enter_car_number(max_row,sheet):
    'function to enter the car reference number that is visible on the screen according to which car model customer is looking for an appointment'
    not_sold_number_list = []
    car_num = 0
    # to append every not_sold car model reference numbers into a list
    for i in range(2,max_row+1):
        if sheet.cell(i,9).value == 'not_sold':
            not_sold_number_list.append(sheet.cell(i,1).value)
    # this enables customer to enter car model reference number until it becomes correct
    while car_num not in not_sold_number_list :
        try:
            car_num = int(input('Enter the car number that you need an appointment: '))
            if car_num not in not_sold_number_list:
                raise TypeError ('Enter a correct car number')
        except ValueError:
            print('Only enter positive integers as a car number according to the car details')
        except TypeError as e:
            print(e)
    return car_num

def print_appointments(max_row_2,sheet_2,car_num,max_column):
    'function to print appointments that are available to customer entered correct car model'
    appointment_list =[]
    for i in range(2,max_row_2+1):
        if sheet_2.cell(i, 1).value == car_num:
            for j in range(2,max_column+1):
                if sheet_2.cell(i,j).value != None:
                    appointment_list.append(sheet_2.cell(i,j).value)
   # if this condition true it will print as follows
    if len(appointment_list) == 0:
        print('Sorry,there is no any available appointments to that car model')
   # if there are appointments belong to that customer entered car model system will print them
    else:
        for element in appointment_list:
            print(element)