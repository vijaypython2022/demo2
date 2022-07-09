#Set is collection data type
# a Set is an unordered collection of data types that is iterable,
# mutable and has no duplicate elements.
#The major advantage of using a set, as opposed to a list
#we define set in curley braces {}
#we can define set using Set() constructor
#example
# s={3,2,5,9,11,}
#here s is set name,inside curley braces int value added

#example 2
#1)we can add multiple data type
# set1={"goa",700}
# set2={"mumbai",800}

#2) set method
# add() =Add an element to a set
# s={3,2,5,9,11}
# s.add(3)
# print("After adding element",s)

# clear()=Removes all elements form a set
# s={3,2,5,9,11}
# s.clear()
# print("After clear set:",s)

# pop()=Removes and returns an arbitrary set element.
# Raise KeyError if the set is empty
# s={2,4,5,7}
# s.pop()
# print(s)

# remove()=Removes an element from a set.
# If the element is not present in the set, raise a KeyError
# s={2,4,5,7,2}
# s.remove(4)
# print(s)

# union()=Returns the union of sets in a new set
# s={1,2,3,7,9}
# s2={7,6,8}
# x=set()
# x=union(s,s2)
# print(x)
# isupperset()=Returns True if this set contains another set

# issubset()=Returns True if another set contains this set
#
# intersection()=Returns the intersection of two sets as a new set
#
# intersection_update()=Updates the set with the intersection of itself and another
#
# difference()=Returns the difference of two or more sets as a new set
#
# difference_update()=Removes all elements of another set from this set
#
# isdisjoint()=Returns True if two sets have a null intersection
#
# discard()=Removes an element from set if it is a member.
# (Do nothing if the element is not in set)
#
# update()=Updates a set with the union of itself and others
#
# copy()=Returns a shallow copy of a set
#
# symmetric_difference()=Returns the symmetric difference of two sets as a new set
#
# symmetric_difference_update()=Updates a set with the symmetric difference of itself and another

# s=set()
# print(s)
# s.add(['50'])
# print(s)