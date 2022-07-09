# list1=[45,78,12,65,98,88,46,77]
# length=len(list1)
# n=0
# if (length %2==0):
#     n=int(len(list1)/2)
#     print("List is rotate")
#     list1 = (list1[len(list1)-n:len(list1)]+list1[0:len(list1)-n])
#     print(list1)
#
# else:
#     print("List size should be even number")
#     print(list1
# list2=[65,98,88,45,78,12]
# n=1
# list2=(list2[6-1:6]+list2[1:5]+list2[0:1])


# list1=[45,78,12,65,98,88,46,77]
#
# d=int(input("Value of step"))
# l=len(list1)
# list1=list1[d:l]+list1[0:d]
# print(list1)








#i)
# list1=[45,78,12,65,98,88]
# print("Max is:",max(list1))
# # #ii)Using Negative slicing if list sorted
# list1.sort()
# print(list1)
# print("Max is:",list1[-1])
#
# def swap(li,p1,p2):
#     li[p1],li[p2]=li[p2],li[p1]
#     return li
# li=["Apple","Banana","Orange","Jackfruit"]
# p1,p2=1,3
# print("After swap",swap(li,p1,p2))

# def clr(li):
#     l=len(li)
#
#     for i in range(0,l):
#         print("Removed",li.pop())
#
# li=[10,40,50,60]
# print(clr(li))
#ii)using while and remove()
# li=['abc',10,'xyz',20]
# while(li!=''):
#     for i in li:
#         li.remove(i)
#         print("removed",i)
# print("list is:",li)

# li ="vijay"
# l="vijayjagtap"
# x=l.__contains__(li) # it return true if two string same char
# print(x)

# string = "python team python team "
# substring = "python"
#
# # count after first 'i' and before the last 'i'
# count = string.count(substring, 8, 25)
#
#
# # print count
# print("The count is:", count)
# list1=[1,2,3,4,5]
# for i in range(len(list1),0,-1):
#     print(i)

#Acess dictinary element keys(),values(),items()
# d={"a":1,"b":2,"c":3,"d1":{"x":12,"y":13}}
# x=d.fromkeys("c",3)
# print(x)
# for i in d.keys():
#     print("Keys",i)
# for i in d.values():
#     print("Values",i)
# for i in d.items():
#     print(i)
# output:
# ('a', 1)
# ('b', 2)
# ('c', 3)
# ('d1', {'x': 12, 'y': 13})

#convert sequence to dict
# seq = {'a', 'b', 'c', 'd', 'e'}
# li=["apple","banana","orange"]
# res=dict.fromkeys(li,"fruits")
# print(str(res))
# output :{'apple': 'fruits', 'banana': 'fruits', 'orange': 'fruits'}


#popitem() demo- it pop key-value pair randomly
# d={'apple': 'fruits', 'banana': 'fruits', 'orange': 'fruits'}
# x=d.popitem()
# print(x)
# print(d)
# output:
# ('orange', 'fruits')
# {'apple': 'fruits', 'banana': 'fruits'}

# #pop() demo- pop() method using key return value of key
# d={'apple': 'fruits', 'banana': 'fruits', 'orange':100,'greps':200}
# x=d.pop('apple')
# print(x)
# print(d)
# output:
# fruits
# {'banana': 'fruits', 'orange': 100, 'greps': 200}

# def clr(li):
#     l = len(li)
#     for i in range(0,2):
#         print("Removed", li.pop())
#
# li = [10, 40, 50,60]
# print(clr(li))
# print(li)

# li=['abc',10,'xyz',20]
# print("Before clear",li)
# a=3
# while():
#     for i in li:
#         li.remove(i)
#         print("removed",i)
# print("list is:",li)
#
# li=[1,2,3,4,5,6,7,8,9,10,12]
# even=(list(filter(lambda i:i%2==0,li)))
# print(even)
def even(x):
    for i in x:
        if (i%2==0):
            li2.append(i)
    print("Normal Function",li2)

li=[1,2,3,4,5,6,7,8,9,10,12]
li2=[]
even(li)
print((lambda x: (x % 2 and 'Odd number' or 'Even number'))(6))

So why is a tuple immutable?
We already have lists to store collections of objects
Why do we need tuples?
Suppose you write a method that depends on a particular
sequence of objects remaining the same throughout the lifetime of the code.
If you store these objects in a list, there is a chance that some other
method using the list will accidentally alter it and thus break your method.
Thus, in a way, a tuple offers a guarantee that a particular collection of
objects will remain fixed.