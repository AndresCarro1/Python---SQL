import mysql.connector  

def rental():

    #Create the connection object   
    myconn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "andres1", database='carrental', auth_plugin='mysql_native_password')  

    print(myconn)  

    mycursor = myconn.cursor()

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

rental()





    



