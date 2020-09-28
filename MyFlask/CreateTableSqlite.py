# import sqlite3 as sql
# conn= sql.connect("database.db")
# print("connection Successful")
# # conn.execute("CREATE TABLE students(name TEXT,addr TEXT,City TEXT, Pincode TEXT)")
# # print("Table Successfully Created")
# # conn.close()

#
# import sqlite3 as sql
# conn= sql.connect("students.sqlite3")
# print("connection Successful")
# conn.execute("CREATE TABLE students(student_id Integer PRIMARY_KEY,name TEXT,addr TEXT,City TEXT, pin TEXT)")
# print("Table Successfully Created")
# conn.close()


import sqlite3 as sql
conn= sql.connect("students.sqlite3")
print("connection Successful")
result=conn.execute("select * from students")
for res in result:
    print(res)
