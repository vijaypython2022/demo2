#sort element without inbuild function
# li=[4,8,3,7,1,3]
# for i in range(6):
#     for j in range(i+1,6):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
#
# print(li)

#reverse string using for loop
# st="vijay"
# a=""
# for i in st:
#     a=i+a
# print(a)

#reverse the string using while loop
# st="vijay"
# a=""
# while l>=0:
#     a=a+st[l]
#     l=l-1
# print("while",a)

# a="sadashiv"
# print(a[-1:0:-1])
# import functools
#
# li=[4,8,3,7,1,3]
# x=list(filter(lambda i:i%2!=0,li))
# print(x)

# st="vijay"
# a=""
# l=len(st)-1 #4
# for i in st:
#     a=i+a
#     print(a)
# print(a)
#
#sort the list usinf two for loop
# li=[4,5,1,3,2]
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)
# # single loop
#
# for i in li:
#     if li[i]
#get user input Calculate Average of selected student

# n = int(input("Enter no. of record:"))
# student_marks ={}
# for i in range(n):
#     name,*marks = input().split()
#     student_marks[name]=marks
# st=input("Enter name of student to calculate avarage:")
# if (st in student_marks.keys()):
#     print("Marks is:",student_marks[st])
#     values=student_marks[st]
#     total=[float(x) for x in values]
#     sub=len(total)
#     total_mark=sum(total)
#     res=total_mark/sub
#     print("Percentage is :",res)
#
# a = []
# s = int(input("Enter the size of array: "))
#
# for i in range(0,s):
#     b = list(map(int,input("\nEnter the numbers : ").strip().split()))[:s]
#     a.append(b)
# print(a)
# n1=a[0][1]**2
# n2=a[1][2]**2
# n3=a[2][0]**2
# res=n1+n2+n3
# print(res)

# class Test:
#     def __init__(self):
#         pass
#     def __m1(self): #private method
#         print("m1 method")
#     def _m2(self): #protected method
#         self.__m1()
#         print("m2 method")
#     #@classmethod
#     def m3(cls): #static method
#         print("m3 method")
# ob=Test()
# ob._m2()
# ob.m3()
# Test.m3(45)


for _ in range(int(input())):
        name = input()
        score = float(input())











