'''
print('5*4=',5*4,"hello",4+3)
name = "Virat"
print("name",name)

var1 = 5
print("Type of var1 is",type(var1))

var1 = 4.5
print("Type of var1 is",type(var1))

var1 = 5j # square root of -1
print("Type of var1 is",type(var1))

var1 = 5j # square root of -1
print("Type of var1 is",type(var1))
print(var1 * var1)
# square of -1 is 1
# square root of 1 is +/- 1
# square root of -1 ? = a - imaginary number i = j
# square of a will be  -1
# square of 5j ?  -25 + 0j

# 'text' "text"
var1 = "sdfiosdfsdjfkdsj"
print(var1)
print("Type of var1 is",type(var1))

var1 = True  # False
print(var1)
print("Type of var1 is",type(var1))


# write a program to calculate area of field of given length and breadth
len = 15 #metre
breadth = 20 #metre
area = len * breadth
print("Area of the given rectangle is",area,"square metre")

'''
'''
len = input("Enter length of your field: ")
print("Length = ",len," and datatype of len is",type(len))

len = input("Enter length of your field: ")
print("Length = ",len," and datatype of len is",type(len))
# by default input() will always read the value as a string
len = int(len)
# int(), float(), complex(), str(),bool()
print("Length = ",len," and datatype of len is",type(len))
breadth = int(input("Enter breadth of your field: "))
print("Breadth = ",breadth," and datatype of breadth is",type(breadth))
area = len * breadth
print("Area of the given rectangle is",area,"square metre")


#1. Write a program (WAP) to input radius of a circle and calculate area and circumference

r = float(input("Enter radius of circle : "))
pie = 3.14
area = pie * r * r
print("Area of the given Circle is",area,"square metre")
circumference = 2 * pie * r
print("Circumference of the given Circle is",circumference,"metre")



# 2. WAP to input temperature in degree Celsius and output the equivalent in F

C = float(input("Enter Temperature in Degree Celcius: "))
F = 9 * C/5 +32
print("The Above Temperature in Degree Fahrenheit is",F )



#WAP to calculate profit: given cp,sp,num_items

cp = float(input("Enter the cost price of each item: "))
sp = float(input("Enter the selling price of each item: "))
num_items = int(input("Enter the number of products: "))
tc = cp*num_items
ti = sp*num_items
profit = ti-tc
print("Total profit made by selling",num_items,"items bought at",cp,"and sold at",sp,"is",profit)
#Total profit made by selling 345 items bought at 19.0 and sold at 23.0 is 1380.0

# using f-string (formatting)
print(f"Total profit made by selling {num_items} items bought at {cp:.1f} and sold at {sp:.1f} is {profit:.2f}")


name,country,position="Virat","India","Opener"
print(f"Player {name} plays for {country} as a/an {position} in cricket one day matches.")
name,country,position="Mangbwama","Zimbabwe","Wicket-keeper"
print(f"Player {name} plays for {country} as a/an {position} in cricket one day matches.")



# text padding: fixed number of spaces
print("After text formatting:")
name,country,position="Virat","India","Opener"
print(f"Player {name:<12} plays for {country:^10} as a/an {position:>16} in cricket one day matches.")
name,country,position="Mangbwama","Zimbabwe","Wicket-keeper"
print(f"Player {name:<12} plays for {country:^10} as a/an {position:>16} in cricket one day matches.")
print(f"Player {name:*<12} plays for {country:O^10} as a/an {position:.>16} in cricket one day matches.")




#############
# Operators - arithematic operators
# ** (power)  // (integer division)  % (modulus - remainder)
num1,num2 = 10,20
print(num2 + num1)
print(num2 - num1)
print(num2 * num1)
print(num2 / num1)
print("to the Power of: ", 5 ** 3)
print("Integer part of the division",23 //4)  # integer part of the division - 5.75 = 5
print("Remainder = ",23 % 4)


# Operations on Python
print("# Arithemetic operations: input & output- numbers")
# +  -   *   /   **  //  %
num1,num2 = 10,7
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
print(num1 % num2)


print("# Comparison / relational operators: input: numbers, output: bool")
# >  <   >=  <=   ==   !=
num1,num2 = 10,7
print(num1 > num2) # True
print(num1 < num2) # False
print(num1 >= num2) # True
print(num1 <= num2) # False
print(num1 == num2) # False
print(num1 != num2) # True
print("=====SECOND======")
num1,num2 = 10,10
print(num1 > num2) # False
print(num1 < num2) # False
print(num1 >= num2) # True
print(num1 <= num2) # True
print(num1 == num2) # True
print(num1 != num2) # False
'''
'''
print("1******")
num1,num2 = 10,10
print(num1 > num2 or num1 < num2 and num1 >= num2 or num1 <= num2 and num1 == num2 or num1 != num2)
# F or F and T or T and T or F
# F or F or T or F
# T

print("2******")
num1,num2 = 10,10
print(not num1 > num2 or num1 < num2 and num1 >= num2 or num1 <= num2 and num1 == num2 or num1 != num2)
# T or F and T or T and T or F
# T or F or T or F
# T

print("3******")
print(not (num1 > num2 or num1 < num2 and num1 >= num2 or num1 <= num2 and num1 == num2 or num1 != num2))
# T or F and T or T and T or F
# T or F or T or F
# T
#NOT T
#F


# membership test operator: in, not in:
# is left side value in right side
print("a" in "Apple")
print("A" in "Apple")
print("a" not in "Apple")

'''
#### HANDLING CONDITIONS IN PYTHON #######
#  if - elif - else
'''

name = "Sachi"  # it is equal to
# wap to check if name is Sachin, then print WOW
if name == "Sachin":  # is it equal to:  ==
    print("WOW")
    print("Another WOW")
else:
    print("Name is not Sachin")
print("Thank you")



# program execution when True: 2, 4, 5, 6, 9
# execution when False: 2, 4, 7, 8, 9
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))
m6 = int(input("Enter marks in subject 6: "))


total = m1 + m2 + m3 + m4 + m5 +m6
avg = total / 6
print("Total average marks obtained is",avg)
# avg >=50 to pass or else you have failed
# conditions - choice for cond1 or cond2
# if - elif - else
if avg >=50:
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have not passed the exam.")

'''

