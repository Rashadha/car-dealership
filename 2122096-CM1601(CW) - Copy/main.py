import sort

print('If you are the admin --> press 1\nif you are the owner --> press 2\nif you are the technician --> press 3\nif you are a customer --> press 4')
option = sort.enter_first_option()
password = ''
if option == 1:
    while not(password == 'AD6@12BC'):
        try:
            password = str(input('Enter your password: '))
            if not(password == 'AD6@12BC'):
                raise TypeError ('Your password is incorrect')
        except TypeError as e:
            print(e)
    print('If you want to add car details --> press 1\nif you want to update or delete records --> press 2\nif you want to add test drive appointments --> press 3\nif you want to add customer or company details --> press 4')
    option = sort.enter_first_option()
    if option == 1:
        import admin_main

        admin_main
    elif option == 2:
        import admin_main_2

        admin_main_2
    elif option == 3:
        import add_appointment_main

        add_appointment_main
    else:
        import enter_sold_details_main

        enter_sold_details_main
elif option == 2:
    while not(password == 'OW1#$3BC'):
        try:
            password = str(input('Enter your password: '))
            if not(len(password) == 8 and password[6:8] == 'BC' and password[0:2] == 'OW'):
                raise TypeError ('Your password is incorrect')
        except TypeError as e:
            print(e)
    import owner_main
    owner_main
elif option == 3:
    while not(len(password) == 8 and password[6:8] == 'BC' and password[0:3] == 'TEC'):
        try:
            password = str(input('Enter your password: '))
            if not(len(password) == 8 and password[6:8] == 'BC' and password[0:3] == 'TEC'):
                raise TypeError ('Your password is incorrect')
        except TypeError as e:
            print(e)
    import technician_main

    technician_main
else:
    import customer_main

    customer_main





