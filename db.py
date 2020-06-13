import mysql.connector

con = mysql.connector.connect(host = "localhost", user="root", passwd="1234", database="feedback")
mycursor = con.cursor()

def user_login(tup):
    mycursor.execute("select * from user where username = %s and passwd = %s", tup)
    return (mycursor.fetchall())

def user_exist(tup):
    mycursor.execute("select * from user where username = %s",tup)
    return (mycursor.fetchall())

def email_exist(tup):
    mycursor.execute("select * from user where mail = %s ",tup)
    return (mycursor.fetchall())

def phone_exist(tup):
    mycursor.execute("select * from user where phone = %s", tup)
    return (mycursor.fetchall())