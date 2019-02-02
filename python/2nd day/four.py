import pydb.connection as pydb

data = pydb.fetch("select * from student")

print(data)
