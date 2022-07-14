#Python have two primitive loop:
#i)While loop
#ii)For loop

#i)While loop-using while loop we can execute set of statement as long as
# condition is True.The while loop requires indexing variables to be ready

#break statement-With the break statement we can stop the loop even
# if the while condition is true:

#contineu statement-With the continue statement we can stop the current iteration,
# and continue with the next: (i.e we can skip the current value)

#With the else statement we can run a block of code once when the
# condition no longer is true:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# output:
# 1
# 2
# 4
# 5
# 6

#else condition
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

output:
1
2
3
4
5
i is no longer less than 6

#ii) For loop-A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).

#The for loop does not require an indexing variable to set beforehand.

li=[2,4,5,7,9]
for i in li:
  print(i)

# The range() function returns a sequence of numbers, starting
# from 0 by default, and increments by 1 (by default)
for i in range(0,5,1):
  print(i)

#else in for looop-The else keyword in a for loop specifies a block of code
# to be executed when the loop is finished:
for x in "banana":
  print(x)
else:
  print("Executed")

#The else block will NOT be executed if the loop is stopped by a break statement.

#Nested Loops-A nested loop is a loop inside a loop.
#The inner loop will be executed one time for each iteration of the outer loop

name= ["vijay", "amol", "sam"]
designation = ["tester", "developer", "designer"]

for x in name:
  for y in designation:
    print(x, y)

output:
vijay tester
vijay developer
vijay designer
amol tester
amol developer
amol designer
sam tester
sam developer
sam designer

#The pass Statement
#if the for loop have no content we can use pass statement for avoding error
for x in [0, 1, 2]:
  pass




