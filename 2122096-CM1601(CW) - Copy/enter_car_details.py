def write_record_number (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add car reference numbers on CarDealership.xlsx'
    for i in range(len(number_list)):
        sheet.cell(row=max_row+(i+1),column=1,value=number_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_make(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)

def write_record_make (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add car make on CarDealership.xlsx'
    for i in range(len(make_list)):
        sheet.cell(row=max_row+(i+1),column=2,value=make_list[i])

        workbook.save('CarDealership.xlsx')
        write_record_model(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)



def write_record_model (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add car model on CarDealership.xlsx'
    for i in range(len(model_list)):
        sheet.cell(row=max_row+(i+1),column=3,value=model_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_year(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)

def write_record_year (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add car model year on CarDealership.xlsx'
    for i in range(len(year_list)):
        sheet.cell(row=max_row+(i+1),column=4,value=year_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_mileage(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)



def write_record_mileage (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add mileage on CarDealership.xlsx'
    for i in range(len(mileage_list)):
        sheet.cell(row=max_row+(i+1),column=5,value=mileage_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_owner_info(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)


def write_record_owner_info (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add owner information such as 1st owner, 2nd owner, etc. on CarDealership.xlsx'
    for i in range(len(owner_info_list)):
        sheet.cell(row=max_row+(i+1),column=6,value=owner_info_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_ask_price(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)



def write_record_ask_price (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add the bought price of the car model on CarDealership.xlsx'
    for i in range(len(ask_price_list)):
        sheet.cell(row=max_row+(i+1),column=7,value=ask_price_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_sell_price(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)



def write_record_sell_price (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add the selling price of the car model on CarDealership.xlsx'
    for i in range(len(sell_price_list)):
        sheet.cell(row=max_row+(i+1),column=8,value=sell_price_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_car_status(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list)


def write_record_car_status (max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add is the car sold or not on CarDealership.xlsx'
    for i in range(len(car_status_list)):
        sheet.cell(row=max_row+(i+1),column=9,value=car_status_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_last_price_status(max_row, workbook, sheet, number_list, make_list, model_list, year_list,
                                       mileage_list, owner_info_list, ask_price_list, sell_price_list, car_status_list,
                                       last_price_status_list, last_price_list)

def write_record_last_price_status(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add is the car model under negotiations or not on CarDealership.xlsx'
    for i in range(len(last_price_status_list)):
        sheet.cell(row=max_row+(i+1),column=10,value=last_price_status_list[i])
        workbook.save('CarDealership.xlsx')
        write_record_last_price(max_row, workbook, sheet, number_list, make_list, model_list, year_list, mileage_list,
                                owner_info_list, ask_price_list, sell_price_list, car_status_list,
                                last_price_status_list, last_price_list)

def write_record_last_price(max_row,workbook,sheet,number_list,make_list,model_list,year_list,mileage_list,owner_info_list,ask_price_list,sell_price_list,car_status_list,last_price_status_list,last_price_list):
    'function to add the last selling price on CarDealership.xlsx'
    for i in range(len(last_price_list)):
        sheet.cell(row=max_row+(i+1),column=11,value=last_price_list[i])
        workbook.save('CarDealership.xlsx')



