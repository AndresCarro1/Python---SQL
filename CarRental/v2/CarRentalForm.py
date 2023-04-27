import mysql.connector
import storage
from tabulate import tabulate

db_connection = storage.connect()
print(db_connection)  

mycursor = db_connection.cursor()

def read(x):

    mycursor.execute(x)

    myresult = mycursor.fetchall()

    print (tabulate(myresult))


def update(table_name, column_name, new_value, where_column, where_value):

    sql = f"UPDATE {table_name} SET {column_name} = %s WHERE {where_column} = %s"
    val = (new_value, where_value)

    mycursor.execute(sql, val)

    db_connection.commit()

    if mycursor.rowcount >= 1:
        print(mycursor.rowcount, "record(s) updated.")
    else:
        print("Could not update, please enter a valid ID or plate number.")

def delete(table_namex, where_columnx, del_value):

    sql = f"DELETE FROM {table_namex} WHERE {where_columnx} = %s"
    val = (del_value,) 

    mycursor.execute(sql, val)

    db_connection.commit()

    if mycursor.rowcount >= 1:
        print(mycursor.rowcount, "record(s) updated.")
    else:
        print("Could not update, please enter a valid ID or plate number.")

def new_vehicle():

    plate, brand, model, color, man_year, cat_id = input("Please enter plate number, brand, model, color, manufacture year and category: ").split()
    Car = "INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
    CarVal = (plate, brand, model, color, man_year, cat_id)
    mycursor.execute(Car, CarVal)

    db_connection.commit()

    print(mycursor.rowcount, "record inserted.") 

def new_customer():

    first_name, last_name, mobile, ssn, email, country = input("Please enter first name, last name, mobile, ssn, email and country of origin: ").split()
    Cust = "INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES (%s, %s, %s, %s, %s, %s)"
    CustVal = (first_name, last_name, mobile, ssn, email, country)
    mycursor.execute (Cust, CustVal)
    
    db_connection.commit()

    print(mycursor.rowcount, "record inserted.")

def new_reservation():

    plate, cust_id, pick_date, return_date, amount = input("Please enter Plate Number, Customer ID, dates and amount: ").split()
    Res = "INSERT INTO reservations (plate, cust_id, pick_date, return_date, amount) VALUES (%s, %s, %s, %s, %s)"
    ResVal = (plate, cust_id, pick_date, return_date, amount)
    mycursor.execute (Res, ResVal)

    db_connection.commit()

    print (mycursor.rowcount, "record inserted.")