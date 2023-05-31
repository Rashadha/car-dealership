def enter_first_option():
    option = 0
    while not (option == 1 or option == 2 or option == 3 or option == 4):
        try:
            option = int(input("Enter your preference: "))
            if not (option == 1 or option == 2 or option == 3 or option == 4):
                raise TypeError("Please, enter an integer between 1 and 4 including 1 and 4")
        except TypeError as e:
            print(e)
        except ValueError:
            print("Only integers are allowed(between 0 to 4 including 0 and 4)")
    return option

def enter_second_option():
    option_1 = 0
    print("""If you want to sort the above details\nin ascending order --> press 1\ndescending order --> press 2
                           """)
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

def enter_user_prefer_mileage():
    user_prefer_mileage = 0
    while not(user_prefer_mileage > 0 or type(user_prefer_mileage) == float):
        try:
            user_prefer_mileage = float(input("Enter the maximum mileage you prefer in Km: "))
            if user_prefer_mileage < 0 or user_prefer_mileage == 0:
                raise TypeError('Enter positive value as a mileage')
        except ValueError:
            print('Only enter positive value as a mileage')
        except TypeError as e:
            print(e)
    return user_prefer_mileage

def enter_third_option():
    option = 0
    print("""If you want to sort the above details\nby mileage --> press 1\nby budget --> press 2
                   """)
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

def enter_user_budget():
    budget = 0
    while not(budget > 0 or type(budget) == float):
        try:
            budget = float(input("Enter the maximum amount that you can afford for a car: "))
            if budget < 0 or budget == 0:
                raise TypeError('Enter positive value as a budget')
        except ValueError:
            print('Only enter positive value as a budget')
        except TypeError as e:
            print(e)
    return budget

def without_any_sort(new_list_2,new_list_3,car_record,option,option_1,max_row,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,sell_price_list):
    'function to append column data which can be used as enable to see by customers in separate lists and combine them all together using 2D list'
    for i in range(2, max_row+1):
        if sheet.cell(i, 9).value == "not_sold":
            number_list.append(sheet.cell(i, 1).value)
            make_list.append(sheet.cell(i, 2).value)
            model_list.append(sheet.cell(i, 3).value)
            year_list.append(sheet.cell(i, 4).value)
            mileage_list.append(sheet.cell(i, 5).value)
            owner_info_list.append(sheet.cell(i, 6).value)
            sell_price_list.append(sheet.cell(i, 8).value)
    new_list_1 = [number_list,make_list, model_list, year_list, mileage_list, owner_info_list, sell_price_list]
    append_car_record(new_list_2,new_list_3,new_list_1, make_list,option,option_1,car_record)

def sort_by_mileage(new_list_2,new_list_3,car_record,option,option_1,user_prefer_mileage,max_row,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,sell_price_list):
    'function to append data into separate lists which mileages are under or same to user prefer mileage and combine them all together using 2D list'
    for i in range(2, max_row):
        if sheet.cell(i, 9).value == "not_sold":
            if sheet.cell(i, 5).value <= user_prefer_mileage:
                number_list.append(sheet.cell(i, 1).value)
                make_list.append(sheet.cell(i, 2).value)
                model_list.append(sheet.cell(i, 3).value)
                year_list.append(sheet.cell(i, 4).value)
                mileage_list.append(sheet.cell(i, 5).value)
                owner_info_list.append(sheet.cell(i, 6).value)
                sell_price_list.append(sheet.cell(i, 8).value)
    new_list_1 = [number_list,make_list, model_list, year_list, mileage_list, owner_info_list, sell_price_list]
    append_car_record(new_list_2,new_list_3,new_list_1, make_list,option,option_1,car_record)

def sort_by_budget(new_list_2,new_list_3,car_record,option,option_1,budget,max_row,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,sell_price_list):
    'function to append data into separate lists which selling prices are under or same to user budget and combine them all together using 2D list'
    for i in range(2, max_row):
        if sheet.cell(i, 9).value == "not_sold":
            if sheet.cell(i, 8).value <= budget:
                number_list.append(sheet.cell(i, 1).value)
                make_list.append(sheet.cell(i, 2).value)
                model_list.append(sheet.cell(i, 3).value)
                year_list.append(sheet.cell(i, 4).value)
                mileage_list.append(sheet.cell(i, 5).value)
                owner_info_list.append(sheet.cell(i, 6).value)
                sell_price_list.append(sheet.cell(i, 8).value)


    new_list_1 = [number_list,make_list, model_list, year_list, mileage_list, owner_info_list, sell_price_list]
    append_car_record(new_list_2,new_list_3,new_list_1, make_list,option,option_1,car_record)

