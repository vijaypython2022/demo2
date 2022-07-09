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

#create dictionary using zip() of two list
mobile=["Realme","oppo","samsung","redmi"]
price=[11999,12999,16799,13599]
new_dict={
    mobile:price for mobile,price in zip(mobile,price)
}
print(new_dict)
output:
{'Realme': 11999, 'oppo': 12999, 'samsung': 16799, 'redmi': 13599}


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

# nested dictonary use for loop
mycollege = {
    "developer": {
        "course": "python",
        "branch": "IT"},
    "science": {
        "course": "bcs",
        "branch": "computer"
    },
    "engineers": {
        "course": "BE",
        "branch": "civil"
    }
}
#Access specific value 'python'
# print(mycollege['developer']['course'])
#
# for x, y in mycollege.items():
#     for x1, y1 in y.items():
#         if y1 == "computer":
#             print(x1, y1)
#             break
# output:
# python
# branch computer

#get() method
# d={'apple': 'fruits', 'banana': 300, 'orange':100,'greps':200}
#
# x=d.get('banana')
# print(x)

# #using values() method
# print(d.values())
# output:
# dict_values(['fruits', 300, 100, 200])


# setdefault(key,value) method
# d={'apple': 'fruits', 'banana': 300, 'orange':100,'greps':200}
# x=d.setdefault('greps',300) #if key-value is present in dict. it return only value 200.
# print(x)
# x1=d.setdefault('mango')   #if key not in dict. insert key set value None
# print(x1)
# x3=d.setdefault('jackfruit',400) # if key-value not in dict.it insert in the dict.return value 400
# print(x3)
# print(d)
# output:
# 200
# None
# 400
# {'apple': 'fruits', 'banana': 300, 'orange': 100, 'greps': 200,
#  'mango': None, 'jackfruit': 400}

# update(dict) method or update(key-value)
# mobile={"model":10,"version":1.3}
# print("Original Dict:",mobile)
# company={"oppo":"India"}
# mobile.update(company) #merge two dict
# mobile.update(price=11999) #add key-value pair to existing dict
# mobile.update(version='1.5') #update the version value
# print("Updated Dict:",mobile)
