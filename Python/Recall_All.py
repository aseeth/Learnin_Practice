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
list.extend(list1) #extends the list with another list
list2=list+list1  #adding two lists
print(list2)'''       

#list1 = [30,40,60,70,80]
#list1.remove(30)   #removing an element by element_value
#list1.pop()         #removes the last element.
#list1.pop(1)       #removes element by index.
#del list1[2]       #delete an element by its index
#del list1          #for delete complete list
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
##########Sets########################
######################################

#Sets: unordered, mutable, no dublicates
#myset = {1,2,3,}
#myset.add(4)        #insert single elemnt into a set
#myset.remove(5)    #to delete an element by element_value, here if element not in set,it raises KeyError.
#myset.discard(5)    #to delete an element by element_value, here if element not in set,it can't raise error.
#print(myset.pop())  #to delete a arbitary element and returns deleted elemtn.
#print(myset)

'''
###unioun,intersection
odds = {1,3,5,7,9}
even = {2,4,6,8}
primes ={2,3,5,7}

#u = odds.union(even)               #it returns all elements present in two sets.
#print(u)
#i = odds.intersection(even)        #it returns only common elements of both sets.
#print(i)
setA = {1,2,3,4,5,6}
setB = {4,5,7,8}
diff = setA.difference(setB)                #it returns setA elemtns those elements are not present in setB
s_diff = setA.symmetric_difference(setB)    #it returns all elments from both sets, exclude common elements.
#print(s_diff)

setA.update(setB)           #update() function: merge the two sets. return all elemnts in setA
setA.update(range(10,20))   #update() function: adding multiple elements, must be iterables.
print(setA)'''

######frozenset##########
#Immutable set() is called frozenset

#a = frozenset([2,3,4,5])
#a.add(6) #we got error
#print(a)


#################################
##########Strings################
#################################
#strings: Ordered, immutable, text representation 

'''
my_string = "Hello I'm aseeth"
my_string = 'Hello I\'m aseeth'

#my_string = "Hello I \       #here the \ back slash connect the two lines
#am aseeth"

#my_string[0] = 'h'           #get error string are immutables editing is not supported

my_string1 = my_string[2:5]         #string supports slicing. 
new_string = my_string + "Nani"     #we concatinte two strings, stored in new string object
print(new_string)'''

#my_string = "hello aseeth  and how are u"
'''
#my_string = my_string.strip()         #strip() function removes the white spaces.
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('hello'))    #starstwith() function returns boolen value. True or False
print(my_string.endswith('hello'))    #endswith() function returns boolen value. True or False
print(my_string.find('o'))             #find() function returns index number.
print(my_string.count('e'))             #count() function returns number that is how many times repeat.

print(my_string.replace('aseeth','nani')) #replace() function replace the sub string '''        
'''
list = my_string.split()            #split() function used to split the string and stored into list
new_string = ' '.join(list)         #join() function used to join the splitted string, imp function.
print(new_string)'''



############ %, .format(), f-strings == formating styles ###########

#%-format:

name = "aseeth"
age = 26
#name = 123
#my_string = "my name is %s" % name  #if name is string than we use %s
#my_string = "my name is %d" % name  #if name is integer than we use %d,float %f, these are old styles


#.format() function:
'''
my_string = "my name is {} and age is {}".format(name,27)
print(my_string)'''


#f-String- latest from 3.6
'''
my_string = f"my name is {name*3} age is {age}"
print(my_string)
my_string = f"my name is {name} age is {age}"
print(my_string)'''


##################################
#####COLLECTIONS MODULE###########
##################################
#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

#from collections import Counter

a = 'aaaaaabbbcccccc'
#my_counter = Counter(a)
#print(my_counter) #o/p: Counter({'a': 6, 'c': 6, 'b': 3})
#print(my_counter.keys())
#print(my_counter.values())
#print(my_counter.most_common(1))
#print(my_counter.most_common(1)[0][0]) #find most common element
#print(list(my_counter.elements()))      #converter as list

'''
from collections import namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt.x,pt.y)'''

'''
from collections import defaultdict #This is available in 3.7
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])'''      #it gives deafault integer value as zero.

''''
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(4)
print(d)
d.pop()
d.popleft()
d.extend([5,6,7])
d.extendleft([9,8,7])
print(d)'''


###########itertools#################
#itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators,

'''
from itertools import product
a = [1,2]
b = [3,4]
res = product(a,b)
#res = product(a,b, repeat=2)
print(list(res))'''        #o/p: [(1, 3), (1, 4), (2, 3), (2, 4)]




