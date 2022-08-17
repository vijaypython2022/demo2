# Date-Time Programs:
# 1. Python program to get Current Time
# import time
#
# print("Current time is:", time.strftime("%I:%p,%M:%S"))
# output:
# Current time is: 12 PM 03 13

# 2. Get Current Date and Time using Python
# import datetime
# print(datetime.datetime.now())
# output
# 2022-08-09 12:16:30.910026

# 3. Python | Find yesterday’s, today’s and tomorrow’s date
# from datetime import date, timedelta
#
# today = date.today()
# print("Todays date is:", today)
# yersterday = today - timedelta(1)
# print("Yesterday date is:", yersterday)
# tomarrow = today + timedelta(1)
# print("Tommarow date is:", tomarrow)

# 4. Python program to convert time from 12 hour to 24 hour format
from datetime import datetime


# def convert_to_24(st):
#     # Checking if last two elements of time
#     # is AM and first two elements are 12
#     if st[-2:]=='AM' and st[:2]=='12':
#         return '00'+st[2:-2]
#     #remove the AM
#     elif st[-2]=='AM':
#         return st[:-2]
#     # Checking if last two elements of time
#     # is AM and first two elements are 12
#     elif st[-2:]=='PM' and st[:2]=='12':
#         return st[:-2]
#     else:
#         # add 12 to hours and remove PM
#         return str(int(st[:2])+12)+st[2:8]
#
# now = datetime.now()
# today = now.strftime("%H:%M:%S")
# print(today)
#
# if int(today[0])<=12:
#     print("Converting of 24 hr format",convert_to_24(today+'AM'))
# else:
#     print("converting to 24 hr format : ", convert_to_24(today + "PM"))

# 5. Python program to find difference between current time and given time
# from datetime import *
#
# def diff(c_time,in_time):
#     time_format="%Y-%m-%d"
#     c_time=datetime.strptime(today,time_format)
#     print(type(c_time))
#     dt_object=datetime.strptime(in_time,"%Y-%m-%d")
#     print(type(dt_object))
#     print("current time:",c_time)
#     print("Date of birth:",dt_object)
#     delta=dt_object-c_time
#     print(delta.days)
#
#
# today='2022-08-10'
# dob='1992-08-10'
# diff(today,dob)


# 6. Python Program to Create a Lap Timer
# import time
# start=time.time()
# end=start
# lap=1
# print("Press enter to start timer \n T stop timer press Ctrl+C")
# try:
#     while True:
#
#
#         input()
#         laptime=round((time.time()-end),2)
#         totaltime=round((time.time()-start),2)
#         print("Lap Number:"+str(laptime))
#         print("Total time:"+str(totaltime))
#         print("Lap time:"+str(lap))
#         print("*"*20)
#         end=time.time()
#         lap+=1
# except KeyboardInterrupt as e:
#     print("Done",e)

# 7. Convert date string to timestamp in Python
# 8. How to convert timestamp string to datetime object in Python?
# 9. Find number of times every day occurs in a Year

# 10)write date time in text file
# import datetime
# with open("C:\\Users\\Shreee\\Desktop\\test.txt", mode='a') as file:
#     file.write('Todays Date %s recorded at %s.\n' % ('', datetime.datetime.now()))
#
# 11)Display calender
# import calendar
# year=int(input("Enter Year"))
# month=int(input("Enter month"))
# calendar=calendar.month(year,month)
# print(calendar)

#
#
# Python File Handling Programs:
# 1. Python program to read file word by word

# f=open("abc.txt","r")
# list=f.readlines()
# for line in list:
#    word=line.split()
#    for w in word:
#        print(w)
# # 2. Python program to read character by character from a file
# f=open("abc.txt","r")
# list=f.read()
# for chr in list:
#    print(chr)
# 3. Python – Get number of characters, words, spaces and lines in a file

# f=open("abc.txt","r")
# z1=f.readlines()
# lcount=0
# for lines in z1:
#     lcount+=1
# print("count of lines is ",lcount)
# wcount=0
# for line in z1:
#    word=line.split()
#    for w in word:
#        wcount+=1
# print("count of word is ",wcount)
# f.seek(0)
# z2=f.read()
# ccount=0
# for chr in z2:
#     ccount+=1
# print("count of chr is ",ccount)

# 4. Python | Finding ‘n’ Character Words in a Text File
# count = 1
# chrw = ""
# file = open('vijay.txt', 'r')
# while 1:
#     sp = file.read(1)
#
#     if count <= 4:
#         chrw = chrw + sp
#
#     if count > 4:
#         if sp == " ":
#             count = 0
#             if len(chrw) > 0:
#                 print(chrw)
#                 chrw = ""
#         elif sp != " ":
#             chrw = ""
#     count = count + 1
#
#     if not sp:
#         break
#
# file.close()

# 5. Python Program to obtain the line number in which given word is present
# f=open("vijay.txt","r")
# data=f.readlines()
# word="vijay"
# c=0
# for line in data:
#     c=c+1
#     if word in line:
#         print(c)


