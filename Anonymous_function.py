#sum of list using lambda
from functools import reduce
# li=[4,8,4]
# print(reduce(lambda x,y:x+y,li))

#sum of two number use lambda
# s=lambda a,b:a+b
# print(s(10,20))

#count the string length use lambda
# name="vijay"
# print(reduce(lambda x,y:x+1,name,0))

# 29. Python program to count Even and Odd numbers in a List

# li=[1,2,3,4,5,6,7,8,9,10,12,13,17,16]
# even=len(list(filter(lambda i:i%2==0,li)))
# print("Even count is:",even)
# x=len(li)-even
# print("odd count is:",x)

# odd=len(list(filter(lambda i:i%2!=0,li)))
# print(odd)

# 30. Python program to print positive numbers in a list
# li=[-1,0,2,-3,4,-5,6,7,8,9,10,12]
# l=list(filter(lambda i:i>0,li))
# print(l)

# x = lambda a : a + 10
# print(x(5))
#
#
# Multiply argument a with argument b and return the result:
#
# x = lambda a, b : a * b
# print(x(5, 6))
#
# Why Use Lambda Functions?
# The power of lambda is better shown when
# you use them as an anonymous function inside another function.

def abc(n):
    return lambda a:a*n
ob=abc(2)
print(ob(4))