
a=10
b=10
c=10
how many object created?
A. one object is create. a,b,c 3 ref veriable is created.
same object is used hence memory utilization will be improved.

So why is a tuple immutable?
We already have lists to store collections of objects
Why do we need tuples?
Suppose you write a method that depends on a particular
sequence of objects remaining the same throughout the lifetime of the code.
If you store these objects in a list, there is a chance that some other
method using the list will accidentally alter it and thus break your method.
Thus, in a way, a tuple offers a guarantee that a particular collection of
objects will remain fixed.
