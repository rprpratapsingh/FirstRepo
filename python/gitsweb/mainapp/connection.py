import mysql.connector as mysql

def getConnection():
    db = mysql.connect(host="localhost",user="root",passwd="",database="pydb")
    return db

def exec(query):
    c = getConnection()
    cursor = c.cursor()
    cursor.execute(query)
    c.commit()
    c.close()

def fetch(query):
    c = getConnection()
    cursor = c.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data