'''
wap: to check if a number is odd or even
 odd:   1 3 5
 even:  2 4 6
'''
'''
num1 = int(input("Enter a number: "))
if num1<0:
    print("Invalid number!")
elif num1 % 2 ==0:
    print("Even number!")
else:
    print("Odd Number!")

'''
'''
WAP to calculate total and average and assign grade:
>=90: Grade A
80-90: Grade B
70-80: Grade C
60-70: Grade D
50-60: Grade E
<50: Failed
'''
'''
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))
m6 = int(input("Enter marks in subject 6: "))
total = m1 + m2 + m3 + m4 + m5 + m6
avg = total / 6
print("Total average marks obtained is",avg)

### METHOD 1:
if avg >=90:
    print("Congratulations! You have passed the exam. Your grade is A")
elif avg >=80:
    print("Congratulations! You have passed the exam. Your grade is B")
elif avg >=70:
    print("Congratulations! You have passed the exam. Your grade is C")
elif avg >=60:
    print("Congratulations! You have passed the exam. Your grade is D")
elif avg >= 50:
    print("Congratulations! You have passed the exam. Your grade is E")
else:
    print("Sorry! You have not passed the exam.")
'''

'''
wap: to check if a number is odd or even
'''
'''
num1 = int(input("Enter a number: "))
if num1<0:
    print("Invalid number!")
elif num1 % 2 ==0:
    print("Even number!")
else:
    print("Odd Number!")

'''
# Multiple conditions: more than 1 condition: if elif else
# Nested conditions: condition inside another condition
'''
if num1<0:
    print("Invalid number!")
else:
    if num1 % 2==0:
        print("Even number!")
    else:
        print("Odd Number!")


Is multiple conditions better or Nesting better?
            -ve         odd         even
Method 1:   3           5            4
Method 2:   3           6            5
'''
'''
WAP to calculate total and average and assign grade:
>=90: Grade A
80-90: Grade B
70-80: Grade C
60-70: Grade D
50-60: Grade E
<50: Failed

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))
m6 = int(input("Enter marks in subject 6: "))
total = m1 + m2 + m3 + m4 + m5 + m6
avg = total / 6
print("Total average marks obtained is",avg)

### METHOD 1:
if avg >=90:
    print("Congratulations! You have passed the exam. Your grade is A")
elif avg >=80:
    print("Congratulations! You have passed the exam. Your grade is B")
elif avg >=70:
    print("Congratulations! You have passed the exam. Your grade is C")
elif avg >=60:
    print("Congratulations! You have passed the exam. Your grade is D")
elif avg >= 50:
    print("Congratulations! You have passed the exam. Your grade is E")
else:
    print("Sorry! You have not passed the exam.")

### METHOD 2:

if avg >=50:
    print("Congratulations! You have passed the exam.")
    if avg>=90:
        print("Grade A")
    elif avg>=80:
        print("Grade B")
    elif avg>=70:
        print("Grade C")
    elif avg>=60:
        print("Grade D")
    else:
        print("Grade E")
else:
    print("Sorry! You have not passed the exam.")

'''

'''
WAP to print Fizz if the number is divisible by 3, Buzz if
divisible by 5. If they are divisible by both then print- FizzBuzz
'''

