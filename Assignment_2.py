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


def convert_to_24(st):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if st[-2:]=='AM' and st[:2]=='12':
        return '00'+st[2:-2]
    #remove the AM
    elif st[-2]=='AM':
        return st[:-2]
    # Checking if last two elements of time
    # is AM and first two elements are 12
    elif st[-2:]=='PM' and st[:2]=='12':
        return st[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(st[:2])+12)+st[2:8]

now = datetime.now()
today = now.strftime("%H:%M:%S")
print(today)

if int(today[0])<=12:
    print("Converting of 24 hr format",convert_to_24(today+'AM'))
else:
    print("converting to 24 hr format : ", convert_to_24(today + "PM"))

# 5. Python program to find difference between current time and given time
# 6. Python Program to Create a Lap Timer
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
