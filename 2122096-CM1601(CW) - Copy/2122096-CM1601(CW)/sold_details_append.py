def create_cus_list(max_row_3,sheet_3):
    'function to create a list that included with car reference numbers which cars were sold to customers'
    cus_list = []
    for i in range(2,max_row_3+1):
        cus_list.append(sheet_3.cell(i,7).value)
    return cus_list

def create_comp_list(max_row_4,sheet_4):
    'function to create a list that included with car reference numbers which cars were sold to companies'
    comp_list = []
    for j in range(2,max_row_4+1):
        comp_list.append(sheet_4.cell(j,7).value)
    return comp_list

def enter_record_number_to_add_sold_info(max_row,cus_list,comp_list):
    'function to enter a car record number it will ask car record number again and again until admin types correct record number and also there shoild not be a record on CustomerInformation.xlsx or CompanyInformation.xlsx under admin entered record number'
    detail_row_number = 0
    while  ( detail_row_number <= 0 or  detail_row_number > max_row or (detail_row_number  in cus_list) or (detail_row_number  in comp_list)):
        try:
            detail_row_number = int(input('Enter the correct record number you want to add customer or company details : '))
            if (detail_row_number > 0 and detail_row_number < max_row):
                if ((detail_row_number  in cus_list) or (detail_row_number  in comp_list)):
                    raise TypeError ('You have already entered sold details related to that record number')
            if not (detail_row_number > 0 and detail_row_number < max_row):
                raise TypeError('Please enter the correct record number you want to add customer or company details')
        except ValueError:
            print('Only integers are allowed,Please enter the correct record number you want to add customer or company details')
        except TypeError as e:
            print(e)
    return detail_row_number

def refer_month(month,workbook_3):
    'function to find the correct sheet which is available on CustomerInformation.xlsx from admin entered month'
    if month == 1:
        sheet_3 = workbook_3['2022JAN']

    if month == 2:
        sheet_3 = workbook_3['2022FEB']

    if month == 3:
        sheet_3 = workbook_3['2022MARCH']

    if month == 4:
        sheet_3 = workbook_3['2022APRIL']

    if month == 5:
        sheet_3 = workbook_3['2022MAY']

    if month == 6:
        sheet_3 = workbook_3['2022JUNE']

    if month == 7:
        sheet_3 = workbook_3['2021JULY']

    if month == 8:
        sheet_3 = workbook_3['2021AUG']

    if month == 9:
        sheet_3 = workbook_3['2021SEP']

    if month == 10:
        sheet_3 = workbook_3['2021OCT']

    if month == 11:
        sheet_3 = workbook_3['2021NOV']

    if month == 12:
        sheet_3 = workbook_3['2021DEC']
    return sheet_3

def refer_month_in_CompnyDetails_workbook(month,workbook_4):
    'function to find the correct sheet which is available on CompanyInformation.xlsx from admin entered month'
    if month == 1:
        sheet_4 = workbook_4['2022JAN']

    if month == 2:
        sheet_4 = workbook_4['2022FEB']

    if month == 3:
        sheet_4 = workbook_4['2022MARCH']

    if month == 4:
        sheet_4 = workbook_4['2022APRIL']

    if month == 5:
        sheet_4 = workbook_4['2022MAY']

    if month == 6:
        sheet_4 = workbook_4['2022JUNE']

    if month == 7:
        sheet_4 = workbook_4['2021JULY']

    if month == 8:
        sheet_4 = workbook_4['2021AUG']

    if month == 9:
        sheet_4 = workbook_4['2021SEP']

    if month == 10:
        sheet_4 = workbook_4['2021OCT']

    if month == 11:
        sheet_4 = workbook_4['2021NOV']

    if month == 12:
        sheet_4 = workbook_4['2021DEC']
    return sheet_4

def enter_customer_name():
    'function to enter customer name'
    customer_name = str(input("Enter customer name: "))
    return customer_name

def enter_company_name():
    'function to enter company name'
    company_name = str(input("Enter company name: "))
    return company_name

def enter_customer_address():
    'function to enter customer address'
    customer_address = str(input("Enter customer address "))
    return customer_address

def enter_company_location():
    'function to enter company location'
    company_location = str(input("Enter customer company location "))
    return company_location

