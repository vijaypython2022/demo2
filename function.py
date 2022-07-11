
#def function_name(parameter1,parameter2......parameter n..):
    #docstring
    #statement(s)
    #return expression

def hELLO():
    """hELLOW FUNCTION"""
    print("Hellow Vijay")
hELLO()
print(hELLO.__doc__)  # docstring


# In[9]:


#create addition function--keyword as argument
def addition(first_number,second_number):
    result=first_number+second_number

    return result
print(addition(12,45))


# In[10]:


#function default argument
def fun(x,y=50):
    print(x)
    print(y)
fun(10)





#veriable length non-keyword argument
def no_argument(*argv,x):
    for arg in argv:
        print(argv,"x=:",x)
    
no_argument('hi','vijay','jagtap',x=10)





#veriable length keyword argument use when length unknown
def user(**kwargs):
    for arg in kwargs:
        print(arg)
    
user('hi','vijay','jagtap',[1,2,3,4])





#function are object:  python function are first class object
def emp(statement):
    return statement.upper()

print(emp("Hi hellow i am pyton student"))
user=emp
print(user("Hi hellow i am alias call"))





#can be pass as argument to other function
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(x):
    greeting=x("HIII ammmm vijay ")
    print(greeting)
greet(shout)
greet(whisper)





# function can return another function
def first_fun(x):
    def second_fun(y):
        return x+y
    return second_fun
add_15=first_fun(15)
print(add_15(10))
#OR
print(first_fun(15)(10))





#RETURNING MULTIPLE VALUE FROM A FUNCTION
def cal(x,y):
    sum=x+y
    sub=x-y
    mul=x*y
    return sum,sub,mul
x=int(input("Enter 1st:"))
y=int(input("Enter 2nd:"))
t=cal(x,y)   # t is tuple
for i in t:
    print(i)





#function inside function
def f1(): #outer function
    print("I am outer")
    def f2():
        print("I am inner function")
        a=20
        print(a)
    f2()
f1()





#Anonymous function
#lambda function
#lambda argument:expression
sum=lambda a,b :a+b
print("Sum of :",sum(10,20))

mul=lambda a,b,c :a*b*c
print("Mul is 3 number:",mul(10,5,6))

name=input("Enter name")
(lambda name:print(name))(name.upper())

# fact=lambda x:1 if x==0 else x*fact(x-1)
# print("Fact is :",fact(5))


# In[4]:


#map(fun,iterable)
#number=(1,2,3,4)
numbers1=[1,3,4,7]
numbers2=[4,7,8,9]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))


# In[11]:


#filter
def fun(ver):
    letters=['a','e','i','o','u']
    if ver in letters:
        return True
    else:
        return False
    
seq=['g','e','i','p']
filtered=filter(fun,seq)
for result in filtered:
    print(result)
print(filtered)


# In[1]:


# perform addition using for loop
lst=[1,2,3,4,5]
lst1=[]
for i in lst:
    i=i+i
    lst1.append(i)
print(lst1)


# In[11]:


#use filter
def evenodd(x):
    if x%2==0:
        return True
    else:
        return False
lst=[1,2,3,4,5]
result=list(filter(evenodd,lst))
result1=tuple(filter(evenodd,lst))

print(result)
print(result1)

#for i in result:
 #   print(i)#


# In[14]:


#use lambda
lst=[1,2,3,4,5]
result=tuple(filter(lambda x: True if x%2==0 else False,lst))
print(result)
result1=list(filter(lambda x: True if x%2==0 else False,lst))
print(result1)


# In[15]:


#MAP map(function,(list,tuple,set)) **peform operation based on expression given in function
#FILter filter(function,sequence) **filter based on condition given function return true value
#reduce(function,seq) **return singe element import functools


# In[16]:


#without reduce function
sum=0
lst=[1,2,3,4,5]
for i in lst:
    sum+=i
print(sum)


# In[17]:


#use reduce
import functools
lst=[1,2,3,4,5]
def abc(x,y):
    return x+y
