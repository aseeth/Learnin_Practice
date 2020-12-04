###########################################
#########INTERVIEW QUESTIONS###############
###########################################

#1)if input l = [2,3,4,5] then o/p: l = [60,40,30,24]?

'''
from functools import reduce
def task1(l):
    emp_list = []
    for num in l:
        new_list = l[:]
        new_list.remove(num)
        emp_list.append(reduce(lambda a,b:a*b, new_list)) #Here we use lambda function
    return emp_list
l = [2,3,4,5]
res=task1(l)
print(res)'''

#with out lambda so with out lambda we need two for loops.

'''
def task1(l):
    emp_list=[]
    for num in l:
        new_list = l[:]
        new_list.remove(num)
        val = 1
        for num1 in new_list:
            val = val*num1
        emp_list.append(val)
    print(emp_list)
l = [2,3,4,5]
task1(l)'''


#2)write regular expression for validate email and phone num?

#for validating phone num..!
import re
'''
def task2(num):
    res = re.fullmatch("[+]91[789]\d{9}",num)
    if res != None:
        print("valid phone num")
    else:
        print("not valid")
num=input("enter u r phone num:")
task2(num)'''

#for validating mail?
'''
def task2(mail):
    res=re.fullmatch("[a-zA-Z][a-zA-Z0-9._]*@gmail[.]com",mail)
    if res != None:
        print("valid mail id")
    else:
        print("not valid")
mail = input("enter u r mail id: ")
task2(mail)'''

#3)print first 10 numbers in dictionary format?
'''
def task3(l):
    res = dict([(k,v) for k,v in zip(l[::2],l[1::2])])  #dictionary format
    res1 = list([(k,v) for k,v in zip(l[::2],l[1::2])]) #list format
    print(res)
    print(res1)
l = [1,2,3,4,5,6,7,8,9,10]
task3(l)'''

#4)if j = [[[[[6]]]]] in this how to get 6?
'''
j = [[[[[6]]]]]
print(j[0][0][0][0][0])'''

#5)Reverse a string without using built function j = 'welcome' and check whether string
#is palindrome or not?
'''
def task5(s):
    rev=""
    l = len(s)-1
    while l >= 0:
        rev = rev+s[l]
        l = l-1
    print(rev)
    if s == rev:
        print("palindrom")
    else:
        print("not palindrom")
#s = "welcome"
s = "madam"
task5(s)'''

#6)write sql update and ORM update query?
'''
sql_query = "update table_name set field = field+add where condition";
exp: "update employee set salary = salary+2000 where emp_name = 'aseeth'";

orm_query:
obj = model.objects.get(id=id)
obj = obj + 2000
obj.save()'''

#7)Write out puts below questions?

'''
class C:
	danger = 2
c1=C()
c2=C()

print(c1.danger)
c1.danger = 3
print(c1.danger)
print(c2.danger)
del c1.danger
C.danger = 3
print(c2.danger)'''


#8)if list = ['a','b','c','d','e'] than what is the output of print list[10:]?
'''
list = ['a','b','c','d','e']
print(list[10:])'''

#9)w a p to read a file and splite and print based on our requirement??
'''
def task9():
    f = open("D:\Learnin_Practice\Python\nani.txt","r")
    a=[]
    b=[]
    c=[]
    for i in f:
        for k in i.split():
            if len(k)==1 or len(k)==2 or len(k)==3:
                a.append(k)
                
            elif len(k)==4 or len(k)==5 or len(k)==6:
                b.append(k)
                
            else:
                c.append(k)
task9()
print("1 or 2 or 3 charecter string")
print(a)
print()
print("4 or 5 or 6 charecter string")
print(b)
print()
print("more than 6 charecter string")
print(c)'''


#10)Print the element with index?
'''
l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    print(l[i],"index at",i)'''


#11)
'''
a
as
ase
asee
aseet
aseeth'''
'''
def task11(s):
    for i in range(1,len(s)+1):
        print(s[:i])
s = "aseeth"
task11(s)'''

#12)capitalize the fitst letter for given string?
#case1:
'''
def task12(s):
    l= s.split()
    s = [word.capitalize() for word in l] #here we use list comprehension
    s = " ".join(s)
    print(s)
s = "hi aseeth how are u, are u ok"
task12(s)'''

#case2:
'''
def task12(s):
    l = s.split()
    s1 = ""
    for word in l:
        s1 = s1 + word.capitalize()+" "
    print(s1)
s = "hi aseeth how are u, are u ok"
task12(s)'''


#13)Find the factorial of a num using recursion?
def task13(num):
    if num == 0:
        return "factorial is 1"
    elif num == 1:
        return num
    else:
        return num*task13(num-1)
num = 6
print(task13(num))

