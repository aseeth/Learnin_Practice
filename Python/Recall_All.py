###Recall all Basics###


#in python every thing is an object
#s = "hello"
#print(s.capitalize())
#print("hello".capitalize())

'''
#Boolean
print('a'>'Z')
print('ab' > 'b')
print(ord('a'),ord('Z')) #ord() method for find AASCI value
print(chr(97))           # chr() method for find charecter for that value'''


########COLLECTIONS IN PYTHON##############
####1)LIST######

'''
list = [] #empty list
list1 = [30,40,60]
list = [1,2,3]
list.insert(0,10) #insert element by index
list.append(20)   #insert element at end of the list
list2=list+list1  #adding two lists
print(list2)'''       

list1 = [30,40,60,70,80]
#list1.remove(30)   #removing an element by element_value
#list1.pop()         #removes the last element.
#list1.pop(1)       #removes element by index.
#print(list1)




#######2)Tuple#########
#Tuples: orderd, immutable allows duplicate elements

'''
my_tuple = ('a','s','e','n','n')
my_list = (list(my_tuple))  #converting tuple to list.
my_tuple = tuple(my_list)   #coverting list to tuple
print(my_tuple)'''

'''
a = (1,2,3,4,5,6,7)         #it supports slicing
b = a[2:5:2]
print(b)'''


#tuple packing
'''
my_tuple = ('aseeth',26,'kkd')
name,age,city = my_tuple       #Here num of values must matched with tuple
print(name)
print(age)
print(city)'''


'''
my_tuple = (0,1,2,3,4)
i1, *i2 , i3 = my_tuple     #here remaining elemnets grouped as a list and stored into the *i2 variable.
print(i1)
print(i2)
#print(i3)'''


'''
import sys
my_tuple=(0,1,2,"aseeth",True)      #so here tuple less memory utilization than list to store same elements
my_list=[0,1,2,"aseeth",True]
print(sys.getsizeof(my_tuple),"bytes")  #80 bytes
print(sys.getsizeof(my_list),"bytes")   #120 bytes'''


'''
import timeit                       #so here tuple take less time to execute iterations than a list
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000)) #o/p: 0.024986399999999992
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000)) #o/p: 0.15797499999999998'''


##############################
########DICTIONARIES##########
##############################

#Key-value pairs, unorder, Mutable

#mydict1 = {'name':'aseeth','age':'26', 'city':'kkd'} #case1:   create a dictionary 

#mydict2 = dict(name='aseeth',age='26', city='kkd')  #case2:    create a dictionary
#print(mydict2)

#values = mydict1["name"]                   #to get the values

#mydict1["email"]="aseeth@gmail.com"        #add the key value to dictionary
#mydict1["email"]="aseeth_nani@gmail.com"   #overide the value, when add different value to existin key


#del mydict1['name']                        #to delete particular key value
#mydict1.pop('age')                         #same as delete
#mydict1.popitem()                          #It deletes the last pair



######Tocheck wheather key and value available or not
'''
try:
    print(mydict1["lastname"])
except:
    print("Error")'''


#######get all keys or values or both######
'''
for key,value in mydict1.items():
    print(key,value)

for keys in mydict1.keys():
    print(keys)

for value in mydict1.values():
    print(value)'''



##########copy the dictionary#######
#mydict1_cpy = mydict1              #this is assignment if change one dict it effects other dict
#mydict1_cpy = mydict1.copy()       #this copy creates seperate dict objects that's not effect another
#mydict1_cpy = dict(mydict1)         # same as above we can do with dict() function..not effect another
#mydict1_cpy['color']="brown"



############merge two dictionaris#######
'''
mydict1 = {'name':'aseeth','age':'26', 'city':'kkd'}
mydict2 = {'addres':'1-111','street':'temple street'}
mydict1.update(mydict2)                #merge two dictrionaries using update() function.
print(mydict1)'''


##########tuple can use keys in dictionary not list######
'''
my_list = [4,5]
my_tuple = (4,6)
mydict = {my_tuple:10}           #its possible
#mydict = {my_list:10}           #its not possible, Type error:unhashable
print(mydict)'''



######################################
##########Sets#######################
####################################
#Sets: unordered, mutable, no dublicates
myset = {1,2,3,}
myset.add(4)        #insert single elemnt into a set
myset.remove(2)     #to delete an element

print(myset)














#######connect MYSQL############
'''
import mysql.connector
con = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    database = 'my_new_database',
)
mycur = con.cursor()'''
#mycur.execute("create database my_new_database")
#mycur.execute("create table student(name varchar(30), address varchar(255))")
#mycur.execute("create table customer(ID int auto_increment primary key,name varchar(40),address varchar(1000))")

# inserting single record
# mycur.execute("(insert into student(name,address) values('aseeth','rajahmundry')")
#mycur.execute("insert into student values('nani','kakinada')")
#con.commit()

'''
#inserting multiple records:

sql = "insert into customer(name,address) values(%s,%s)"
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
