'''
num1 = 22
if num1 % 3==0 or num1 % 5==0:
    if num1 % 3 == 0 and num1 % 5 == 0:
        print("FizzBuzz")
    elif num1 % 3 == 0:
        print("Fizz")
    elif num1 % 5 == 0:
        print("Buzz")
else:
     print("Not Divisible by 3 or 5 ")


READ name, hourlyRate, hoursWorked, deductionRate
grossPay = hourlyRate * hoursWorked
deduction = grossPay * deductionRate
netPay = grossPay – deduction
WRITE name, grossPay, deduction, netPay



name=input("Enter your name = ")
hourlyRate=float(input("Enter Hourly Rate = "))
hoursWorked=int(input("Enter Hours Worked = "))

grossPay = hourlyRate * hoursWorked
if grossPay>=100:
    deductionRate=float(input("Enter Deduction Rate = "))
else:
    deductionRate = 0
deduction = grossPay * deductionRate
netPay = grossPay - deduction
print("********************************")
print("Name = ",name)
print("Gross Pay = ",grossPay)
print("Deduction = ",deduction)
print("Net Pay = ",netPay)
print("********************************")

'''
'''
## to pass, user has to get at least 35 in each of the three subjects
m1 = int(input("Enter the marks in subject 1: "))
m2 = int(input("Enter the marks in subject 2: "))
m3 = int(input("Enter the marks in subject 3: "))
if m1>=35:
    if m2 >= 35:
        if m3 >= 35:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Failed in Subject 2")
else:
    print("Failed in Subject 1")

num1,num2,num3 = 15,17,11

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else: # num2 > num1
    if num2 > num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")

'''
'''
#### LOOPS   ###########

# Loops in Python: while and for
# range(start, end, increment) - generates range of values -
# start is inclusive and end is not (upto)
# range(2,10,2): 2, 4,6,8
print("    ===>  1.")
for i in range(2,10,2):
    print("Hello : i=",i)
print("    ===>  2.")
# range(start, end)  # increment is default 1
for i in range(2,6):
    print("Hello there: i=",i)
print("    ===>  3.")
# range(end)  # start is default 0, increment is default 1
for i in range(5):
    print("Hello there: i=",i)
###
for i in range(5):
    print("*")

### above program using while loop
print("       ======== While 1: ")
count = 5
start = 0
while start < count:
    print("Hello : start =",start)
    start+=1   # start = start + 1

num = 5
for i in range(5):
    print("*")

for i in range(5):
    print("*",end=" ")
print()
print("Hello")

'''
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

'''
for count in range(5):
    for i in range(5):
        print("*",end=" ")
    print()


* 
* * 
* * *  
* * * *  
* * * * * 

for count in range(5):
    for i in range(count+1):
        print("*",end=" ")
    print()


* * * * * 
* * * *  
* * * 
* * 
* 

for count in range(5):
    for i in range(5-count):
        print("*",end=" ")
    print()


* * * * * 
 * * * *  
  * * * 
   * * 
    * 

for count in range(5):
    for i in range(count):
        print(" ",end="")
    for j in range(5-count):
        print("*",end=" ")
    print()


* * * * * 
  * * * * 
    * * * 
      * * 
        * 

for count in range(5):
    for i in range(count):
        print(" ",end=" ")
    for j in range(5-count):
        print("*",end=" ")
    print()




# While

5
4
+
9
6
4
-
2
q

print("Menu")
print("+ to add")
print("- to subtract")
print("* to multiply")
print(" / to divide")
print("q to quit")
print("Keep on entering first 2 values followed by option from above!")

while True:
    n1 = input()
    if n1=="q":
        break
    else:
        n1=int(n1)

    n2 = input()
    if n2=="q":
        break
    else:
        n2=int(n2)

    op = input()
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    elif op=="q":
        break
    else:
        print("...na...")


'''
'''
WAP to generate prime numbers as long as
user hits enter, any other key to stop the program

2
3
5
7
q

'''
'''
num = 2
while True:
    isPrime = True
    for i in range(2,num//2+1):
        if num % i==0:
            isPrime = False
            break
    if isPrime:
        print(num,end="")
        inp = input()
        if len(inp)!=0:
            break
    num+=1 # num = num + 1
###
##
'''

'''
print("Using For loop:\n")
max_pattern = 5
for i in range(max_pattern):
    for j in range(max_pattern):
        print("*",end=" ")
    print()
print("Using While loop:\n")
outer_counter = 1
while outer_counter <=max_pattern:
    inner_counter = 1
    while inner_counter <= max_pattern:
        print("*", end=" ")
        inner_counter+=1
    print()
    outer_counter+=1

'''
'''
import random
print(random.random())
print(random.randint(1,100))

'''

'''
Develop guess a number game: Computer to think and Human to guess
module: its a python file which collection of functions
import: indicating to python that I want to use functions available in the given module
'''
'''
import random

attempt = 1
num=random.randint(1,100)
while True:
    inp = int(input(f"Attempt {attempt}: Guess the number (1 to 100): "))
    if inp == num:
        print(f"Congratulations! You win in {attempt} attempts!")
        break
    elif inp < num:
        print("Sorry, thats incorrect, try guessing a higher value")
    else:
        print("Sorry, thats incorrect, try guessing a lower value")
    attempt+=1
    if attempt>10:
        print("Sorry! You lose")
'''

