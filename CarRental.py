import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "andres1", database='carrental', auth_plugin='mysql_native_password')  
  
#printing the connection object   
print(myconn)  

mycursor = myconn.cursor()

# 1- Adding a new car to the fleet
sql = "INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("AB945IA", "Peugeot", "208", "negro", "2017", "2")
mycursor.execute(sql, val)

myconn.commit()

print(mycursor.rowcount, "record inserted.") 

# 2- Adding new Customer (no commas)
mycursor = myconn.cursor()

first_name, last_name, mobile, ssn, email, country = input("Enter Customer Data: ").split()
Cust = "INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES (%s, %s, %s, %s, %s, %s)"
CustVal = (first_name, last_name, mobile, ssn, email, country)
mycursor.execute (Cust, CustVal)
    
myconn.commit()

print(mycursor.rowcount, "record inserted.")

# 3- New Rental (no commas)
mycursor = myconn.cursor()

plate, cust_id, pick_date, return_date, amount = input("Please enter Plate Number, Customer ID, dates and amount: ").split()
Res = "INSERT INTO reservations (plate, cust_id, pick_date, return_date, amount) VALUES (%s, %s, %s, %s, %s)"
ResVal = (plate, cust_id, pick_date, return_date, amount)
mycursor.execute (Res, ResVal)

myconn.commit()

print (mycursor.rowcount, "record inserted.")


