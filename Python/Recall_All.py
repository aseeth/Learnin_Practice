###Recall the all Basics###


#in python every thing is an object
#s = "hello"
#print(s.capitalize())
#print("hello".capitalize())

#Boolean
#print('a'>'Z')
print('ab' > 'b')
print(ord('a'),ord('Z')) #ord() method for find AASCI value
print(chr(97))           # chr() method for find charecter for that value




'''
list = [] #empty list
list1 = [30,40,60]
list = [1,2,3]
list.insert(0,10) #insert element by index
list.append(20)   #insert element at end of the list
list2=list+list1  #adding two lists
print(list2)'''       





#######connect MYSQL############

import mysql.connector
con = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    database = 'my_new_database',
)
mycur = con.cursor()
#mycur.execute("create database my_new_database")
#mycur.execute("create table student(name varchar(30), address varchar(255))")
#mycur.execute("create table customer(ID int auto_increment primary key,name varchar(40),address varchar(1000))")

# inserting single record
# mycur.execute("(insert into student(name,address) values('aseeth','rajahmundry')")
#mycur.execute("insert into student values('nani','kakinada')")
#con.commit()

'''
#inserting multiple records:

sql = "ame,addrinsert into customer(ness) values(%s,%s)"
val = [
    ('aseeth','rajahmundry'),
    ('mohan','srikakulam'),
    ('balu','vijayawada'),
    ('eswar','vijayanagaram'),
]
mycur.executemany(sql,val)
con.commit()'''

'''
#for select all records from customer table

mycur.execute("select * from customer")
cus_list = mycur.fetchall()
#cus_list = mycur.fetchone() #for only one record
for cus in cus_list:
    print(cus)'''

'''
#fetching required columns.

mycur.execute("select ID,address from customer")
cus_list = mycur.fetchall()
for col in cus_list:
    print(col)'''


#selecting records by using where clause.
'''
sql="select * from customer where name='Bhavi'"
mycur.execute(sql)
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''



#Escape query values by using the placholder %s method:
'''
sql = "select * from customer where address= %s"
add = ('eluru',)
mycur.execute(sql,add)
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''



#Python MySQL Order By, selecting records by order:
'''
sql = "select * from customer order by address"
mycur.execute(sql)
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''

#Python MySQL Order By desc, selecting records order by desc:
#this is reverse of above action.
'''
sql = "select * from customer order by name desc"
mycur.execute(sql)
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''


#Deleting record with where clause
'''
mycur.execute("delete from customer where name='aseeth'")
con.commit()
print(mycur.rowcount,"record deleted")'''


#upadate record
#ex:1
'''
sql = "update customer set name = 'john' where ID =2"
mycur.execute(sql)
con.commit()'''

#ex:2:
'''
sql = "update customer set name = %s where ID= %s"
val = ('mahesh',2)
mycur.execute(sql,val)
con.commit()'''

#Limit the Result, you can get required records by limit.
'''
mycur.execute("select * from customer limit 3")
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''

#Start from position 2, and return 4 records
'''
mycur.execute("select * from customer limit 4 offset 2")
cus_list= mycur.fetchall()
for rec in cus_list:
    print(rec)'''


#Joins in sql:
#Inner Join
#sql = "select * from customer inner join student on customer.ID = student.rollno"
#sql = "select * from customer left join student on customer.ID = student.rollno"
#sql = "select * from customer right join student on customer.ID = student.rollno"
#sql="select * from customer full outer join student on customer.ID = student.rollno"

###########if u want selected columns from both tables then try below quary###########
'''
sql="select customer.ID,student.name,student.address,customer.subject 
from customer inner join student on customer.ID = student.rollno;" '''

'''
mycur.execute(sql)
cus_rec = mycur.fetchall()
for rec in cus_rec:
    print(rec)'''
