'''

'''
# Develop guess a number game: Computer to think and Computer to guess
# module: its a python file which collection of functions
# import: indicating to python that I want to use functions available in the given module
'''
import random
max_try = 9000
max_attempt, min_attempt = 0,9999
total_attempts = 0
for i in range(max_try):
    attempt = 1
    start,end=1,100
    num=random.randint(1,100)
    while True:
        #inp = int(input(f"Attempt {attempt}: Guess the number (1 to 100): "))
        inp = random.randint(start,end)
        if inp == num:
            print(f"Congratulations! You win in {attempt} attempts!")
            total_attempts+=attempt  #storing all the sum of attempts
            if attempt > max_attempt:
                max_attempt = attempt
            if attempt < min_attempt:
                min_attempt = attempt
            break
        elif inp < num:
            print("Sorry, thats incorrect, try guessing a higher value")
            start=inp+1
        else:
            print("Sorry, thats incorrect, try guessing a lower value")
            end = inp-1
        attempt+=1
        if attempt>300:
            print("Sorry! You lose")

print("Max attempt was",max_attempt)
print("Min attempt was",min_attempt)
print("Average attempts = ",total_attempts/max_try)
###  ###########

'''

# str1 = "hello"
# str2 = 'Hi there'
# str3 = '''#I am fine
# I am here
# I going there'''
# str4 = """How are you?
# Where are you?
# Where are you going?"""
# assign multiline text to triple quotes
# print(str3)

'''
# + *
print("I am "+"fine")
print("I am "+"running")
print("I am "+"fine"*3)
print(("I am "+"fine")*3)

for i in range(5):
    print("* "*5)

for i in range(5):
    print("* "*(i+1))

j=1
while j<=5:
        print("* "*j)
        j=j+1

str1 = 'aeiou'
for i in str1:
    print("Hello:",i)

str1 = 'i am fine how are you?'
# get part of the given string
# counting in python starts from 0
# how to get a part of a string - []
print("4th char: ",str1[3])
print("10th char:",str1[9])

# counting happens both ways: left to right and also r to l
# left to right: 0,1,2,3...
# right to left: -5,-4,-3,-2,-1
print("last char: ",str1[-1], str1[len(str1)-1])
print("second last char: ",str1[-2], str1[len(str1)-2])
print("Length of HELLO =",len("HELLO"))


# strings are immutable - cant be edited
str2='HELLO'
#str2[1] ='Y'  # TypeError: 'str' object does not support item assignment
str1 = 'i am fine how are you?'
# how to get continuous set of values
# to get continuous set use : colon var[start:end:increment]
print("first 3 characters of str1:",str1[0:3],",",str1[:3],",",str1[0:3:1],",",str1[-len(str1):-len(str1)+3])
print("5 to 8 characters of str1:",str1[4:8],",",str1[4:8:1])
print("===> ",str1[3:16:3])
print("last 3 char:",str1[len(str1)-3:len(str1)],",",str1[-3:])
print("Entire: ",str1[:])

'''

