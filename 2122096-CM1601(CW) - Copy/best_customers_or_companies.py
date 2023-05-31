def create_customer_list(sheet_3):
    'function to append all customer names with in a month to a list'
    max_row_3 = sheet_3.max_row
    customer_name = []
    for i in range(2,max_row_3+1):
        customer_name.append(sheet_3.cell(i,1).value)
    return customer_name

def create_company_list(sheet_4):
    'function to append all company names with in a month to a list'
    max_row_4 = sheet_4.max_row
    company_name = []
    for i in range(2,max_row_4+1):
        company_name.append(sheet_4.cell(i,1).value)
    return company_name

def make_a_dic_by_count_of_the_customers(customer_name):
    'function to covert the count of each customer names as a value and the customer names as keys into a dictionary'
    customer_dict = {}
    for i in customer_name:
        customer_dict[i] = customer_name.count(i)
    return customer_dict

def make_a_dic_by_count_of_the_companies(company_name):
    'function to covert the count of each company names as a value and the company names as keys into a dictionary'
    company_dict = {}
    for i in company_name:
        company_dict[i] = company_name.count(i)
    return company_dict

def find_best_customers(customer_dict):
    'function to find the best customers in descending order'
    # to create a key list using all keys(customer names) of customer_dict
    key_list = list(customer_dict.keys())
    # to create a value list using all values(customer count) of customer_dict
    value_list = list(customer_dict.values())
    # to create another list using values which counts are greater than 1
    cu_list = list(customer_dict.values())
    count = 0
    #for i in range(len(cu_list)):
        #if cu_list[i] == 1:
            #cu_list.pop(i)
            #i = i
    while count < len(cu_list):
        if cu_list[count] == 1:
            cu_list.pop(count)
            count = count
        else:
            count += 1
    # to make customer counts in descending order
    for i in range(1, len(cu_list)):
        for j in range(0, len(cu_list) - 1):
            value_to_sort = cu_list[i]
            while cu_list[i - 1] < value_to_sort and i > 0:
                cu_list[i], cu_list[i - 1] = cu_list[i - 1], cu_list[i]
                i = i - 1
    # to print best customers in descending order
    if len(cu_list) == 0:
        print('There is no any best customers during this month')
    else:
        for i in range(len(cu_list)):
            print(key_list[value_list.index(cu_list[i])])

def find_best_companies(company_dict):
    'function to find the best companies in descending order'
    # to create a key list using all keys(company names) of company_dict
    key_list = list(company_dict.keys())
    # to create a value list using all values(company count) of company_dict
    value_list = list(company_dict.values())
    # to create another list using values which counts are greater than 1
    comp_list = list(company_dict.values())
    count = 0
    #for i in range(len(comp_list)):
        #if comp_list[i] == 1:
            #comp_list.pop(i)
            #i = i
    while count < len(comp_list):
        if comp_list[count] == 1:
            comp_list.pop(count)
            count = count
        else:
            count += 1
    # to make company counts in descending order
    for i in range(1, len(comp_list)):
        for j in range(0, len(comp_list) - 1):
            value_to_sort = comp_list[i]
            while comp_list[i - 1] < value_to_sort and i > 0:
                comp_list[i], comp_list[i - 1] = comp_list[i - 1], comp_list[i]
                i = i - 1
    # to print best companies in descending order
    if len(comp_list) == 0:
        print('There is no any best companies during this month')
    else:
        for i in range(len(comp_list)):
            print(key_list[value_list.index(comp_list[i])])