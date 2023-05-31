def view_details(new_list_2, new_list_3, car_record, max_row, sheet, number_list, make_list, model_list, year_list,
                 mileage_list, owner_info_list, ask_price_list, car_status_list, sell_price_list,last_price_status_list,last_price_list):
    'function to append each column data in separate lists and combine them all together using 2D list'
    for i in range(2, max_row + 1):
        number_list.append(sheet.cell(i, 1).value)
        make_list.append(sheet.cell(i, 2).value)
        model_list.append(sheet.cell(i, 3).value)
        year_list.append(sheet.cell(i, 4).value)
        mileage_list.append(sheet.cell(i, 5).value)
        owner_info_list.append(sheet.cell(i, 6).value)
        ask_price_list.append(sheet.cell(i, 7).value)
        sell_price_list.append(sheet.cell(i, 8).value)
        car_status_list.append(sheet.cell(i, 9).value)
        last_price_status_list.append(sheet.cell(i, 10).value)
        last_price_list.append(sheet.cell(i, 11).value)
    new_list_1 = [number_list, make_list, model_list, year_list, mileage_list, owner_info_list, ask_price_list,
                  sell_price_list, car_status_list,last_price_status_list,last_price_list]
    append_car_record(new_list_2, new_list_3, new_list_1, number_list, car_record)


def append_car_record(new_list_2, new_list_3, new_list_1, number_list, car_record):
    'function to append each row details to multiple lists and connect them together using 2D list'
    for i in range(len(number_list)):
        for j in range(11):
            new_list_2.append(new_list_1[j][i])
        new_list_3.append(new_list_2)
    for l in range(len(number_list)):
        car_record.append(new_list_3[l][11 * l:11 * (l + 1)])
    display_car_details(car_record)


def display_car_details(car_record):
    'function to print car records using a table format'
    print(""":    Number    :     Make     :     Model     :    Year    :  mileage_Km           :   owner_info    :  ask_price     :   price in AED   :    status    :  status_of selling_price  :  last_sellimg_price  :
===============================================================================================================================================================================================================================""")
    for i in range(len(car_record)):
        print(":", car_record[i][0], " " * (11 - len(str(car_record[i][0]))), ":",
              car_record[i][1], " " * (11 - len(str(car_record[i][1]))), ":",
              car_record[i][2], " " * (12 - len(str(car_record[i][2]))), ":",
              car_record[i][3], " " * (9 - len(str(car_record[i][3]))), ":",
              car_record[i][4], " " * (20 - len(str(car_record[i][4]))), ":",
              car_record[i][5], " " * (14 - len(str(car_record[i][5]))), ":",
              car_record[i][6], " " * (13 - len(str(car_record[i][6]))), ":",
              car_record[i][7], " " * (15 - len(str(car_record[i][7]))), ":",
              car_record[i][8], " " * (11 - len(str(car_record[i][8]))), ":",
              car_record[i][9], " " * (24 - len(str(car_record[i][9]))), ":",
              car_record[i][10], " " * (19 - len(str(car_record[i][10]))), ":")


def enter_option():
    option = 0
    while not (option == 1 or option == 2):
        try:
            option = int(input("Enter your preference: "))
            if not (option == 1 or option == 2):
                raise TypeError("Please, enter an integer  1 or 2 ")
        except TypeError as e:
            print(e)
        except ValueError:
            print("Only integers are allowed(1 or 2)")
    return option


def enter_second_option():
    option_2 = 0
    while not (option_2 == 1 or option_2 == 2 or option_2 == 3):
        try:
            option_2 = int(input("Enter your preference: "))
            if not (option_2 == 1 or option_2 == 2 or option_2 == 3):
                raise TypeError("Please, enter an integer  1 or 2 or 3 ")
        except TypeError as e:
            print(e)
        except ValueError:
            print("Only integers are allowed(1 or 2 or 3)")
    return option_2


def enter_record_number(max_row):
    'function to enter the record number of a car'
    detail_row_number = 0
    # this will check is the record number on CarDealership.xlsx and also is it an integer if the condition is false it will ask admin to again enter a correct record number
    while not (type(detail_row_number) == int and detail_row_number > 0 and detail_row_number < max_row):
        try:
            detail_row_number = int(input('Enter the correct record number you want to update : '))
            if not (detail_row_number > 0 and detail_row_number < max_row):
                raise TypeError('Please enter the correct record number you want to update')
        except ValueError:
            print('Only integers are allowed,Please enter the correct record number you want to update')
        except TypeError as e:
            print(e)
    return detail_row_number


def enter_column_number():
    'function to enter the column number that you want to update'
    column_number = ''
    # this will check is the column number on CarDealership.xlsx and also is it an integer if the condition is false it will ask admin to again enter a correct column number
    while not (type(column_number) == int and column_number > 1 and column_number < 12):
        try:
            column_number = int(input('Enter the column number that you want to update: '))
            if not (column_number > 1 and column_number < 12):
                raise TypeError('Please, Enter the correct column number that you want to update')
        except ValueError:
            print('Only integers are allowed,Please, Enter the correct column number that you want to update')
        except TypeError as e:
            print(e)
    return column_number


def enter_third_option():
    option_3 = 0
    while not (option_3 == 1 or option_3 == 2):
        try:
            option_3 = int(input("Enter your preference: "))
            if not (option_3 == 1 or option_3 == 2):
                raise TypeError("Please, enter an integer  1 or 2 ")
        except TypeError as e:
            print(e)
        except ValueError:
            print("Only integers are allowed(1 or 2)")
    return option_3


def enter_record_number_to_delete(max_row):
    'function to enter a record number to delete'
    detail_row_number = 0
    # this will check is the record number on CarDealership.xlsx and also is it an integer if the condition is false it will ask admin to again enter a correct record number
    while not (type(detail_row_number) == int and detail_row_number > 0 and detail_row_number < max_row):
        try:
            detail_row_number = int(input('Enter the correct record number you want to delete : '))
            if not (detail_row_number > 0 and detail_row_number < max_row):
                raise TypeError('Please enter the correct record number you want to delete')
        except ValueError:
            print('Only integers are allowed,Please enter the correct record number you want to delete')
        except TypeError as e:
            print(e)
    return detail_row_number