def sort_by_mileage_and_budget(new_list_2,new_list_3,car_record,option,option_1,budget,user_prefer_mileage,max_row,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,sell_price_list):
    'function to append data into separate lists which selling prices are under or same to user budget and which mileages are under or same to user prefer mileage then combine them all together using 2D list'
    for i in range(2, max_row):
        if sheet.cell(i, 9).value == "not_sold":
            if sheet.cell(i, 5).value <= user_prefer_mileage:
                if sheet.cell(i, 8).value <= budget:
                    number_list.append(sheet.cell(i, 1).value)
                    make_list.append(sheet.cell(i, 2).value)
                    model_list.append(sheet.cell(i, 3).value)
                    year_list.append(sheet.cell(i, 4).value)
                    mileage_list.append(sheet.cell(i, 5).value)
                    owner_info_list.append(sheet.cell(i, 6).value)
                    sell_price_list.append(sheet.cell(i, 8).value)

    new_list_1 = [number_list,make_list, model_list, year_list, mileage_list, owner_info_list, sell_price_list]
    append_car_record(new_list_2,new_list_3,new_list_1, make_list,option,option_1,car_record)


def append_car_record(new_list_2,new_list_3,new_list_1,make_list,option,option_1,car_record):
    'function to append each row details to multiple lists that the customer can view and connect them together using 2D list'
    for i in range(len(make_list)):
        for j in range(7):
            new_list_2.append(new_list_1[j][i])
        new_list_3.append(new_list_2)

    for l in range(len(make_list)):
        car_record.append(new_list_3[l][7 * l:7 * (l + 1)])

    if option == 1 :
        sort_mileage(car_record,option_1)
    elif option == 2 :
        sort_sell_price(car_record,option_1)
    elif option == 0:
        display_car_details(car_record)


def sort_mileage (car_record,option_1):
    'function sort to customer visible records according to user prefer mileage'
    for i in range(1,len(car_record)):
        for j in range(0,5):
            if j == 4:
                value_to_sort = car_record[i][4]
                # to sort in ascending order
                if option_1 == 1:
                    while car_record[i - 1][4] > value_to_sort and i > 0:
                        car_record[i], car_record[i - 1] = car_record[i - 1], car_record[i]
                        i = i - 1
                # to sort in descending order
                else:
                    while car_record[i - 1][4] < value_to_sort and i > 0:
                        car_record[i], car_record[i - 1] = car_record[i - 1], car_record[i]
                        i = i - 1

    display_car_details(car_record)




def sort_sell_price (car_record,option_1):
    'function sort to customer visible records according to user budget'
    for i in range(1,len(car_record)):
        for j in range(0,7):
            if j == 6:
                value_to_sort = car_record[i][6]
                # to sort in ascending order
                if option_1 == 1:
                    while car_record[i - 1][6] > value_to_sort and i > 0:
                        car_record[i], car_record[i - 1] = car_record[i - 1], car_record[i]
                        i = i - 1
                # to sort in descending order
                else:
                    while car_record[i - 1][6] < value_to_sort and i > 0:
                        car_record[i], car_record[i - 1] = car_record[i - 1], car_record[i]
                        i = i - 1
    display_car_details(car_record)

def display_car_details(car_record):
    'function to display records that the user can view'
    print(""":    Number    :     Make     :     Model     :    Year    :  mileage_Km           :   owner_info    :   price in AED   :
==================================================================================================================================""")
    for i in range(len(car_record)):
        print(":", car_record[i][0], " " * (11 - len(str(car_record[i][0]))), ":",
              car_record[i][1], " " * (11 - len(str(car_record[i][1]))), ":",
              car_record[i][2], " " * (12 - len(str(car_record[i][2]))), ":",
              car_record[i][3], " " * (9 - len(str(car_record[i][3]))), ":",
              car_record[i][4], " " * (20 - len(str(car_record[i][4]))), ":",
              car_record[i][5], " " * (14 - len(str(car_record[i][5]))), ":",
              car_record[i][6], " " * (15 - len(str(car_record[i][6]))), ":")