'''
from itertools import permutations
a = [1,2,3]

res = permutations(a, 2)    o/p:[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#res = permutations(a)       #o/p: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
                             #possible orders returns.
print(list(res)) '''


'''
from itertools import combinations
a = [1,2,3,4]
#res = combinations(a, 2)
res = combinations(a, 3)
print(list(res))'''   #o/p: returns all possible combinations with length(length mandatory)

'''
from itertools import groupby
persons = [{'name':'aseeth','age':26},{'name':'nani','age':25},
{'name':'eswar','age':26},{'name':'balu','age':26}]

res = groupby(persons, key=lambda x: x['age'])
for k,v in res:
    print(k,list(v))'''


'''
from itertools import count,cycle,repeat
for i in count(10):
    print(i)
    if i == 25:
        break'''



######################################
##########lambda functions############
######################################
#lambda arguments: expression

'''
#adding
add = lambda x: x+20
print(add(30))

mul = lambda x,y: x*y
print(mul(10,10))'''



'''
points2D = [(1,2),(15,1),(5,-1),(10,4)]

points2D_sorted = sorted(points2D) #sorting with first element that is x.
print(points2D_sorted)


points2D_sorted = sorted(points2D, key=lambda x: x[1]) #Here sorted()function sorts the based on x means 
                                                    #first element if u want to sort with 2nd elemtnt u can pass the key=

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) #sorted by adding two elemnts
print(points2D_sorted)'''


'''
points2D = [(1,2),(15,1),(5,-1),(10,4)]
def sort_by_y(x):                           #same achieved by a funciton.
    return x[1]
points2D_sorted = sorted(points2D,key=sort_by_y)
print(points2D_sorted)'''



#map(func, seq)
'''
l = [2,3,4,5]
res =map(lambda x: x**2, l)
print(list(res))

c = [x**2 for x in l]   #achieve with list comprehension
print(c)'''



#filter(func,seq)
'''
l = [2,3,4,5,7,8,9]

res = filter(lambda x: x%2==1, l) #with lambda
print(list(res))

c = [x for x in l if x%2==1]    #with list comprehension
print(c)'''


#reduce(func, seq)
'''
from functools import reduce
l = [2,3,4,5,7,8,9]
res = reduce(lambda x,y: x+y, l)
print(res)'''





##########################################################################
##########EXCEPTIONS############
'''
x = 5
if x > 0:   #condition true than below exception execute
    raise Exception("x should be less than 3")'''

'''
x = -5  # condition false than assert error display
assert(x>=0), 'x is not positive'''


#ex1:
'''
try:
    a = 5/0
except:
    print('its not possible')'''



#ex2:
'''
try:
    a = 5/0
except Exception as e:  #if u dont know exception thann use this syn
    print(e)'''


#ex3:
'''
try:
    #a = 5/0
    a = 5/1
    #b = a + '20'
    b = a+2
except ZeroDivisionError as e: # if u know than use it
    print(e)
except TypeError as e:
    print(e)
else:
    print("every thing is fine")    #when there is no exception than else block executes

finally:                #it always executes.
    print("cleaning up...")'''





#######Writing User manual Errors#####

'''
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x>100:
        raise ValueTooHighError('value is too high')
    if x<100:
        raise ValueTooSmallError('value is too small',x)
#test_value(150)

try:
    test_value(99)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)'''


#################################################################################


###########LOGGING MODULE#############
'''
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%d/%m/%Y  %H:%M:%S')

logging.debug('this is debug message')
logging.info('This is a info message')
logging.warning('This is a warnig message')
logging.error('this is error message')
logging.critical('this is a critical message')'''

'''
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',datefmt='%d/%m/%Y  %H:%M:%S')
import helper
logging.debug('this is debug message')'''

'''
import logging
import traceback

try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error('the error is %s',traceback.format_exc())'''


######################################################################################
                ############
#####################JSON########################
                ############


import json

person = {'name':'aseeth', 'age':27, 'city':'Kakinada', 'hasChildren':False, 'titles':['engineer','programmer']}

personJSON = json.dumps(person, indent=4, sort_keys = True) #Here we change python dict obj into json string called serialization ,(sort_keys is sorted the object by order of keys.,)
print(personJSON)

person = json.loads(personJSON) #Deserialization convert json to python dict.
print(person)






'''
with open('person.json', 'w') as file: #to store json data in file #Here file not created ... why??
    json.dump(person, file, indent=4)'''

'''
with open('person.json', 'r') as file: #to retrieve data from that file
    json.load(person, file, indent=4)'''


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



















