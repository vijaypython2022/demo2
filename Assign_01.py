#1) Python programe for factorial of a number without recursion
# def facto(x):
#     def inner(func):
#         fact=1
#         while(x>0):
#             fact=fact*x
#             x=x-1
#         return inner()
# print(facto(5))
# #
# # n=5
# # fact=1
# # while(n>0):
# #     fact=fact*n
# #     n=n-1
# # print(fact)
#
# class F:
#     def __init__(self,a):
#         self.a=a
#         fact=1
#         while(a>0):
#             fact=fact*a
#             a=a-1
#         print("Factorial is:{}".format(fact))
# ob=F(5)
#output=120

#2)Python programe check Armstrong number
#Armstrong number 3 digit the sum of cube each digit is equal to number itself.
# number=int(input("Enter number check Armstrong \n"))
# sum=0
# temp=number
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp//=10
# if number==sum:
#     print("{} is Armstrong number".format(number))
# else:
#     print("{} is not Armstrong number".format(number))

#3)Python program to print all Prime numbers in an Interval

# def check_prime(number):
#     for i in range(1,100):
#         if (number % i)==0:
#             print("{} Its prime number".format(number))
#             break
#         else:
#             print("not prime")
#     return number
# check_prime(32)

# number=44
# if (number>1):
#     for i in range(2, number):
#         if (number % i) == 0:
#             print("{} Its not prime number".format(number))
#             break
#         else:
#             print(number,"its prime")
#             break

# 4. Python Program for Fibonacci numbers 0,1,1,2,3,5
# number=20
# count=0
# n1,n2=0,1
#
# while count<number: #check number greater than 0
#     print(n1)
#     sum=n1+n2
#     #update value of n1 and n2
#     n1=n2
#     n2=sum
#     count=count+1

# 5. Python Program to find sum of array (using multiple approach)
#i)
# a=[2,3,1,5,8,4]
# print(sum(a)) #output is 23
#ii)Add 1 each element to list
# a=[2,3,1]
# for i in a:
#     #print(i)
#     s=i+1
#     print(s)
#iii) find the mean value
# from statistics import mean
# li=[2,3,1,4,5,14,20,12]
# def av(li):
#     return mean(li)
# a=av(li)
# print(round(a,2))

#iv) sum of list
# li=[2,4,6,8,10]
# def add_list(li):
#     s=0
#     for i in li:
#         s=s+i
#     print("Sum Of li is:{}".format(s))
# add_list(li)

# 6. Python Program to find largest element in an array

# i) 1st way use builtin function
#
# list1=[45,78,12,65,98,88]
# print("Max is:",max(list1))

# #ii)Using Negative slicing if list sorted
# list1.sort()
# print(list1)
# print("Max is:",list1[-1])

#iii) using function
# def large(list1):
#     mx=list1[0]
#     for i in list1:
#         if i>mx:
#             mx=i
#     return mx
# list1=[45,78,12,65,98,88,]
# print("Maximum number is:",large(list1))

# 7. Python Program for array rotation
# list1=[45,78,12,65,98,88,46,77]
# n=len(list1)/2
# li=(list1[len(list1)-n:len(list1)]+list1[0:len(list1)-n])
# print(li)
#output [65, 98, 88, 45, 78, 12]


# 8. Python Program for Reversal algorithm for array rotation
#
# list1=[45,78,12,65,98,88,46,77]
#
# d=int(input("Value of step"))
# l=len(list1)
# list1=list1[d:l]+list1[0:d]
# print(list1)

# 9. Python Program to Split the array and add the first part to the end
# list2=[65,98,88,45,78,12]
# n=1
# list2=(list2[6-1:6]+list2[1:5]+list2[0:1])
# new_list=(list2[len(list2)-n:len(list2)]+list2[0:len(list2)-n])
# new_list=(list2[6-1:6]+list2[0:6-1])
# print(list2)
#[12, 98, 88, 45, 78, 65]

#METHOD 2
# list2=[65,98,88,45,78,12]
# li=[]
# for i in range(3,len(list2)):
#     li.append(list2[i])
# for i in range(0,3):
#     li.append(list2[i])
#
# print(li)



