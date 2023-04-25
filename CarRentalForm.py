import mysql.connector
import storage
from tabulate import tabulate

myconn = storage.connect()
print(myconn)  

mycursor = myconn.cursor()

def checker(x):
    
    mycursor = myconn.cursor()

    CarCheck = x
    mycursor.execute(CarCheck)

    myresult = mycursor.fetchall()

    print (tabulate(myresult))


def updater(table_name, column_name, new_value, where_column, where_value):

    mycursor = myconn.cursor()

    sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {where_column} = %s"
    val = (new_value, where_value)

    mycursor.execute(sql, val)

    myconn.commit()

    print(mycursor.rowcount, "record(s) updated.")

def deleter(table_namex, where_columnx, del_value):

    mycursor = myconn.cursor()

    sql = f"DELETE FROM {table_namex} WHERE {where_columnx} = %s"
    val = (del_value,) 

    mycursor.execute(sql, val)

    myconn.commit()

    print(mycursor.rowcount, "record(s) deleted.")

def new_vehicle():

    plate, brand, model, color, man_year, cat_id = input("Please enter plate number, brand, model, color, manufacture year and category: ").split()
    Car = "INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
    CarVal = (plate, brand, model, color, man_year, cat_id)
    mycursor.execute(Car, CarVal)

    myconn.commit()

    print(mycursor.rowcount, "record inserted.") 

def new_customer():

    mycursor = myconn.cursor()

    first_name, last_name, mobile, ssn, email, country = input("Please enter first name, last name, mobile, ssn, email and country of origin: ").split()
    Cust = "INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES (%s, %s, %s, %s, %s, %s)"
    CustVal = (first_name, last_name, mobile, ssn, email, country)
    mycursor.execute (Cust, CustVal)
    
    myconn.commit()

    print(mycursor.rowcount, "record inserted.")

def new_reservation():

    mycursor = myconn.cursor()

    plate, cust_id, pick_date, return_date, amount = input("Please enter Plate Number, Customer ID, dates and amount: ").split()
    Res = "INSERT INTO reservations (plate, cust_id, pick_date, return_date, amount) VALUES (%s, %s, %s, %s, %s)"
    ResVal = (plate, cust_id, pick_date, return_date, amount)
    mycursor.execute (Res, ResVal)

    myconn.commit()

    print (mycursor.rowcount, "record inserted.")