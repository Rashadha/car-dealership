

def create_a_list_with_number_of_sold_cars(number_of_sold_cars,num_of_sold_car_list):
    'function to create a list with numbers of cars sold with in last six months'
    #num_of_sold_car_list = []
    num_of_sold_car_list.append(number_of_sold_cars)
    return num_of_sold_car_list

def find_total_income_by_selling_car(sheet_3,sheet_4,customer_sold_price,company_sold_price):
    'function to find total income by selling car of each month'
    #customer_sold_price = []
    #company_sold_price = []
    total_customer_sold_price = 0
    total_company_sold_price = 0
    max_row_3 = sheet_3.max_row
    max_row_4 = sheet_4.max_row
    # to create a list with all sold prices to customers
    for i in range(2,max_row_3+1):
        customer_sold_price.append(sheet_3.cell(i,11).value)
    # to create a list with all sold prices to companies
    for i in range(2,max_row_4+1):
        company_sold_price.append(sheet_4.cell(i,11).value)
    # to add all customers sold prices together
    for i in range(len(customer_sold_price)):
        total_customer_sold_price += customer_sold_price[i]
    # to add all companies sold prices together
    for i in range(len(company_sold_price)):
        total_company_sold_price += company_sold_price[i]
    # to find total income by selling car
    total_income_sell_car = total_customer_sold_price + total_company_sold_price
    return total_income_sell_car

def find_total_income_by_maintenance(sheet_5,maintenance_cost_list):
    'function to find total income by maintenance for each month'
    #maintenance_cost_list = []
    max_row_5 = sheet_5.max_row
    total_maintenance_cost = 0
    # to create maintenance cost list
    for i in range(2,max_row_5+1):
        maintenance_cost_list.append(sheet_5.cell(i,5).value)
    # to add all maintenance costs all together
    for i in range(len(maintenance_cost_list)):
        if maintenance_cost_list[i] != None:
            total_maintenance_cost += maintenance_cost_list[i]
    return total_maintenance_cost

def create_total_income_list(total_income,total_income_list):
    'function to create a total income list'
    #total_income_list = []
    total_income_list.append(total_income)
    return total_income_list

def generate_graph_for_the_sold_cars(num_of_sold_car_list):
    'function to generate total number of cars sold for the last 6 months'
    import pandas as pd
    plotdata = pd.DataFrame({
        "total_sold_car":num_of_sold_car_list
    },
    index=["September 2021","October2021","November 2021","December 2021","January 2022","February 2022"]
    )
    axis = plotdata.plot(kind='bar')
    axis.set_title("Total number of cars sold for the last six months")
    axis.set_xlabel("Months")
    axis.set_ylabel("Number of cars")

def generate_graph_for_the_total_income(total_income_list):
    'function to generate total income for the last 6 months'
    import pandas as pd
    plotdata = pd.DataFrame({
        "total_income":total_income_list
    },
    index=["September 2021","October2021","November 2021","December 2021","January 2022","February 2022"]
    )
    axis = plotdata.plot(kind='bar')
    axis.set_title("Total income for the last six months")
    axis.set_xlabel("Months")
    axis.set_ylabel("Total income")
