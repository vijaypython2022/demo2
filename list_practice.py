#list comprehension
#print list who's character contain 'v'
# li=["vijay","vinay","sam","jacky"]
# z=[x for x in li if 'v' in x]
# print(z)
# #return even number from list
# li=[4,3,7,8,2]
# z=[x for x in li if x%2==0]
# print(z)
#
# #reverse list
# li=[1,2,3,4,5]
# print(len(li))
# z=[li[i] for i in range(len(li)-1,0,-1)]
# print(z)
#
# #return duplicate from list
# li=[1,2,1,5,4,5]
# li2=[]
# z=[x for x in li if li.count(x)>1]
# print(z)

#sum of list
# li=[2,4,6,8]
# li[1]=4
# print(li)
# ob=li
# ob[1]=8
# print(li)

#check list contains int or str
li=[2,5,"vijay","abc",55]
st=[]
numbers=[]
for i in li:
    if isinstance(i,int):
        print(i)
    if isinstance(i,str):
        print(i)

#method 2
li = [2, 5, 'abc']
st = []
numbers = []
for i in li:
    #     if int(i)==i:
    #         numbers.append(i)
    if str(i) == i:
        st.append(i)
else:
    print("numbers is:", numbers)
    print("string is:", st)

#method 3
li="ab4d"

for i in li:
    if i.isdigit():
       print("its string content int")
    if type(i)==str:
        print("its string")

# return max number from list
li = [2, 1, 8, 4, 10, 3]
mx = li[0]
for i in li:
    if i > mx:
        mx = i
print("Max number is:", mx)

# return small number from list
li = [2, 1, 8, 4, 10, 3]
small = li[0]
for i in li:
    if i < small:
        small = i
print("Small Number is:", small)

#get highest and second highest element from list
arr=[4,6,7,9,3]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print("sorted",arr)
mx=arr[0]
for i in arr:
    if i>mx:
        mx=i
print("max element is:",mx)
second_high=0
for j in arr:
    if j<mx:
        second_high=j
print("second highest element is:",second_high)

#insert,append,pop ,reverse method
li=[]
li.insert(0,5)
li.insert(1,10)
li.insert(0,6)
print(li)
li.remove(6)
li.append(9)
li.append(1)
li.sort()
print(li)
li.pop()
li.reverse()
print(li)

#create nested list dynamically and square addition of selected elements.
a = []
s = int(input("Enter the size of array: "))

for i in range(0,s):
    b = list(map(int,input("\nEnter the numbers : ").strip().split()))[:s]
    a.append(b)
print(a)
n1=a[0][1]**2
n2=a[1][2]**2
n3=a[2][0]**2
res=n1+n2+n3
print(res)
