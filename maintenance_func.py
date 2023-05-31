def enter_maintenance_description():
    'function to enter maintenance description'
    maintenance_description = str(input("Enter maintenance description: "))
    return maintenance_description

def enter_maintenance_cost():
    'function to enter maintenance cost'
    maintenance_cost = 0
    while not(type(maintenance_cost) == float):
        try:
            maintenance_cost = float(input("Enter the total maintenance cost: "))
        except ValueError:
            print('Only type the cost without using any characters')
    return maintenance_cost

def refer_month(month,workbook_5):
    'function to refer a sheet according to technician entered month that he is going to enter details'
    if month == 1:
        sheet_5 = workbook_5['2022JAN']

    if month == 2:
        sheet_5 = workbook_5['2022FEB']

    if month == 3:
        sheet_5 = workbook_5['2022MARCH']

    if month == 4:
        sheet_5 = workbook_5['2022APRIL']

    if month == 5:
        sheet_5 = workbook_5['2022MAY']

    if month == 6:
        sheet_5 = workbook_5['2022JUNE']

    if month == 7:
        sheet_5 = workbook_5['2021JULY']

    if month == 8:
        sheet_5 = workbook_5['2021AUG']

    if month == 9:
        sheet_5 = workbook_5['2021SEP']

    if month == 10:
        sheet_5 = workbook_5['2021OCT']

    if month == 11:
        sheet_5 = workbook_5['2021NOV']

    if month == 12:
        sheet_5 = workbook_5['2021DEC']
    return sheet_5

def write_make(make_list,sheet_5,max_row_5,workbook_5):
    'function to enter the car make on MaintenanceDetails.xlsx'
    for i in range(len(make_list)):
        sheet_5.cell(row=max_row_5+(i+1),column=1,value=make_list[i])
        workbook_5.save('MaintenanceDetails.xlsx')

def write_model(model_list,sheet_5,max_row_5,workbook_5):
    'function to enter the car model on MaintenanceDetails.xlsx'
    for i in range(len(model_list)):
        sheet_5.cell(row=max_row_5+(i+1),column=2,value=model_list[i])
        workbook_5.save('MaintenanceDetails.xlsx')

def write_year(year_list,sheet_5,max_row_5,workbook_5):
    'function to enter the car year on MaintenanceDetails.xlsx'
    for i in range(len(year_list)):
        sheet_5.cell(row=max_row_5+(i+1),column=3,value=year_list[i])
        workbook_5.save('MaintenanceDetails.xlsx')

def write_maintenance_des(maintenance_des_list,sheet_5,max_row_5,workbook_5):
    'function to enter the car maintenance description on MaintenanceDetails.xlsx'
    for i in range(len(maintenance_des_list)):
        sheet_5.cell(row=max_row_5+(i+1),column=4,value=maintenance_des_list[i])
        workbook_5.save('MaintenanceDetails.xlsx')

def write_maintenance_cost(cost_list,sheet_5,max_row_5,workbook_5):
    'function to enter the car maintenance cost on MaintenanceDetails.xlsx'
    for i in range(len(cost_list)):
        sheet_5.cell(row=max_row_5+(i+1),column=5,value=cost_list[i])
        workbook_5.save('MaintenanceDetails.xlsx')