# 6. Count number of lines in a text file in Python
# f=open("vijay.txt","r")
# data=f.readlines()
# c=0
# for line in data:
#     c=c+1
# print(c)
# 7. Python Program to Eliminate repeated lines from a file
# f1=open("vijay.txt","r")
# data1=f1.readlines()
# for d1 in data1:
#     f2=open("xyz.txt","r")
#     data2=f2.readlines()
#     if d1 not in data2:
#         f2=open("xyz.txt","a+")
#         f2.write(d1)
# # 8. Python – Append content of one text file to another
# f1=open("abc.txt","r")
# data1=f1.readlines()
# for d1 in data1:
#     f2=open("xyz.txt","a")
#     f2.write(d1)
# # 9. Python program to copy odd lines of one file to other
# f1=open("abc.txt","r")
# data1=f1.readlines()
# c=0
# for d1 in data1:
#     c+=1
#     if c%2==1:
#         f2=open("xyz.txt","a")
#         f2.write(d1)
# # 10. Python Program to merge two files into a third file
# f1=open("abc.txt","r")
# data1=f1.readlines()
# for d1 in data1:
#     f3=open("merge.txt","a")
#     f3.write(d1)
# f2=open("xyz.txt","r")
# data2=f2.readlines()
# for d2 in data2:
#     f3=open("merge.txt","a")
#     f3.write(d2)
# 11. Python program to Reverse a single line of a text file

# f1=open("vijay.txt","r")
# lines=f1.readlines()
# c=0
# line=lines[c].split()
# r=" ".join(line[::-1])
# lines.pop(c)
# lines.insert(c,r)
# z=open("python",'w')
# z.writelines(lines)
# z.close()


# 12. Python program to reverse the content of a file and store it in another file
# writeFile = open("mydata.txt", "w")
# with open("main.txt", "r") as readFile:
#     txt = readFile.read()
# reversedContent = txt[::-1]
# writeFile.write(reversedContent)
# writeFile.close()

# Scenario Based Programs:
# 1. Python Program for Linear Search
# def linear_search(li, n, key):
#     for i in range(0, n):
#         if li[i] == name:
#             return i
#
#     return -1
#
# student_list = ['Akash', 'Amol', 'Arjun', 'vijay', 'vishal', 'rohit']
# name = 'vishal'
# size = len(student_list)
# result=linear_search(student_list, size, name)
# if result==-1:
#     print("Name not found")
# else:
#     print("Name found at {} Position".format(result))

# 2. Python Program for Binary Search (Recursive and Iterative)

# 3. Python Program for Bubble Sort
# 4. Write a python program for string that will print out char with char count.
# E.g. words = 'aaaabahhhhhaaa' Output should be a4b1a1h5
# s = 'a4b1a1h5'
# opt = ''
# for i in s:
#     if i.isalpha():
#         opt = opt + i
#         previous = i
#     else:
#         opt = opt + previous * (int(i) - 1)
# print(opt)


#E.g. words = 'aaaabahhhhhaaa' Output should be a4b1a1h5
def abc(st):

    di=dict.fromkeys(st,0)
    for i in st:
        di[i]+=1
    a = ''
    for k,v in di.items():
        a=a+k+str(v)
    return a

s='aaaabahhhhhaaa'
print(abc(s))
# 5. Write a python program to take command line arguments. (using docopt and other
# libraries). Two or more programs.
# 6. Write a python program to take input date string, time string is in UTC format we need to
# convert it into PST and print converted date time. E.g. input: “2023-02-13 18:10:27”
# 7. write a program for character count string "aaabbbccaa" for output:a5b3c2
# 8. Write a decorator for calculating execution time of any python function.
# 9. Problem: Remove specified characters in a string irrespective of the
# case.char_to_remove =['A','N'] string= 'Think Analytics'
# 5.Problem: Perform below task
# 1) Create a list of 10 even numbers using list comprehension.
# 2) Create a list of 10 odd numbers using list comprehension.
# 3) Multiply and sum them up while iterating over once.
# x = x1 + x2 + x3 + ....... + x9 + x10
# y = y1 + y2 + y3 + ....... + y9 + y10
# z = x1y1 + x2y2 + x3y3 + ....... + x9y9 + x10y10
# 10. create decorator for function which prints its arguments. decorator should check if
# argument divided by 2. if it is then only run the function.
# 11. Student management system in Python( Using Class and Object)
# Problem Statement: Write a program to build a simple Student Management System
# using Python which can perform the following operations:
# Accept, Display, Search, Delete, Update
# Accept – This method takes details from the user like name, roll number, and marks for
# two different subjects
# Search – This method searches for a particular student from the list of students. This
# method will ask the user for roll number and then search according to the roll number
# Delete – This method deletes the record of a particular student with a matching roll
# number
# Update – This method updates the roll number of the student. This method will ask for
# the old roll number and new roll number. It will replace the old roll number with a new roll
# number.
# 12. Write a program to convert json file to csv file.
