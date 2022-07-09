str=input("Enter some string: ")
substr=input("Enter substring to be find in string: ")
try:
    if str.index(substr)>=0:
     print("Yes")
except:
    print("No")
Rahul Shirsath10:33 PM
s1="rahul"
s2=s1[-1]
s3=s1.index(s2)
s4=s3+1
print(s4)
arjun waditke10:34 PM
elements repeat astil tr work nahi honar
Rahul Shirsath10:37 PM
hmmm
teambrainwork python202211:22 PM
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