'''
Strings - indexing in the last session
This session, we will look at the some of the methods of string class
'''
'''
txt1 = "Hello"
txt2 = "Hi"
print(txt2 + txt1 *5)
print((txt2 + txt1) *5)

txt1 = "I am fine"

# methods which starts with .is...() - True or False
print(txt1.isalnum())
print(txt1.isdigit())
'''
'''
length = input("Enter the length: ")
if length.isdigit():
    length = int(length)
else:
    print("Invalid length value, setting it to 0")
    length = 0
print("============")
print(length, "Type:", type(length))
print("============")
'''
'''
txt3="                     "
print(txt3.isspace())
txt3 = "i m fine how r u?"
print(txt3.islower())
print(txt3.isupper())
print(txt3.istitle())

print("Title case of txt 3: ",txt3.title())
print("Lower case of txt 3: ",txt3.lower())
print("Upper case of txt 3: ",txt3.upper())

# strip() will remove blank spaces before and after the text
txt3 = "      i      m          fine            "
print("Strip: ",txt3.strip())

print("Split: ",txt3.split())

txt3 = "I am FINE HOW I AM DOING"
print("Split2: ",txt3.split())
print("Split3: ",txt3.split("I"))
'''
'''
val1 = ['How','are','you','doing?',"I",'am','fine.']
val2 = " ".join(val1)
print("Val2 = ",val2)

print(val2.find("doing"))
print(val2.find("doingo"))
print(val2.find("doing",5,16))
val3 = "How are you doing? doing well. I am doing fine."
print(val3.find("doing",13))
print(val3.count("doing"))


print('R -Find: ',val3.rfind("doing"))
start = 0
for i in range(val3.count("doing")):
    pos = val3.find("doing",start)
    print("Found at pos:",pos)
    start = pos + 1

print(val3.replace("doing","eating"))
print(val3) # strings are immutable
val3 = val3.replace("doing","eating",3)
print(val3)

## COLLECTIONS - handling multiple values by a single variable
#<class 'list'>
l0 = [10]
l1 = [3,6,8.5,12,"Hello",True, 5j, [4,8,12]]
print(l1, type(l1))
print("First and last member: ",l1[0],l1[-1])
a = l1[-1]
print(a[1],l1[-1][1])


print("============= 1 =========")
for i in l1:
    print(i)

print("============= 2 =========")
for i in range(len(l1)):
    print(i, l1[i])

print("============= 3 =========")
print([1,2,3] + [5,6,7] + [2,3,5,7])
print([1,2,3] + [5,6,7]*2 + [2,3,5,7])

# list is mutable
l1 = [3,6,9]
l1[2] = 12
print(l1)
l0 = []

# append(), insert() - to add members to existing list
l1.append(18) # always add at the end of the list
print("L1 after append 1: ",l1)
l1.append(15)
print("L1 after append 2: ",l1)
# insert() - add at the given position
l1.insert(3,21) # index, value
print("L1 after insert: ",l1)

# pop() remove()
l1.pop(1)  # needs index to delete
l1.pop(-1)
print("l1 after pop:",l1)
l1.remove(18)  #needs value to delete
print("l1 after remove:",l1)

'''
'''

print("**************")

l1= [4,5,6,4,7,8,4]
print(l1.count(4))
l2 = l1.copy()  # it creates a new copy (photocopy)
l3 = l1  # they both point to same list
print("1 Print:")
print(l1,"\n",l2,"\n",l3)
l1.append(11)
l2.append(22)
l3.append(33)
print("2 Print:")
print(l1,"\n",l2,"\n",l3)

print("***********")

l3.reverse()
print("L1 after reverse: ",l1)
l3.sort() # sort in ascending order
print("L1 after sort: ",l1)
l3.sort(reverse=True) # sort in descending order
print("L1 after sort: ",l1)

l3.clear()
print("after clear: ",l1)
del l1
#print("after clear: ",l1) #NameError: name 'l1' is not defined.
l1 = [10,20,30,40]
l2.extend(l1)  # l2 = l2 + l1
print("After Extend:", l2)

'''
'''
#Implementation of queue: FIFO Data Structure : First in first out
Queue=[]

while True:
    print("1. Add value")
    print("2. Remove value")
    print("3. Display the value")
    print("4. Quit")
    ch = input("Enter your choice:")
    if ch=="1":
        val = input("Enter the value: ")
        Queue.append(val)
    elif ch=="2":
        if len(Queue) == 0:
            print("Empty Queue - nothing to delete!")
            continue
        print(Queue[0],"removed!")
        Queue.pop(0)
    elif ch=="3":
        if len(Queue)==0:
            print("Empty Queue!")
            continue
        for v in Queue:
            print(v,end=" <- ")
        print()
    elif ch=="4":
        print("Thank you")
        break
    else:
        print("Invalid option")
'''
'''
## STACK IMPLEMENTATION - using list
# LIFO - last in first out
Stack = []
while True:
    print("1. Add value")
    print("2. Remove value")
    print("3. Display the value")
    print("4. Quit")
    ch = input("Enter your choice:")
    if ch=="1":
        val = input("Enter the value: ")
        Stack.insert(0,val)
    elif ch=="2":
        if len(Stack)==0:
            print("Stack is empty - nothing to remove!")
            continue
        Stack.pop(0)
    elif ch=="3":
        if len(Stack)==0:
            print("Stack is empty!")
            continue
        print("TOP:")
        for v in Stack:
            print(v)
        print("====")
    elif ch=="4":
        print("Thank you")
        break
    else:
        print("Invalid option")
'''
'''
#################
# tuples
t1 = ()
print(type(t1))

t2 = (2,)
print(type(t2))

t3 = (45,6.7,True,"Hello",(1,2,3),[2,4,5])
print(type(t3))

t3 = (45,6.7,True,"Hello",(1,2,3),[2,4,5])

for i in t3:
    print(i)
'''
'''
t3 = (45,6.7,True,"Hello",(1,2,3),[2,4,5])

# Indexing is also exactly like String and List
print(t3[0],t3[1],t3[-1])

#tuples are not mutable -  immutable
#t3[1] = 5
# #TypeError: 'tuple' object does not support item assignment
print(t3.count(45))
print(t3.index(45))

# u can convert list to tuple and tuple to list
t3=list(t3)
t3 = tuple(t3)

t1 = (4,8,12)
t2 = (4,6, 64, 66)
if t1 > t2:
    print(t1," is greater")
elif t2 > t1:
    print(t2,"is greater")
else:
    print("They are equal")
#################
# LIST - linear ordered mutable collection
# Tuple - linear ordered immutable collection
# Dictionary:  unordered mutable collection
d1 = {}
print(type(d1))
d1 = {3:"Hello",'Runs':3000}
print(d1[3])
print(d1['Runs'])
'''
'''
# Dictionary
d1 = {1:"Sachin","City":"Mumbai","Runs":45000}
d1.update({"Team":"MI"})
print(d1, type(d1))
'''
'''

'''
# WAP to get marks of 3 students in 3 subjects
# {1024:[],1026:[],[],[],[]}
'''
sub_list = ['Maths','Science','Social Studies']
main_dict = {}
n_students, n_subjects = 3,3
for roll in range(n_students):
    roll_no = input("Enter the roll number of student "+str(roll+1)+": ")
    temp_list = []
    for sub in range(n_subjects):
        marks = int(input("Enter the marks for subject " + sub_list[sub] + ": "))
        temp_list.append(marks)
    temp_dict = {roll_no:temp_list}
    main_dict.update(temp_dict)

print("Printing the details:\n",main_dict)
'''

