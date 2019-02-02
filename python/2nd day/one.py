import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",passwd="",database="pydb")
cursor = db.cursor()
insert1 = "INSERT INTO student(roll,name,age,marks) VALUES(1, 'Rudra', 21, 80.0 )"
cursor.execute(insert1)
db.commit()
db.close()