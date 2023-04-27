import mysql.connector
from tabulate import tabulate  

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
                break
            except:
                print("It must be a number, from 1 to 3")

        if option == 1: #Adding new car to the fleet

            mycursor = myconn.cursor()

            plate, brand, model, color, man_year, cat_id = input("Please enter plate number, brand, model, color, manufacture year and category: ").split()
            Car = "INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
            CarVal = (plate, brand, model, color, man_year, cat_id)
            mycursor.execute(Car, CarVal)

            myconn.commit()

            print(mycursor.rowcount, "record inserted.") 
    
        if option == 2: #Adding new customer

            mycursor = myconn.cursor()

            first_name, last_name, mobile, ssn, email, country = input("Please enter first name, last name, mobile, ssn, email and country of origin: ").split()
            Cust = "INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES (%s, %s, %s, %s, %s, %s)"
            CustVal = (first_name, last_name, mobile, ssn, email, country)
            mycursor.execute (Cust, CustVal)
    
            myconn.commit()

            print(mycursor.rowcount, "record inserted.")

        if option == 3: #Adding new reservation

            mycursor = myconn.cursor()

            plate, cust_id, pick_date, return_date, amount = input("Please enter Plate Number, Customer ID, dates and amount: ").split()
            Res = "INSERT INTO reservations (plate, cust_id, pick_date, return_date, amount) VALUES (%s, %s, %s, %s, %s)"
            ResVal = (plate, cust_id, pick_date, return_date, amount)
            mycursor.execute (Res, ResVal)

            myconn.commit()

            print (mycursor.rowcount, "record inserted.")

        elif option < 1 or option > 3:

            print ("Not a valid option, please try again.")

    if option == 2:

        print('1) Check vehicles')
        print('2) Check customers')
        print('3) Check reservations')

        while True:
            try:
                option = int(input('Please select your operation.'))
                break
            except:
                print("It must be a number, from 1 to 3")

        def read(x):
            
            CarCheck = x
            mycursor.execute(CarCheck)

            myresult = mycursor.fetchall()

            print (tabulate(myresult))
            
        if option == 1:
            
            mycursor = myconn.cursor()
            
            read ("SELECT * FROM vehicles ORDER BY cat_id")

        if option == 2:
          
            read ("SELECT * FROM customers ORDER BY last_name")
            
        if option == 3:
           
            Checker ("SELECT * FROM reservations ORDER BY pick_date DESC")

        elif option < 1 or option > 3:

            print ("Not a valid option, please try again.")
    
    if option == 3:

        def Updater(table_name, column_name, new_value, where_column, where_value):

                mycursor = myconn.cursor()

                sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {where_column} = %s"
                val = (new_value, where_value)

                mycursor.execute(sql, val)

                myconn.commit()

                print(mycursor.rowcount, "record(s) updated.")
   
        table_name = input ("What do you want to modify?: ")
        column_name = input("Which column would you like to modify?: ")
        new_value = input("Please enter the new value: ")
        where_column = input("Please select the parameter to identify the vehicle or person: ")
        where_value = input("Please identify the vehicle or person: ")

        Updater(table_name, column_name, new_value, where_column, where_value)

    if option == 4:

        def Deleter(table_namex, where_columnx, del_value):

                mycursor = myconn.cursor()

                sql = f"DELETE FROM {table_namex} WHERE {where_columnx} = %s"
                val = (del_value,) 

                mycursor.execute(sql, val)

                myconn.commit()

                print(mycursor.rowcount, "record(s) deleted.")

        table_namex = input ("What do you want to delete?: ")
        where_columnx = input ("Choose delete criteria: ")
        del_value = input ("Please input what to delete: ")

        Deleter(table_namex, where_columnx, del_value)

rental()