'''
# {'1021': [78, 98, 82], '1029': [90, 87, 99], '67': [56, 49, 60]}
D1 = {'1021': [78, 98, 82], '1029': [90, 87, 99], '67': [56, 49, 60]}

# Dictionaries are mutable - edit the values
D2 = D1  # they point to the same dictionary
D3 = D1.copy() # creating a photocopy

D1.update({'1045':[59,89,79]})
print("D1: ",D1)
print("D2: ",D2)
print("D3: ",D3)


print("Keys = ",D1.keys())
print("Values = ",D1.values())
print("Items = ",D1.items())  # [(key,value),(),()]

print("==================")

# calculate avg marks for all the students
D1:  {'1021': [78, 98, 82], '1029': [90, 87, 99], '67': [56, 49, 60], '1045': [59, 89, 79]}

avg_marks = []
for marks in D1.values():
    avg_marks.append(sum(marks)/3)

avg_marks2 = {}
for roll,marks in D1.items():
    avg_marks2.update({roll:sum(marks)/3})
print("avg_marks:", avg_marks)
print("avg_marks2:" ,avg_marks2)

print("===================")

D1 = {'1021': [78, 98, 82], '1029': [90, 87, 99], '67': [56, 49, 60],
      '1045': [59, 89, 79], '1049': [59, 89, 79]}

print(D1['67'])
# keys will be unique
D1.pop('67')  # pop takes the key
print("D1 after pop:",D1)
D1.popitem() # last updated value
print("D1 after popitem:",D1)
D1.clear()
print(D1)
'''

# sets : linear unordered collection which doesn't allow duplicates
'''
s1 = {A, B, C, G, M}
s2 = {M,G,B,A,C}
s3 = {P,P,P,P,P}
'''
'''
s1 = {4,6,8,4,6,8,12,14,18,4,6,8,12}
print(type(s1), s1)
'''
'''
# operations: union, intersection, difference
s1 = {1,2,3,5,7,9}
s2 = {2,3,4,6,8,10}
print("Union:")
print(s1.union(s2))
print(s1|s2)
print("Intersection:")
print(s1.intersection(s2))
print(s1&s2)
print("Difference:")
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
print("Symmetric Difference:")
print(s1.symmetric_difference(s2))
print(s1^s2)

# union: c= a |b  update: a =a|b
# c=a&b  intersection_update  a=a&b
# difference update a = a-b
# symdiff update a=a^b

print("===================")

print(s1.issuperset(s1))
print(s1.issubset(s1))
print(s1.isdisjoint(s2))

print("===================")

print(s1)
s1.pop()
print("S1 after pop: ",s1)
s1.remove(7)
print("S1 after remove: ",s1)

print("===================")

s1 = {1, 2, 3, 5, 7, 9}
# sets, lists, tuples - can be converted into each others format
s1 = list(s1)
l1 = [4,4,5,6,4,3,6,7,9,10,4,5,10,7,9]
l1 = list(set(l1))
print(l1)

'''
'''
# inbuilt/predefined functions - len(), print(), input()...
# user defined functions - u give a name to few lines of code
#definition and usage- define once and use it multiple times
#definition is like giving meaning to the function

#Module is a collection of functions

#import p18

#filename.myquestions()

## THIS IS SAVED AS p18 filename

# using local and global variable
# docstring - multiline comment added as first line in a function
'''


def somesome():
    '''
    this function demonstrates working of global and local variables
    :return: doesnt return any value

    '''

    # global a,b
    # print(a+b)
    # a = 3  # local variable
    # b = 33  # local variable
    # print(a+b)


