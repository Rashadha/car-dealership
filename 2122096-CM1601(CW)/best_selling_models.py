def refer_month(month,workbook):
    if month == 1:
        sheet = workbook['2022JAN']

    if month == 2:
        sheet = workbook['2022FEB']

    if month == 3:
        sheet = workbook['2022MARCH']

    if month == 4:
        sheet = workbook['2022APRIL']

    if month == 5:
        sheet = workbook['2022MAY']

    if month == 6:
        sheet = workbook['2022JUNE']

    if month == 7:
        sheet = workbook['2021JULY']

    if month == 8:
        sheet = workbook['2021AUG']

    if month == 9:
        sheet = workbook['2021SEP']

    if month == 10:
        sheet = workbook['2021OCT']

    if month == 11:
        sheet = workbook['2021NOV']

    if month == 12:
        sheet = workbook['2021DEC']
    return sheet

def append_models_to_a_list(max_row,sheet):
    'function to append models to a list according to each month'
    model_list = []
    for i in range(2,max_row+1):
        model_list.append(sheet.cell(i,3).value)
    return model_list

def make_a_dic_by_count_of_the_models(model_list):
    'function to covert the count of each models as a value and the models as keys into a dictionary'
    model_dict = {}
    for i in model_list:
        model_dict[i] = model_list.count(i)
    return model_dict

def print_best_five_selling_models_of_a_month(model_dict):
    'function to print best five selling models of a month'
    # to convert keys in the model_dict to a list
    key_list = list(model_dict.keys())
    # to convert values in the model_dict to a list
    value_list = list(model_dict.values())
    # another list for values
    mo_list = list(model_dict.values())
    # to sort values in descending order
    for i in range(1, len(mo_list)):
        for j in range(0,len(mo_list)-1):
            value_to_sort = mo_list[i]
            while mo_list[i-1] < value_to_sort and i > 0:
                mo_list[i], mo_list[i-1] = mo_list[i-1], mo_list[i]
                i -= 1
    # to print best five selling models for a month
    for i in range(5):
        print(key_list[value_list.index(mo_list[i])], end = '   ')