def enter_customer_contact_number():
    'function to enter customer contact number'
    customer_contact_number = str(input("Enter customer contact number: "))
    return customer_contact_number

def enter_company_contact_number():
    'function to enter company contact number'
    company_contact_number = str(input("Enter company contact number: "))
    return company_contact_number

def enter_payment_type():
    'function to enter payment type is it \'card\' or \'cash\''
    payment_type = ''
    while not(payment_type == 'cash' or payment_type == 'card'):
        try:
            payment_type = str(input("Enter payment type as 'card' or 'cash'"))
            if not (payment_type == 'cash' or payment_type == 'card'):
                raise TypeError('Only mention payment type as "card" or "cash"')
        except TypeError as e:
            print(e)
    return payment_type

def enter_account_number(payment_type):
    'function to enter the account number if it is a card'
    account_number = ''
    if payment_type == 'card':
        while not(len(account_number) == 16):
            try:
                account_number = str(input('Enter the account number without using spaces: '))
                if not(len(account_number) == 16):
                    raise TypeError ('Only tpe account number without using spaces')
            except TypeError as e:
                print(e)
    else:
        account_number = '-'
    return account_number

def enter_receipt_number():
    'function to enter the payment receipt number'
    receipt_number = str(input('Enter receipt number: '))
    return receipt_number

def enter_car_make(max_row,sheet,detail_row_number):
    'function to enter the car make this will take the car make value from CarDealership.xlsx which is belonging to admin entered car reference number'
    for i in range(2,max_row+1):
        if sheet.cell(i,1).value == detail_row_number:
            car_make = sheet.cell(i,2).value
    return car_make

def enter_car_model(max_row,sheet,detail_row_number):
    'function to enter the car model this will take the car model value from CarDealership.xlsx which is belonging to admin entered car reference number'
    for i in range(2,max_row+1):
        if sheet.cell(i,1).value == detail_row_number:
            car_model = sheet.cell(i,3).value
    return car_model

def enter_car_year(max_row,sheet,detail_row_number):
    "function to enter the car year this will take the car year value from CarDealership.xlsx which is belonging to admin entered car reference number"
    for i in range(2,max_row+1):
        if sheet.cell(i,1).value == detail_row_number:
            car_year = sheet.cell(i,4).value
    return car_year

def enter_sold_price(max_row,sheet,detail_row_number):
    'function to enter the last sold price'
    import update_record
    #  this will referes to CarDealership.xlsx and if the car model under negotiations this will ask from the admin like was this sold under negotiations or not
    for i in range(2,max_row+1):
        if sheet.cell(i,1).value == detail_row_number:
            if sheet.cell(i,10).value == 'not_fixed':
                print('This car make contains negotiations:\nif the customer bought it under negotiations --> press 1\nif not --> press 2')
                option = update_record.enter_option()
                # if it was sold under negotiation it will take the last sold price from CarDealership.xlsx , if not admin has to enter the value
                if option == 1:
                    sold_price = sheet.cell(i,11).value
                else:
                    sold_price = 0
                    while type(sold_price) != float:
                        try:
                            sold_price = float(input('Enter the sold price under negotiations: '))
                        except ValueError:
                            print("Enter only integer numbers or float to the sold price")
            # if this car model price is fixed it also take the value from carDealership.xlsx
            else:
                sold_price = sheet.cell(i, 8).value

    return sold_price