'''
def myquestions():
    print("Q1. What's your name?")
    print("Q2. Where are you?")
    print("Q3. What do you do?")
    print("Q4. What do you need?")
    print("Q5. Why are you doing?")


#function without input parameters
def my_add():
    num1,num2 = 5,7
    total = num1 + num2
    print("Total is",total)

# taking in 2 parameters /arguments
def my_add1(num1,num2):
    total = num1 + num2
    print("Total is",total)

# function with return
def my_add2(num1,num2):
    total = num1 + num2
    #print("Total is",total)
    return total

if __name__=="__main__":
    #calling code
    myquestions()
    print("calling again...")
    myquestions()
    print("one more time...")
    myquestions()

    my_add()
    my_add1(30,40)
    my_add1(3,24)
    tot = my_add2(3,24)
    print(f"I have {tot} chocolates")

    a,b=5,55  #global variable
    somesome()
    help(somesome)  # prints docstring
    print("================")
    help(print)
    print("================")
    help(input)
    print("================")
    help(len)
'''
'''
# Functions
def myadd1(num1,num2):
    print("Num1 =",num1)
    print("Num2 =", num2)
    total = num1 + num2
    print("Total =",total)

def myadd2(num1, num2=10):
    print("Num1 =",num1)
    print("Num2 =", num2)
    total = num1 + num2
    print("Total =",total)

def myadd3(num1=21, num2=10):
    print("Num1 =",num1)
    print("Num2 =", num2)
    total = num1 + num2
    print("Total =",total)

# 1 required arguments - you have to pass
# 2 positional arguments - left to right values
# 3 default arguments : non-required
# 4 Keywords : non-positional

print("1")
myadd1(10,30)
print("2")
myadd2(7)
print("3")
myadd3()
print("4")
myadd1(num2=10,num1=30)

print("=================")

def mycalc(side1,side2=0):
    if side2==0:
        area= side1 * side1
        peri = 4*side1
        print(f"Area and Perimeter of the given square is {area} and {peri}")
    else:
        area = side1 * side2
        peri = 2 * (side1+side2)
        print(f"Area and Perimeter of the given rectangle is {area} and {peri}")

print("Calculates for Rectangle(l and b req)")
mycalc(10,5)
print("Calculates for Square(only 1 side req)")
mycalc(21)

print("another example")
def somesome(var1,var2):
    print("Var1 = ",var1)
    print("Var2 = ", var2)

somesome([2,4,6,8,10,12,14], {3,5,7,9})

print("=================")

#variable length arguments
def varlenfunc(*var1):
    print("varlenfunc: ")
    print("Var1 = ",var1)

print("******eg1*******")
varlenfunc(3,5,7,9,11,14,15,16)

def varlenfunc2(*var1, **var2):
    print("varlenfunc: ")
    print("Var1 = ",var1)
    print("Var2 = ", var2)
    main_story = ""
    if "name" in var2.keys():
        main_story+="My name is "+var2['name']+". "
    if "game" in var2.keys():
        main_story += "I love to play " + var2['game'] + ". "
    if "place" in var2.keys():
        main_story+="I live in "+var2['place']+". "
    print("My Story:\n",main_story)


print("*******eg2*********")
varlenfunc2(3,5,7,9,11,14,15,16,name="Sachin",game="Cricket",place="Mumbai")

print("*********eg********3")
varlenfunc2(name="Laxman",place="Hyderabad")
# plot -title, subtitle,x label, y label,

print("*****************")

def c_to_f(value):
    print("Temperature in F will be calculated here.")

def f_to_c(value):
    print("Temperature in C will be calculated here.")

def convert_temp(value,type):
    type(value)

def convert_temp2(value,type):
    if type==1:
        c_to_f(value)


print("******* eg 1 **********")
convert_temp(40,c_to_f)
print("******* eg 2 **********")
convert_temp(40,f_to_c)
print("******* eg 3 **********")
convert_temp2(50,1)

print("*****************")

'''
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
'''
def factorial_recur(n):
    if n==0:
        return 1
    return n *factorial_recur(n-1)
'''
# f(5): 5 * 4 * 3 * 2 * 1 * 1
'''
result = factorial_recur(5)
print("Factorial of 5 is",result)

print("**************************")

#lambda function - oneline function - anonymous function
myfunc1 = lambda x,y: x+y

res = myfunc1(10,30)
print(res)

print("**************************")
'''
# Properties of list:
# 1. MAP: to apply same logic over a large values in a list
# 2. FILTER: to filter out subset of values from large values in a list
# 3. REDUCE: apply a logic to reduce large values of list into one
'''

#MAP
list_inr = [5800,4500,8900,1234,5436,6789,9876,5634,2390]
list_usd = []
for i in list_inr:
    list_usd.append(round(i/80.5,1))
print("Loop: ",list_usd)

# map takes function and the list of values
res = list(map(lambda x:round(x/80.5,1),list_inr))
print("Map : ",res)

print("**************************")

#FILTER: filter out
# filter out value
list_inr = [5800,4500,8900,1234,5436,6789,9876,5634,2390]
res = list(filter(lambda x:x%10==0,list_inr))
print("Filter : ",res)

print("**************************")


# Reduce

Method 1 of importing modules and functions:
import functools
functools.reduce()

Method 2:
import functools as ft
ft.reduce()

in methods 1 and 2, all the functions/methods/classes of the module
is available to use
if you dont want to import all of them, then use method 3 as shown below

from functools import reduce
res = reduce(lambda x,y: x+y,list_inr)
print("reduced to",res)

print("**************************")

import math
print(math.ceil(5.001))
print(math.floor(5.999))
rad = 5
print("Area of circle =",math.pi *(rad**2))
print("Area of circle =",math.pi *(math.pow(rad,2)))
print("factorial of 5 =",math.factorial(5))

print("**************************")

import sys
print("System path =",sys.path)

print("**************************")

import datetime as dt
print("current time = ",dt.datetime.now())
print("current year = ",dt.datetime.now().year)
print("current month = ",dt.datetime.now().month)
print("current hour = ",dt.datetime.now().hour)

print("**************************")

import random
print(random.random())  # 0-1
print(random.randint(100,110))
print(random.randrange(1,20,3))  # 1,4,7,10,13,16,19
values = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
random.shuffle(values)
print(values)
print(random.choice([1,2,3,4,5,6]))
'''

'''
#Class and Objects
'''
# Properties:  variables and functions
# Types: class level and object level
#: class variables, class functions, object variables, object functions

