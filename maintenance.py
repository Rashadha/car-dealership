def define_customer_receipt_num(sheet_3,max_row_3):
    'function to make a list which is included with customer receipts numbers on CustomerInformation.xlsx'
    custom_receipt_num = []
    for i in range(2,max_row_3+1):
        custom_receipt_num.append(sheet_3.cell(i,6).value)
    return custom_receipt_num

def define_company_receipt_num(sheet_4,max_row_4):
    'function to make a list which is included with  receipts numbers on CompanyInformation.xlsx'
    company_receipt_num = []
    for i in range(2, max_row_4 + 1):
        company_receipt_num.append(sheet_4.cell(i, 6).value)
    return company_receipt_num

def enter_receipt_num(custom_receipt_num,company_receipt_num):
    'function to enter the receipt number if they are going to look for a maintenance to the same car model which was bought by them from our company'
    receipt_num = 0
    # this will ask the receipt number until it becomes the correct receipt number
    while not((receipt_num in custom_receipt_num) or (receipt_num in company_receipt_num)):
        try:
            receipt_num = str(input('Enter your receipt number: '))
            if not ((receipt_num in custom_receipt_num) or (receipt_num in company_receipt_num)):
                raise TypeError ('Enter the correct receipt number')
        except TypeError as e:
            print(e)
    return receipt_num

def define_customer_name(sheet_3,max_row_3):
    'function to make a list including all customer names on CustomerInformation.xlsx'
    custom_name = []
    for i in range(2,max_row_3+1):
        custom_name.append(sheet_3.cell(i,1).value)
    return custom_name

def define_company_name(sheet_4,max_row_4):
    'function to make a list including all company names on CompanyInformation.xlsx'
    company_name = []
    for i in range(2,max_row_4+1):
        company_name.append(sheet_4.cell(i,1).value)
    return company_name


def enter_customer_or_company_name(receipt_num,custom_receipt_num,company_receipt_num,custom_name,company_name):
    real_cus_name = 0
    real_company_name = 0
    for i in range(len(custom_receipt_num)):
        if custom_receipt_num[i] == receipt_num :
            real_cus_name = custom_name[i]
    for i in range(len(company_receipt_num)):
        if company_receipt_num[i] == receipt_num :
            real_company_name = company_name[i]
    if receipt_num in custom_receipt_num:
        name = ''
        while name != real_cus_name:
            try:
                name = str(input("Enter your  name as mentioned in the receipt: "))
                if (name != real_cus_name):
                    raise TypeError('Enter your name as mentioned in the receipt')
            except TypeError as e:
                print(e)
    else:
        name = ''
        while name != real_company_name:
            try:
                name = str(input("Enter your  company name as mentioned in the receipt: "))
                if (name != real_company_name):
                    raise TypeError('Enter your company name as mentioned in the receipt')
            except TypeError as e:
                print(e)
    return name

def print_maintenance_time_1(sheet_5,max_row_5):
    print('Appointments')
    for i in range(2,max_row_5+1):
        print(sheet_5.cell(i,2).value)

def print_maintenance_time_2(sheet_5,max_row_5):
    print('Appointments')
    for i in range(2,max_row_5):
        print(sheet_5.cell(i,3).value)