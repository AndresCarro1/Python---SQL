import mysql.connector
from tabulate import tabulate
from CarRentalForm import read
from CarRentalForm import update
from CarRentalForm import delete
from CarRentalForm import new_vehicle
from CarRentalForm import new_customer
from CarRentalForm import new_reservation
import storage


def rental():

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

            read ("SELECT * FROM reservations ORDER BY pick_date DESC")

        elif option == 3: #Modifing reservations

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the reservation's ID number: ")

            update('reservations', column_name, new_value, 'reservation_id', where_value)

            read ("SELECT * FROM reservations ORDER BY pick_date DESC")
        
        elif option == 4: #Deleting reservations

            del_value = input ("Please enter the reservation's ID number: ")

            delete('reservations', 'reservation_id', del_value)

            read ("SELECT * FROM reservations ORDER BY pick_date DESC")
                
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
          
            read ("SELECT * FROM customers ORDER BY last_name")
            
        elif option == 3:

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the customers's ID number: ")

            update('customers', column_name, new_value, 'cust_id', where_value)

            read ("SELECT * FROM customers ORDER BY last_name")
           
        elif option == 4:

            del_value = input ("Please enter the customer's ID number: ")

            delete('customers', 'cust_id', del_value)

            read ("SELECT * FROM customers ORDER BY last_name")
   
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
          
            read ("SELECT * FROM vehicles ORDER BY plate")
            
        elif option == 3:

            column_name = input("Which column would you like to modify?: ")
            new_value = input("Please enter the new value: ")
            where_value = input("Please enter the vehicle's plate number: ")

            update('vehicles', column_name, new_value, 'plate', where_value)

            read("SELECT * FROM vehicles ORDER BY plate")

        elif option == 4:

            del_value = input ("Please enter the vehicle's plate number: ")

            delete('vehicles', 'plate', del_value)

            read("SELECT * FROM vehicles ORDER BY plate")

while True:
    rental()
    response = input("Do you want to run the program again? (y/n): ")
    if response.lower() != "y":
        print("Have a nice day!")
        break

# mycursor.close()
# db_connection.close()