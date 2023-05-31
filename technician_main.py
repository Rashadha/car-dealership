import openpyxl
import input_car_details
import view_appointment
import maintenance_func
workbook_5 = openpyxl.load_workbook("MaintenanceDetails.xlsx")


# declare variables
make_list = []
model_list = []
year_list = []
maintenance_des_list = []
cost_list = []

print('If you want to add maintenance details --> press 1\nif not --> press 2')
option = view_appointment.enter_first_option()
while option == 1:
    month = input_car_details.type_month()
    make = input_car_details.type_make()
    model = input_car_details.type_model()
    year = input_car_details.type_year()
    maintenance_description = maintenance_func.enter_maintenance_description()
    maintenance_cost = maintenance_func.enter_maintenance_cost()

    make_list.append(make)
    model_list.append(model)
    year_list.append(year)
    maintenance_des_list.append(maintenance_description)
    cost_list.append(maintenance_cost)

    sheet_5 = maintenance_func.refer_month(month,workbook_5)
    max_row_5 = sheet_5.max_row
    maintenance_func.write_make(make_list,sheet_5,max_row_5,workbook_5)
    maintenance_func.write_model(model_list,sheet_5,max_row_5,workbook_5)
    maintenance_func.write_year(year_list,sheet_5,max_row_5,workbook_5)
    maintenance_func.write_maintenance_des(maintenance_des_list,sheet_5,max_row_5,workbook_5)
    maintenance_func.write_maintenance_cost(cost_list,sheet_5,max_row_5,workbook_5)

    make_list.clear()
    model_list.clear()
    year_list.clear()
    maintenance_des_list.clear()
    cost_list.clear()

    print("If you want to add maintenance details again --> press 1\nif not --> press 2")
    option = view_appointment.enter_first_option()