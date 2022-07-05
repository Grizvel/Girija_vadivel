
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="miyagirija@01",database="employee_db")
if con:
    print("MySQL database connected successfully")
else:
    print("connection error")

def insert (name, age, city):
    res = con.cursor()
    sql = "Insert into users(name, age, city) values (%s,%s,%s)"
    user = (name, age, city)
    con.commit()
    print("Data Inserted successfully")

def update(name, age, city, id):
    res = con.cursor()
    sql = "Update users set name=%s, age=%s, city=%s, where id=%s"
    user = (name, age, city, id)
    con.commit()
    print("Data Updated successfully")

def select():
    res = con.cursor()
    sql = "SELECT * from employee_db"
    #res.excecute(sql)
    #result=res.fetchall()
    print(res)

def delete():
    res = con.cursor()
    sql = "Delete from users where id=%s"
    user = (id)
    con.commit()
    print("Data delete success")

while True:
    print("1.Insert data")
    print("2.Update data")
    print("3.Select data")
    print("4.Delete data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        name = input("Enter name : ")
        age = input("Enter age : ")
        city = input("Enter city : ")
        insert(name, age, city)
    elif choice == 2:
        id = input("Enter id  : ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        update(name, age, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter the id to delete : ")
        delete()
    elif choice == 5:
        print("Thank you")
    else:
        print("Invalid selection, please try again")



