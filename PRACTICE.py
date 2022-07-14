# str=input("Enter some string: ")
# substr=input("Enter substring to be find in string: ")
# try:
#     if str.index(substr)>=0:
#      print("Yes")
# except:
#     print("No")
# Rahul Shirsath10:33 PM
# s1="rahul"
# s2=s1[-1]
# s3=s1.index(s2)
# s4=s3+1
# print(s4)

# # 40. Python program to check if a string is palindrome or not Reverse words in a given String
#
#
# str1 = input("Enter a string : ")
#
# if (str1 == str1[::-1]):
#     print("yes")
# else:
#     print("no")


# 41. Python Ways to remove i’th character from string
#

# index = int(input("Enter a character to remove : "))
#
# for i in range(len(str1)):
#     if index == i:
#         continue
#     else:
#         print(str1[i],end='')
# print(str1.replace(str1[index],''))

#swap two varibale value (using third veriable)
# a=10
# b=20
# temp=0
# print("Before Swaping values of A:",a,"and B:",b)
# temp=a # temp hold 10
# print(temp) #10
# a=b        # a is 20
# print("a",a)
# b=temp  #temp value assign to b
#
# print("After swaping values of A:",a,"and B:",b)

#swap two veriable without using third variable
# a=10
# b=20
# a,b=b,a
# print("After swaping values of A:",a,"and B:",b)

#sum of list using lambda
# from functools import reduce
# li=[4,8,4]
# print(reduce(lambda x,y:x+y,li))
#
# #sum of two number use lambda
# s=lambda a,b:a+b
# print(s(10,20))
#
# #count the string length use lambda
# name="vijay"
# print(reduce(lambda x,y:x+1,name,0))

# from difflib import get_close_matches
#
# def find_close_matches(text,seq):
#     print(get_close_matches(text,seq))
# seq="python is programing language"
# s=seq.split(" ")
# #seq=["pyt","python","pypdf","numpy","list","dict","jpython","p"]
# txt="pyt"
# find_close_matches(txt,s)


# Print the obtained permutations
#Assignment 54

# def get_permutation(string, i=0):
#     if i == len(string):
#         print("".join(string),end="")
#     count=0
#     for j in range(i, len(string)):
#         count += 1
#         words = [c for c in string]
#
#         # swap
#         words[i], words[j] = words[j], words[i]
#
#         get_permutation(words, i + 1)
#     print(count)
# print(get_permutation('yup'))

#count each char in string
a="abcabb"
# a=input("Enter string \n")
d={}
l=len(a)
print("length is:",l)
for x in a:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print("Occured",k,"Times",v)
