import mysql.connector  
  
#Create the connection object   
myconn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "andres1", database='carrental', auth_plugin='mysql_native_password')  
  
#printing the connection object   
print(myconn)  

mycursor = myconn.cursor()

#Adding a new car to the fleet
sql = "INSERT INTO vehicles (plate, brand, model, color, man_year, cat_id) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("AB945IA", "Peugeot", "208", "negro", "2017", "2")
mycursor.execute(sql, val)

myconn.commit()

print(mycursor.rowcount, "record inserted.")

#Adding new Customer
mycursor = myconn.cursor()

first_name, last_name, mobile, ssn, email, country = input("Enter Customer Data: ").split()
Cust = "INSERT INTO customers (first_name, last_name, mobile, ssn, email, country) VALUES (%s, %s, %s, %s, %s, %s)"
CustVal = (first_name, last_name, mobile, ssn, email, country)
mycursor.execute(Cust, CustVal)
    
myconn.commit()

print(mycursor.rowcount, "record inserted.")