# 10. Python Program for Find reminder of array multiplication divided by n
# list3=[65,98,88,45,78,11]
# rem=[]
# mul=[]
# div=[]
# r,m,d=0,0,0
# n=int(input("Enter number to perform operation on list:\n"))
# for i in list3:
#     r=i%n
#     m=i*n
#     d=i/n
#     rem.append(r)
#     mul.append(m)
#     div.append(d)
# print("Remender of list is:",rem)
# print("Multiplication of list is:",mul)
# print("Division of list is",div)

# 11. Python program to interchange first and last elements in a list

#i)last element is move to first position
# li=[44,77,88]
# li.insert(0,li.pop(2))
# print("last element is move to first position"+str(li))
#output :last element is move to first position[88, 44, 77]

#ii)interchange the first to last element
# li=["first",77,"last"]
# li.insert(2,li.pop(0))
# li.insert(0,li.pop(1))
# print("interchange first to last",li)
#output: interchange first to last ['last', 77, 'first']

# 12. Python program to swap two elements in a list

# def swap(li,p1,p2):
#     li[p1],li[p2]=li[p2],li[p1]
#     return li
# li=["Apple","Banana","Orange","Jackfruit"]
# p1,p2=1,3
# print("After swap",swap(li,p1,p2))

#output: After swap ['Apple', 'Jackfruit', 'Orange', 'Banana']


# 13. Python program to remove Nth occurrence of the given word
# def remove_Nth(list,word,nth):
#     count=0
#     for i in range(0,len(list)):
#         if (list[i]==word):
#             count+=1
#             if (count==nth):
#                 del(list[i])
#                 return True
#     return False
#
# list=['sub','for','sub']
# nth=2
# word='sub'
# print(remove_Nth(list,word,nth))
# print(list)

#output:
# True
# ['sub', 'for']
#***********************************************
# a=input("Enter string \n")
# d={}
# l=len(a)
# print("length is:",l)
# for x in a:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print("Occured",k,"Times",v)

# 14. Python | Ways to find length of list
# li=[1,'A',2,'B',3,'C',4]
# print("Using len() given list length is:",len(li))
# count=0
# for i in li:
#     count=count+1
# print("Using for loop list length is:",count
#
#
# li=[4,8,3]
# y=[x for i in range(len(li))]
# print(y)

#********************************************************
# 15. Python | Ways to check if n element exists in list
#li=[11,2,6,4,8,7,10,3]
#1)Native method
#i)using for loop
# for x in li:
#     if (x==8):
#         print("Element is exists")
#ii)using in operator
# if(6 in li):
#     print("Element is exists")
#using set()
# li= set(li)
# if 4 in li:
#     print ("Element Exists")
#2)using sort() and bisect()
# from bisect import bisect,bisect_left
# li.sort()
# if bisect(li,6)!=bisect(li,3):
#     print("Element exists")
# else:
#     print("Not exists")
#************************************************************
# 16. Different ways to clear a list in Python

#i) Using clear() method
# li=['abc',10,'xyz',20]
#print("Before clear",li)
# li.clear()
#print("After clear",li)

#ii)using while and remove()
# li=['abc',10,'xyz',20]
#print("Before clear",li)
# while(li!=''):
#     for i in li:
#         li.remove(i)
#         print("removed",i)
# print("list is:",li)

#iii) using function-pop() method
# def clr(li):
#     l = len(li)
#     for i in range(0, l):
#         print("Removed", li.pop())
#
# li = [10, 40, 50,60]
# print(clr(li))

#iv)reinitialized list
# li = [10, 40, 50,60]
#print("Before clear",li)
# li=[]
#print("After clear",li)

#v) using *=0
# li = [10, 40, 50,60]
#print("Before clear",li)
# li*=0
#print("After clear",li)

#using del keyword
# li = [10,40,50,60]
# print("Before clear",li)
# del li[:]
# print("After clear",li)