def write_record_name_cus(name_list,sheet_3,max_row_3,workbook_3):
    'function to append customer name on CustomerInformation.xlsx'
    for i in range(len(name_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=1,value=name_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_address_cus(address_list,sheet_3,max_row_3,workbook_3):
    'function to append customer address on CustomerInformation.xlsx'
    for i in range(len(address_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=2,value=address_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_contact_num_cus(contact_num_list,sheet_3,max_row_3,workbook_3):
    'function to append customer contact number on CustomerInformation.xlsx'
    for i in range(len(contact_num_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=3,value=contact_num_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_payment_type_cus(payment_type_list,sheet_3,max_row_3,workbook_3):
    'function to append customer payment type as \'card\' or \'cash\' on CustomerInformation.xlsx'
    for i in range(len(payment_type_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=4,value=payment_type_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_account_num_cus(account_num_list,sheet_3,max_row_3,workbook_3):
    'function to append customer account number if the payment type is card on CustomerInformation.xlsx'
    for i in range(len(account_num_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=5,value=account_num_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_receipt_num_cus(receipt_num_list,sheet_3,max_row_3,workbook_3):
    'function to append customer receipt number after paying the payment to the car on CustomerInformation.xlsx'
    for i in range(len(receipt_num_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=6,value=receipt_num_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_car_ref_num_cus(number_list,sheet_3,max_row_3,workbook_3):
    'function to append car reference number which car the customer has bought on CustomerInformation.xlsx'
    for i in range(len(number_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=7,value=number_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_car_make_cus(make_list,sheet_3,max_row_3,workbook_3):
    'function to append car make which car make the customer has bought on CustomerInformation.xlsx'
    for i in range(len(make_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=8,value=make_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_car_model_cus(model_list,sheet_3,max_row_3,workbook_3):
    'function to append car model which car model the customer has bought on CustomerInformation.xlsx'
    for i in range(len(model_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=9,value=model_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_car_year_cus(year_list,sheet_3,max_row_3,workbook_3):
    'function to append car year that the customer bought car model belongs to which year on CustomerInformation.xlsx'
    for i in range(len(year_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=10,value=year_list[i])
        workbook_3.save('CustomerInformation.xlsx')

def write_record_car_sold_price_cus(sold_price_list,sheet_3,max_row_3,workbook_3):
    'function to append the last sold price of the car on CustomerInformation.xlsx'
    for i in range(len(sold_price_list)):
        sheet_3.cell(row=max_row_3+(i+1),column=11,value=sold_price_list[i])
        workbook_3.save('CustomerInformation.xlsx')




def write_record_name_comp(name_list, sheet_4, max_row_4, workbook_4):
    'function to append company name on CompanyInformation.xlsx'
    for i in range(len(name_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=1, value=name_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_address_comp(address_list, sheet_4, max_row_4, workbook_4):
    'function to append company location on CompanyInformation.xlsx'
    for i in range(len(address_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=2, value=address_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_contact_num_comp(contact_num_list, sheet_4, max_row_4, workbook_4):
    'function to append company contact number on CompanyInformation.xlsx'
    for i in range(len(contact_num_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=3, value=contact_num_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_payment_type_comp(payment_type_list, sheet_4, max_row_4, workbook_4):
    'function to append company payment type as \'card\' or \'cash\' on CompanyInformation.xlsx'
    for i in range(len(payment_type_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=4, value=payment_type_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_account_num_comp(account_num_list, sheet_4, max_row_4, workbook_4):
    'function to append company account number if the payment type is card on CompanyInformation.xlsx'
    for i in range(len(account_num_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=5, value=account_num_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_receipt_num_comp(receipt_num_list, sheet_4, max_row_4, workbook_4):
    'function to append company receipt number after paying the payment to the car on CompanyInformation.xlsx'
    for i in range(len(receipt_num_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=6, value=receipt_num_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_car_ref_num_comp(number_list, sheet_4, max_row_4, workbook_4):
    'function to append car reference number which car the company has bought on CompanyInformation.xlsx'
    for i in range(len(number_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=7, value=number_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_car_make_comp(make_list, sheet_4, max_row_4, workbook_4):
    'function to append car make which car make the company has bought on CompanyInformation.xlsx'
    for i in range(len(make_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=8, value=make_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_car_model_comp(model_list, sheet_4, max_row_4, workbook_4):
    'function to append car model which car model the company has bought on CompanyInformation.xlsx'
    for i in range(len(model_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=9, value=model_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_car_year_comp(year_list, sheet_4, max_row_4, workbook_4):
    'function to append car year that the company bought car model belongs to which year on CompanyInformation.xlsx'
    for i in range(len(year_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=10, value=year_list[i])
        workbook_4.save('CompanyInformation.xlsx')


def write_record_car_sold_price_comp(sold_price_list, sheet_4, max_row_4, workbook_4):
    'function to append the last sold price of the car on CompanyInformation.xlsx'
    for i in range(len(sold_price_list)):
        sheet_4.cell(row=max_row_4 + (i + 1), column=11, value=sold_price_list[i])
        workbook_4.save('CompanyInformation.xlsx')