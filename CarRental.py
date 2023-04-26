import mysql.connector
from tabulate import tabulate
from CarRentalForm import checker
from CarRentalForm import updater
from CarRentalForm import deleter
from CarRentalForm import new_vehicle
from CarRentalForm import new_customer
from CarRentalForm import new_reservation
import storage


def rental():

    #Create the connection object   
    myconn = storage.connect()

    mycursor = myconn.cursor()

    print('1) Rentals')
    print('2) Customers')
    print('3) Vehicles')   
    
    while True:
        try:
            option = int(input('Please select your operation.'))
            break
        except:
            print("It must be a number, from 1 to 3")
    
    if option == 1:

        print('1) Add new Rental')
        print('2) View Rentals')
        print('3) Modify Rental')
        print('4) Delete Rental')

        while True:
            try:
                option = int(input('Please select your operation.'))
                if option < 1 or option > 4:
                    print ("Not a valid option, please try again.")
                else:
                    break
            except ValueError:
                 print("It must be a number, from 1 to 4")

        if option == 1: #Adding new reservation

            new_reservation()

        elif option == 2: #Viewing reservations

            checker ("SELECT * FROM reservations ORDER BY pick_date DESC")

        elif option == 3: #Modifing reservations

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the reservation's ID number: ")

            updater('reservations', column_name, new_value, 'reservation_id', where_value)

            checker ("SELECT * FROM reservations ORDER BY pick_date DESC")
        
        elif option == 4: #Deleting reservations

            table_namex = 'reservations'
            where_columnx = 'reservation_id'
            del_value = input ("Please enter the reservation's ID number: ")

            deleter('reservations', 'reservation_id', del_value)

            checker ("SELECT * FROM reservations ORDER BY pick_date DESC")

         
    elif option == 2:

        print('1) Add new Customer')
        print('2) View Customers')
        print('3) Modify Customer')
        print('4) Delete Customer')

        while True:
            try:
                option = int(input('Please select your operation.'))
                break
            except:
                print("It must be a number, from 1 to 4")
            
        if option == 1:
            
            new_customer()

        elif option == 2:
          
            checker ("SELECT * FROM customers ORDER BY last_name")
            
        elif option == 3:

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the customers's ID number: ")

            updater('customers', column_name, new_value, 'cust_id', where_value)

            checker ("SELECT * FROM customers ORDER BY last_name")
           
        elif option == 4:

            table_namex = 'customers'
            where_columnx = 'cust_id'
            del_value = input ("Please enter the customer's ID number: ")

            deleter('customers', 'cust_id', del_value)

            checker ("SELECT * FROM customers ORDER BY last_name")
   
    elif option == 3:
   
        print('1) Add new Vehicle')
        print('2) View Vehicles')
        print('3) Modify Vehicle')
        print('4) Delete Vehicle')

        while True:
            try:
                option = int(input('Please select your operation.'))
                break
            except:
                print("It must be a number, from 1 to 4")
            
        if option == 1:
            
            new_vehicle()

        elif option == 2:
          
            checker ("SELECT * FROM vehicles ORDER BY plate")
            
        elif option == 3:

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the vehicle's plate number: ")

            updater('vehicles', column_name, new_value, 'plate', where_value)

            checker("SELECT * FROM vehicles ORDER BY plate")

        elif option == 4:

            del_value = input ("Please enter the vehicle's plate number: ")

            deleter('vehicles', 'plate', del_value)

            checker("SELECT * FROM vehicles ORDER BY plate")

while True:
    rental()
    response = input("Do you want to run the program again? (y/n): ")
    if response.lower() != "y":
        break

# mycursor.close()
# myconn.close()