#****************************************************************
# 17. Python | Reversing a List Python
# li=[1,2,3,4] #sorted list
# li2=[]
# for i in li:
#     li2.append(li[-i])
# print("Using append",li2)
#
# li=[55,44,78]  #unsorted list
# li.sort(reverse=True)
# print("reversed",li)



# 18. Cloning or Copying a list Python
# fruits=["apple","cherry","banana","Greps"]
# clone=fruits[:]
# print("clone Using slicing[:] :",clone)
# clone2=fruits.copy()
# print("clone Using copy():",clone)


# 19. Count occurrences of an element in a list



# 20. Python program to find sum of elements in list
#1)using loop
# list1=[4,6,7,2]
# res=0
# for i in list1:
#     res=res+i
# print(res)
# #2) using sum()
# list1=[4,6,7,2]
# print("Using sum()",sum(list1))
# #3)Using lambda
# from functools import reduce
# list1=[4,6,7,2]
# print("Using Lambda",reduce(lambda x,y:x+y,list1))
# #4) while loop
# list1=[4,6,7,2]
# b=len(list1)-1
# count=0
# while b>=0:
#     count+=list(b)
#     b-=1
# print("using while loop",count)
#



# 21. Python | Multiply all numbers in the list

# li=[18,17,150,19,22,7,4]
# value=2
# for i in li:
#     res=value*i
#     print(res)
#
# 22. Python program to find smallest number in a list
# def large(li):
#     largest=li[0]
#     for i in range(len(li)):
#         if li[i]<largest:
#             largest=li[i]
#     return largest
# li=[18,17,150,19,22,7,4,]
# print("small number is:",large(li))
#
# # 23. Python program to find largest number in a list
# def large(li):
#     largest=li[0]
#     for i in range(len(li)):
#         if li[i]>largest:
#             largest=li[i]
#     return largest
# li=[18,17,150,19,22,7,4,]
# print("Max number is:",large(li))


# 24. Python program to find second largest number in a list
# def Sec_Largest(arr):
#     secondLargest = arr[0]
#     largest = arr[0]
#
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             largest = arr[i]
#
#     for i in range(len(arr)):
#         if arr[i] > secondLargest and arr[i] != largest:
#             secondLargest = arr[i]
#     return secondLargest
# print(Sec_Largest([10, 20, 4, 45, 99]))

# 25. Python program to print even numbers in a list
# list1=[1,2,3,4,5,6,7]
# for i in list1:
#     if (i%2==0):
#         print(i)
# list1=[1,2,3,4,5,6,7]
# print(list(filter(lambda i :i%2==0,list1)))

# 26. Python program to print odd numbers in a List
# list1=[1,2,3,4,5,6,7]
# # for i in list1:
# #     if (i % 2 != 0):
# #         print(i)
# #using lambda
# #print(list(filter(lambda i :i%2!=0,list1)))
# #list comprehension
# x=[i for i in list1 if i%2!=0]
# print(x)





# 27. Python program to print all even numbers in a range
# x=[i for i in range(21) if i%2==0]
# print(x)
# for i in range(21,101):
#     if (i%2==0):
#         print(i,end=' ')


# 28. Python program to print all odd numbers in a range
# for i in range(21,101):
#     if (i%2!=0):
#         print(i,end=' ')
# 29. Python program to count Even and Odd numbers in a List

# li=[1,2,3,4,5,6,7,8,9,10,12]
# even=len(list(filter(lambda i:i%2==0,li)))
# print(even)
# x=len(li)
# y=x-even
# print(y)

# odd=len(list(filter(lambda i:i%2!=0,li)))
# print(odd)








# 30. Python program to print positive numbers in a list
# li=[-1,0,2,-3,4,-5,6,7,8,9,10,12]
# l=list(filter(lambda i:i>0,li))
# print(l)


# 31. Python program to print negative numbers in a list
# for i in li:
#     if(i<0):
#         print(i)



# 32. Python program to print all positive numbers in a range

# for i in range(-8,20):
#     if (i >=0):
#         print(i)

