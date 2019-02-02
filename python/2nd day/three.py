import pydb.connection as pydb

roll = int(input("Enter your Roll Number"))
name = input("Enter your Name")
age = int(input("Enter your Age"))
marks = float(input("Enter your marks"))
insert1 = "INSERT INTO student VALUES({0}, '{1}', {2}, {3})".format(roll,name,age,marks)

pydb.exec(insert1)