'''
class Books:
    book_count = 0

    # __init__() - method which is called automatically when we create object
    def __init__(self,title,pages):
        self.title = title
        self.page = pages
        Books.book_count+=1

    def put_details(self):
        print(f"Title of the book is {self.title} and it has {self.page} pages")

    @classmethod
    def book_population(cls):
        print("Total number of books =",cls.book_count)

book_list=['Python Programming',"Data Visualization", 'Machine Learning','Deep Learning']
page_list=[350,450,550,650]
b1 = Books(book_list[0], page_list[0])  #__init__() is called
b2 = Books(book_list[2], page_list[2])  #__init__() is called
b3 = Books(book_list[3], page_list[3])  #__init__() is called
b4 = Books(book_list[1], page_list[1])  #__init__() is called
print(type(b2))

b3.put_details()
b1.put_details()
b2.put_details()
b4.put_details()
print("************")
print(b1.book_count)
print(b2.book_count)
print(b3.book_count)
print(Books.book_count)
b3.book_population()
print("*******************")

##  ####  ####
#Properties of classes
##  ####  ####
'''
# access modifiers:
# 1. Public: public members can be called by any other class
# 2. Protected members: can be called by derived classes but not by
#    other classes. declared using: _membername PYTHON DOESNT STRICTLY IMPLEMENTS THIS
# 3. private members: it can be called by same class. private members are
#    declared using __membername

'''
class Books:
    def _show_data(self):
        print("This is Books")
    def __data_books(self):
        print("This is Books Data")
class Magazines (Books):
    def show_data(self):
        print("This is Magazines")

    def data_magazines(self):
        print("This is Magazines Data")

class Journals:
    def show_data(self):
        print("This is Journals")
    def data_journals(self):
        print("This is Journals Data")

b1 = Books()

print("********")
m1 = Magazines()
print("********")
#m1.data_books()
m1.show_data()
print("********")
j1 = Journals()
j1.show_data()
print("********")
'''

#############################
## types of errors:
'''
1. Syntax error: dont follow the rules of programming. Program will not run with
    this error. Easiest to find and fix
2. Logical error: python cant capture this error, most difficult to fix
3. Runtime error / exceptions: errors that occur at runtime/execution of the program

'''
a = 25
people = int(input("Enter number of people: "))
print(a / people)

# ZeroDivisionError
# ValueError
'''
1. predict which lines can give error and which errors
e.g. line # 10 can give ValueError
e.g. line # 11 can give ZeroDivisionError

2. Get access to the exception using TRY
    put the suspected lines into try block

3. Handle it using error code
    e.g. except ValueError, except ZeroDivisionError, except Exception

4. else:
    executes when there is not exception

5. finally:
    both the cases - error or no error this part is called

'''
a = 25
try:
    people = int(input("Enter number of people: "))
    parts = a / people

except ValueError:
    print("You have not entered a valid number, so we change the value to 1")

    people = 1
    parts = a / people
except ZeroDivisionError:
    print("Zero people cant be accepted so setting it to 1")
    people = 1
    parts = a / people
except Exception:
    print("Some error has occurred not sure what!!!")
else:  # when there is no error
    print("No error has occurred")

finally:
    print(f"Each people will get {parts} pieces")

print("Thank you")

path = "abcabc.txt"
'''
file mode:
r : read
w : write
a : append

'''
try:
    file_handle = open(path, "r")
except FileNotFoundError:
    print("Existing file not found")


else:
    file_handle.close()

# option 2
path = "abcabc2.txt"
'''
file mode:
r : read
w : write
a : append

r+ : read & write
w+ : write & read
a+ : append & read
'''
'''
try:
    file_handle = open(path,"w+")
except FileNotFoundError:
    print("Existing file not found")
    file_handle = open(path, "w")


finally:
    file_handle.close()
'''

# print("Hello World")


'''
basic programming - how to solve simple using: variables,
    arithmetic, comparison, logicals operators
conditions in Python - if -elif - else
loops - iterate / repeat the block of code - for & while
collections - list, tuple, dictionary & sets
functions - block of code to perform certain task - you cant execute it
independently, call it when and where required.
class & objects -
handling files - text files
error handling
working with database

Numpy & Pandas are extension of collections

MATRIX Notes: https://www.britannica.com/science/matrix-mathematics

'''
import numpy as np

'''
to install Python, goto Python home at command prompt / terminal and install it using:
pip install numpy
'''
# convert range of values into numpy matrix
x = range(16)
x = np.reshape(x, (4, 4))  # (rows,columns)
print(x)

'''
# convert 2-D list into matrix
l1 = [[2,3,1,5],[3,5,1,2],[2,3,5,1]]
print(l1)
l1 = np.array(l1)
print(l1)

## indexing of numpy
print(x[0], x[2])
print(x[:,0])
#3rd row 2nd col
print(l1[2,1])

# functions to create standard matrix
m1 = np.zeros((2,4))
print(m1)
print("Dtype = ",m1.dtype)
m1 = np.zeros((2,4), dtype=int)
print(m1)
print("Dtype = ",m1.dtype)
m1 = np.ones((3,4))
print(m1)
m1 = np.full((3,4),8)
print(m1)
print("Shape of M1 Matrix is",m1.shape)
print("Dtype = ",m1.dtype)

#### Numpy operations - add, subtract, multiplication, division
'''

print("Hello World")

