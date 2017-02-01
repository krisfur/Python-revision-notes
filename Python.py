#!/bin/python
#statement at the top shows the computer that this is a python script - not required but useful when calling python programs from other scripts

import numpy as np #you can import something and shorten its name for easier calling in file
import pylab as ply

#comment
"""
multi line comment
"""


print('Hello neighbour') #console output - you can use 'text' or "text" - it's irrelevant but be consistent

#you can use semicolons to signify end of line but it's not useful
#can be used for many statements in one line
#print('this'); print('that')

#indentation is KEY! you need proper indentation in while, for and such things, since there are no parentheses for that - use 4 spaces
#convention: either do i=5 or i = 5 it is irrelevant, but be consistent!

#data types
#int, double, float, str, byte, bool, char etc.
#but forget that - Python automatically picks up on the datatype 

#casting
#to change datatype just use the datatype name as a function: float(something)
mate = 5
floatedMate = float(mate)
print(floatedMate)
#prints 5.0

#
print('\nNew line')
print('To use special signs use a break like \"John\'s a nice name\"')
#

#asking for input
name = input('Please state your name: ')
print('Hello ' + name)

#maths
j=5
k=6
sum=j+k
difference=j-k
power=j**k
root=sqrt(j)
absolute=abs(j-k)
#etc.
#if you don't find it in python - use numpy


#arrays
list=[1,2,3]
list2=[4,5,6]
#list operations
len(list) #length of the list
print(list[2]) #prints 2nd index so 3rd thing
print(list[-2]) #prints 2nd from the end
print(list[1:]) #prints [2,3] - slices what was before 1 - basically from 1 inclusive till the end 

list3= list1+list2
print(list3) #prints a list [1,2,3,4,5,6]
print(max(list3)) #gives highest value thingy, can use min
3 in list3 #returns True
list3.append(7) #adds 7 at the end of list3
list3.sort() #sorts from smallest to largest

#python is marvellous for using lists/arrays! but not in many dimensions really, for that use numpy


#conditionals
if(mate==5):
	print('yep')
elif:(mate<=10)
	if(mate>5):
		print('big')
	else:
		print('small')
else:
	print('nope')

#logical operators use WORDS not traditional &&, || - so 'and' 'or'
#loops

#while
i=1
while(i<=10):
	print(i)
	i+=1 #Python doesn't use the i++
	#no need to break - works like a for loop
	#to make infinite loop just don't increment
	#or make a boolean like i=True and set a condition of while(i==True):
	

#for loop works like a foreach loop in C#
list=[3,4]
for i in list:
	print(i)
#prints:
#3
#4


#defining methods/functions
def printme( str ): #use def, set function name, in perentheses put in the peremeters (as their datatypes)
	print(str) #do some stuff in the function
	return #end with return
	
	
#classes
class Employee:

	def __init__(self, name, salary):
        self.name = name
        self.salary = salary

	    def displayEmployee(self):
			print("Name : ", self.name,  ", Salary: ", self.salary)
#make a new object
emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

emp1.displayEmployee() #calles function from class using class's inside variables


#inheritance
#to make a class inherit properties of a different class:
class Boss(Employee):
	def __init__(self)
#class boss will now have all of Employee's properties and can also have some of its own




#plotting data using matplotlib
import pylab as ply #plotting library
import numpy as np #advanced mathematics library
x=[1,2,3,4,5] #data for x axis
y=[21,43,9,70,12] #unsorted data for y axis
y.sort() #sorts yep
xerr=0.25
yerr=5
ply.xlabel('X AXIS') #label of X axis
ply.ylabel('Y AXIS') #label of Y axis
np.array(x) #use mathematical library to make sure your arrays are properly formatted
np.array(y) #this step can be dropped really
ply.errorbar(x, y, xerr=xerr, yerr=yerr, marker='o', linestyle='--', color='blue', label='y(x)'
#this prepares the graph but doesn't show you anything yet, properties used will define how it looks
#you can use ply.plot for a plot without errorbars


#style info:
#linestyles: '-' solid line; '--' dashed line; ':' dotted line; '-.' dash-dotted line; 'none' no connecting lines;

#colours: 'r' red; 'b' blue; 'g' green; 'c' cyan; 'm' magenta; 'y' yellow; 'k' black; 'w' white;

#markers: '+' plus; '.' dot; 'o' circle; '*' star; 'p' pentagon; 's' square; 'x' x-sign; 'D' diamond; 'h' hexagon; '^' triangle;


y2=np.exp(x) #making data for a new graph - exp of x
y2err=2.5
ply.errorbar(x, y2, xerr=0, yerr=y2err, marker='o', linestyle='-.', color='r', label='exp(x)')

ply.ylim([0,200]) #set limits of the graph - separately ranges for x and y
ply.grid(True) #show grid or not

ply.legend() #creates the legend in the top right, can change position putting in properites inside the parentheses
ply.show() #actually makes the graph and shows it to ya
#the graph we just made shows both thingies plotted
	
	
	
	
	
	
	
	