# 33. Python program to print all negative numbers in a range
# 34. Python program to count positive and negative numbers in a list
# 35. Remove multiple elements from a list in Python
# 36. Python | Remove empty tuples from a list
# 37. Python | Program to print duplicates from a list of integers
# 38. Python program to find Cumulative sum of a list Break a list into chunks of size N in
# 39. Python | Sort the values of first list using second list
# 40. Python program to check if a string is palindrome or not Reverse words in a given String in
#str1 = input("Enter a string : ")
#
# if (str1 == str1[::-1]):
#     print("Its Pelidrome")
# else:
#     print("Not Pelidrome")

# 41. Python Ways to remove i’th character from string
#method-1
# st="vijay"
# index=4
# for i in range(len(st)):
#     if (index==i):
#         continue
#     else:
#         print(st[i])

#METHOD 2
# st='python team brainworks aa'
# x=st.replace('python',"")
# print(x)

#METHOD 2
# st='python team brainworks aa'
# print(st.translate({ord('a'):None})) #ord() get the unicode of the letter
#USING UNICODE REPLACE THE NONE VALUE USING DICT KEY VALUE

#REMOVE MULTIPLE CHARACTER IN STRING
# st='python team brainworks pune'
# print(st.translate({ord(letter):None for letter in 'htp'}))

#METHOD 3
# for i in range(6):
#     if(index==i):
#         i.remove()
#     print(i)

# index = int(input("Enter a character to remove : "))
#
# for i in range(len(str1)):
#     if index == i:
#         continue
#     else:
#         print(str1[i],end='')
# print(str1.replace(str1[index],''))




# 42. Python|Check if a Substring is Present in a Given String Find length of a string in python (4
# ways)
# 43. Python program to print even length words in a string


# a="ab "
# l=len(a)
# for i in a:
#     if (i.(l%2==0)) and (i.isspace()==True):
#         print(i)
#     else:
#         print("not found")
#

# 44. Python | Program to accept the strings which contains all vowels
# st="python is high level programing language"
# vow=['a','e','i','o','u']
# for i in vow:
#     if i==vow:
#         print("Yes, String content all vowels",)
#     else:
#         print("Not all vowels")


# 45. Python | Count the Number of matching characters in a pair of string
# 46. Python program to count number of vowels using sets in given string Remove all duplicates from
# a given string in Python
# 47. Python | Program to check if a string contains any special character Generating random strings
# until a given string is generated Find words which are greater than given length k
# 48. Python program for removing i-th character from a string
# 49. Python program to split and join a string
# 50. Python | Check if a given string is binary string or not
# 51. Python | Find all close matches of input string from a list
# 52. Python program to find uncommon words from two Strings
# 53. Python | Swap commas and dots in a String
# 54. Python | Permutation of a given string using inbuilt function
# 55. Python | Check for URL in a String Execute a String of Code in
# 56. Python String slicing in Python to rotate a string
# 57. String slicing in Python to check if a string can become empty by recursive deletion
# 58. Python Counter| Find all duplicate characters in string Dictionary Programs:
# 59. Python | Sort Python Dictionaries by Key or Value Handling missing keys in
# 60. Python dictionaries Python dictionary with keys having multiple inputs
# 61. Python program to find the sum of all items in a dictionary
# 62. Python | Ways to remove a key from dictionary Ways to sort list of dictionaries by values in
# 63. Python – Using itemgetter Ways to sort list of dictionaries by values in Python – Using lambda
# function
# 64. Python | Merging two Dictionaries Program to create grade calculator in Python
# 65. Python | Check order of character in string using OrderedDict( )
# 66. Python Counter to find the size of largest subset of anagram words
# 67. Python | Remove all duplicates words from a given sentence
# 68. Python Dictionary to find mirror characters in a string Counting the frequencies in a list using
# dictionary in Python
# 69. Python | Convert a list of Tuples into Dictionary
# 70. Python counter and dictionary intersection example (Make a string using deletion and
# rearrangement)
# 71. Python dictionary, set and counter to check if frequencies can become same Scraping And
# Finding Ordered Words In A Dictionary using Python Possible Words using given characters in
# Python
#



