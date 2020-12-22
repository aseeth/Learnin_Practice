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
#import re
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


#5(i))Find given num is a palindrom or not?
'''
def palindrom(num):
    num1 = num
    rev = 0
    while num > 0:
        dig = num%10
        rev = rev *10+dig
        num = num//10
    if num1 == rev:
        print("It is a palindrom num")
    else:
        print("Not a palindrom")
num = int(input("enter u r number:"))
palindrom(num)'''



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
'''
def task13(num):
    if num == 0:
        return "factorial is 1"
    elif num == 1:
        return num
    else:
        return num*task13(num-1)
num = 6
print(task13(num))'''




#14)Find the given num is a armstrong or not?
'''
def armstrong(num):
    num1=num
    l = len(str(num))
    arm = 0
    while num>0:
        dig = num%10
        arm = arm+dig**l
        num = num//10
    if num1 == arm:
        print("armstrong")
    else:
        print("not")

num=int(input("enter u r num:"))
armstrong(num)''' 




#15)check given num is prime or not?
'''
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                print("not prime")
                break
        else:
            print("prime")        
num=int(input("enter num:"))
prime(num)'''




#15(i) print all prime numbers upto u need?
'''
def prime(num):
    for i in range(num):
        if i>1:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                print(i,end=",")
num = int(input("enter u r num: "))
prime(num)'''


#16)write algorithm for binary search?

'''
def binSearch(l,n):
    start = 0
    end = len(l)-1
    mid = len(l)//2
    while start <= end:

        if n == l[mid]:
            return mid

        elif n>l[mid]:
            start = mid +1
            
        else:
            end = mid - 1
    return -1
        
l = [19,22,30,43,50]
n = int(input("enter number: "))
res = binSearch(l,n)

if res != -1:
    print("num present at", res,"index")
else:
    print("num not present in list")'''



#17)write o/p for given python code?
#print("\t\tWelcome\n") #twotab spaces Welcome goto next line



#18)write o/p for given python code?
'''
a = 60
print(60<<2) # find binary of 60 then add 2 zeros right side.o/p:240'''



#19)convert the input camel case string to snake case?
'''
def conCase(s): 
    res = [s[0].lower()]
    for char in s[1:]:
        if char.isupper():
            res.append("_"+char.lower())
        else:
            res.append(char)
    return ''.join(res)
s = "AseethNani"
print(conCase(s))'''


#19(i) Same as above but based on num of input strings?
'''
def conCase(s):
    l1 = []
    for i in range(s):
        l1.append(input())
    l2 = []
    for s in l1: 
        res = [s[0].lower()]
        for char in s[1:]:
            if char.isupper():
                res.append("_"+char.lower())
            else:
                res.append(char)
        out=''.join(res)
        l2.append(out)
    for line in l2:
        print(line)
s = int(input("enter num of strings: "))
conCase(s)
'''


#20)run the given num of test cases, and if value % 3 then print 'fizz',value%5
#then print 'buzz' or % by both 3 and 5 then print 'fizzbuzz'?

'''
def task20(x):
    values = list(input().split())
    for j in range(0,x):
        for i in range(1,int(values[j])+1):
            if(int(i)%3==0 and int(i)%5==0):
                print('FizzBuzz')
            elif(int(i)%3==0):
                print('Fizz')
            elif(int(i)%5==0):
                print ('Buzz')
            else:
                print(i)
x = int(input())
task20(x)'''


#21) find the out put?
'''
line= "Home Alone"
line [4] = "-"
print(line)''' #TypeError: 'str' object does not support item assignment


#22)What is the output of the following Python code:?
'''
a = 10
b = 20
c = b/a
print(c) #o/p: 2.0'''


#23)What is the output of the following Python code:?
'''
s = "\t\tWelcome\n"
print(s.strip())        #o/p:Welcome'''



#24)What is the output of the following Python code:?
'''
d = {}
d.setdefault("name":"aseeth")
print(d)          #o/p:SyntaxError: invalid syntax ("name"="aseeth")'''



#25)What is the output of the following Python code:?
'''
a = 60
print(a<<2)  #o/p:240'''


#26)What is the output of the following Python code:?
'''
x = [1,2,3,4,5]
y = [11,12,13,14,15]
print(len([m+n for m,n in zip(x,y)]))   #o/p:5'''



#27)
#a = "abcdefgh"
#b = "xyz"
#c = "12345"
#write a logic to produce the following out put:ax1,by2,cz3,d4,e5,f,g,h??

def task27(a,b,c):
    l = [a,b,c]
    m = max(len(i) for i in l)
    final = []
    for i in range(0,m):
        s = ''
        for each in l:
            try:
                s += each[i]
            except IndexError:
                pass
        final.append(s)
    out = ','.join(final)
    print(out)
a = "abcdefgh"
b = "xyz"
c = "12345"
task27(a,b,c)



