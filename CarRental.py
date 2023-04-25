import mysql.connector
from tabulate import tabulate
from CarRentalForm import checker
from CarRentalForm import updater
from CarRentalForm import new_car
from CarRentalForm import new_customer
from CarRentalForm import new_reservation


def rental():

    #Create the connection object   
    myconn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "andres1", database='carrental', auth_plugin='mysql_native_password')  

    print(myconn)  

    mycursor = myconn.cursor()

    print('1) Create registers')
    print('2) Read registers')
    print('3) Update registers')
    print('4) Delete registers')
       
    while True:
        try:
            option = int(input('Please select your operation.'))
            break
        except:
            print("It must be a number, from 1 to 4")
    
    if option == 1:

        print('1) Add new Car')
        print('2) Add new Customer')
        print('3) Add new Rental')

        while True:
            try:
                option = int(input('Please select your operation.'))
                if option < 1 or option > 3:
                    print ("Not a valid option, please try again.")
                else:
                    break
            except ValueError:
                 print("It must be a number, from 1 to 3")

        if option == 1: #Adding new car to the fleet

            new_car()

        elif option == 2: #Adding new customer

            new_customer()

        elif option == 3: #Adding new reservation

            new_reservation()
            
    elif option == 2:

        print('1) Check vehicles')
        print('2) Check customers')
        print('3) Check reservations')

        while True:
            try:
                option = int(input('Please select your operation.'))
                break
            except:
                print("It must be a number, from 1 to 3")
            
        if option == 1:
            
            checker ("SELECT * FROM vehicles ORDER BY cat_id")

        if option == 2:
          
            checker ("SELECT * FROM customers ORDER BY last_name")
            
        if option == 3:
           
            checker ("SELECT * FROM reservations ORDER BY pick_date DESC")

        elif option < 1 or option > 3:

            print ("Not a valid option, please try again.")
    
    elif option == 3:
   
        table_name = input ("What do you want to modify?: ")
        column_name = input("Which column would you like to modify?: ")
        new_value = input("Please enter the new value: ")
        where_column = input("Please select the parameter to identify the vehicle or person: ")
        where_value = input("Please identify the vehicle or person: ")

        updater(table_name, column_name, new_value, where_column, where_value)

    elif option == 4:

        table_namex = input ("What do you want to delete?: ")
        where_columnx = input ("Choose delete criteria: ")
        del_value = input ("Please input what to delete: ")

        deleter(table_namex, where_columnx, del_value)

rental()

# mycursor.close()
# myconn.close()