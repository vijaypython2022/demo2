#Zip() example

# l=["vijay","ajay","santosh"]
# s=(10,20,30)
# #using zip() map the value each name
# student=zip(l,s)
# print(set(student))
# output:
# {('vijay', 10), ('ajay', 20), ('santosh', 30)}

# l=["vijay","ajay","santosh"]
# s=(10,20,30)
# for i,(name,roll) in enumerate(zip(l,s)):
#     print(i,name,roll)
#
# ouput:
# 0 vijay 10
# 1 ajay 20
# 2 santosh 30

# #create dictionary using zip() of two list
# mobile=["Realme","oppo","samsung","redmi"]
# price=[11999,12999,16799,13599]
# new_dict={
#     mobile:price for mobile,price in zip(mobile,price)
# }
# print(new_dict)
# output:
# {'Realme': 11999, 'oppo': 12999, 'samsung': 16799, 'redmi': 13599}

#HOW TO UNZIP

l=["vijay","ajay","santosh"]
s=(10,20,30)
#using zip() map the value each name
student=zip(l,s)
student=list(student)
print("zip result:",student)
s1,s2=zip(*student)
print("After Unzip values",end="")
print(s1)
print("After Unzip values",end="")
print(s2)


#ENUMERATE() IN PYTHON
# when we iterate thing sometimes we need to count the itration.
# for that we use python inbuild enumerate() method.
# neumerate() method add a counter to an iterable and return it in form of
# enumerating object.this object we can directly use in for loop and convert
# list of tuple.
# Syntax: enumerate(iterable, start=0)
colors=['red','blue','green','purple','pink','black','white']