result=functools.reduce(abc,lst)
print(result)


# In[18]:


#use reduce+lambda
import functools
lst=[1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b,lst))


# In[20]:


str="vijay"
result="".join(list(map(lambda x:x*2,str)))
print(result)
            


# In[62]:


#decorator
def first_stud(func):
    def james():
        name="Vijay"
        mark=45
        mark=func(name,mark)
        result="Name:{} and Marks is:{}"
        print(result.format(name,mark))
    return james

def second_stud(func):
    def ajay():
        name="Ajay"
        mark=31
        mark=func(name,mark)
        result="Name:{} and Marks is:{}"
        print(result.format(name,mark))
    return ajay

#@second_stud
@first_stud
def result_System(name,mark):
    if mark>35:
        print("Student is Pass")
        return mark
    else:
        print("Student is Fail !")
        return mark
    
result_System()   #MAIN FUNCTION CALL


# In[10]:


__maruti__=1000
def car():
    #global maruti
    maruti=2000
    print(maruti)
    
def van():
    print(maruti)
car()
van()


# In[2]:


def dish(dishes):
    for x in dishes:
        print(x)
        
dishes=[1,2,3,4]
dish(dishes)


# In[24]:


#ONLINE PRODUCT ORDER SYSTEM

def place_order(dict):
    global sum

    sum = 0
    for i in dict.values():
        sum+=i
    if sum<499:
        print("Dear Customer your total value of shoping is less than 500")
    else:
        print("Total value of your product is:",sum)

    total=P_DILIVERY(sum)
    return total

def P_DILIVERY(x):
    """function check cart total price and decide delivery charges"""

    if (sum<= 499):
        pay_charges = 49
        print("Delivery Charges required :", pay_charges)
        Pay_total = sum + pay_charges
        print("Total Payable Payment is:", Pay_total)

    else:
        print("Thank You for shopping with us.Your Product is shipped")
    return x


cart = {"Trimer": 399, "Charger": 299}
cart1 = {"Book": 549, "Mobile_cover": 300}
cart2 = {"Lock": 149, "Mouse_pad": 99}
place_order(cart)




# In[12]:


def P_DILIVERY(s):
    """function check cart total price and decide delivery charges"""
    
    if (s <= 499):
        pay_charges = 49
        print("Delivery Charges required !", pay_charges)
        total=s+pay_charges
        print("Total Payment is:",total)
        
    else:
        print("Your Product is shipped. Thank You for shopping")
        
P_DILIVERY(650)


# In[12]:


l1=[1,2,3,4,5,6]
even=(filter(lambda i:i%2==0,l1))
print(list(even))


# In[ ]:





# In[22]:


x, y, z, n = (int(input()) for _ in range(4))

print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])


# In[13]:


#max number
n = int(input())
arr = map(int, input().split())
for i in arr:
    mx=max(arr)
print("Max is",mx)
    


# In[16]:


#max of list
list1 = [10, 20, 4, 45, 99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",str(secondmax))


# In[17]:


#function to find second largest number from list
def second_max(list1):
    a=[x for x in list1 if x<max(list1)]
    return max(a)

list1=[10,20,7,45,99]
second_max(list1)


    


# In[22]:


#use lambda find second largest from list
list=[45,78,89,12,7]
mx=list(filter(lambda x:fo
print(mx)


# In[1]:


result1=list(filter(lambda x: True if x%2==0 else False,lst))


# In[13]:


def fun(ver):
    vow=['a','e','i','o','u']
    if ver in vow:
        return True
    else:
        return False
    
seq="we work for brain you"
filtered=filter(fun,seq)
for result in filtered:
    print(list(result))
print(filtered)


# In[5]:


def decorator(func):
    def inner(x):
        print("#"*len(x))
        func(x)
        print("#"*len(x))
    return inner
@decorator
def abc(y):
    print(y)
abc(input() or "Good morning")


# In[ ]:




