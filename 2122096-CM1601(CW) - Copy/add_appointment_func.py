# These functions allow admin to add test drive appointments
def define_number_of_appoint():
    "function to enter how many appointments that the admin going to add"
    number_of_appointments = 0
    while not (number_of_appointments > 0 and type(number_of_appointments) == int):
        try:
            number_of_appointments = int(input('Enter the number of appointments that you want to add: '))
            if number_of_appointments < 0:
                raise TypeError('Enter the number of appointments (only enter positive numbers without decimals)')
        except TypeError as e:
            print(e)
        except ValueError:
            print('Only enter positive whole numbers')
    return number_of_appointments

def append_appointments(sheet_2,max_row_2,max_column,detail_row_number,workbook_2,appointment_list):
    'function to append appointments to the workbook(this function will only allow to enter unique appointments that you haven\'t entered to the same make before)'
    number_of_appointments = define_number_of_appoint()
    for i in range(0, number_of_appointments):
        value = str(input('Enter an appointment: '))
        for j in range(2,max_row_2+1):
            if sheet_2.cell(j,1).value == detail_row_number:
                for k in range(2,max_column+1):
                    if sheet_2.cell(j,k).value == value:
                        print('You already entered that appointment to the same model')
                        value = str(input('Enter an appointment'))
        appointment_list.append(value)
    # this will save the car reference number on CarAppointment.xlsx
    sheet_2.cell(row=max_row_2 + 1, column=1, value=detail_row_number)
    workbook_2.save("CarAppointment.xlsx")
    # to save appointments on CarAppointment.xlsx
    for k in range(len(appointment_list)):
        sheet_2.cell(row=max_row_2 + 1, column=2 + k, value=appointment_list[k])
        workbook_2.save("CarAppointment.xlsx")


def enter_first_option():
    option_1 = 0
    while not (option_1 == 1 or option_1 == 2):
        try:
            option_1 = int(input('Enter your preference: '))
            if not (option_1 == 1 or option_1 == 2):
                raise TypeError('Only enter 1 or 2 as your preference')
        except TypeError as e:
            print(e)
        except ValueError:
            print('Only enter integers 1 or 2')
    return option_1

def enter_second_option():
    option_2 = 0
    while not (option_2 == 1 or option_2 == 2):
        try:
            option_2 = int(input('Enter your preference: '))
            if not (option_2 == 1 or option_2 == 2):
                raise TypeError('Only enter 1 or 2 as your preference')
        except TypeError as e:
            print(e)
        except ValueError:
            print('Only enter integers 1 or 2')
    return option_2