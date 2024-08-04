'''
#Program 1 : Addition of Two Numbers
N1 = int(input("Enter Any Number N1: "))
N2 = int(input("Enter Any Number N2: "))
S=N1+N2
print("Sum of Two Numbers is",N1,"+",N2,"=",S)
'''

'''
#Program 2 : Comparison of Two Numbers
A = int(input("Enter Any Number A: "))
B = int(input("Enter Any Number B: "))
if A>B :
    print("A =",A)
else :
    print("B =",B)

'''
'''
#Program 3 : Temperature in Degree Celcius to Degree Fahrenheit 

C = float(input("Enter Temperature in Degree Celcius: "))
F = 9 * C/5 +32
print("The Above Temperature in Degree Fahrenheit is",F )
'''
'''
# Program 4 : Temperature in Degree Fahrenheit to Degree Celcius

F = float(input("Enter Temperature in Degree Fahrenheit: "))
C = (F - 32) * 5 / 9
print("The Above Temperature in Degree Celcius is", C)
'''
'''
# Program 5 : program that converts inches to centimeters
i = float(input("Enter length in Inches: " ))
c = 2.54 * i
print("The above length in Centimeters is",c,"Centimeters")
'''
'''
# Program 6 : program that converts centimeters to inches
c = float(input("Enter length in Centimeters: " ))
i = c / 2.54
print("The above length in Inches is",i,"Inch")
'''
'''
#Program 7 : program to check student is pass or fail
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

'''

'''
#Program 8 : Above program using and
m1 = int(input("Enter the marks in subject 1: "))
m2 = int(input("Enter the marks in subject 2: "))
m3 = int(input("Enter the marks in subject 3: "))
if m1>=35 and m2>=35 and m3>=35 :
    print("Pass")
else :
    print("Fail")
'''

'''
#Program 8 : Program to find sum of n numbers #starts from 1

n = int(input("Enter the number: "))
sum = 0
i=1
while n>=i :
    sum = sum + i
    i+=1
print(f"Sum of the first {n} numbers is,{sum}")

'''
'''
#Program 9 : Program to read characters until user enters z

while True :
    c = input("Enter your input: ")
    if c == "z" or c == "Z" :
        print(f"You entered {c} Program ends here")
        break
    else :
        str(input("Enter your input: "))
'''

'''
#Program 10 : Program to check person is senior citizen or not
print("Enter Your Name followed by Age to check You are Senior Citizen or not, Enter q to quit the program.")
while True:
    name = input("Enter Your Name : ",)
    if  name == "q" :
        break
    else:
        age = int(input("Enter Your Age : ", ))
        if age>=60 :
            print(f"Your Age is, {age} ,That's why, {name}, you are Senior Citizen")
        else :
            print(f"Your Age is, {age},That's why, {name}, you are not Senior Citizen")
            print("You have to wait for",60-age,"more year's to be a Senior Citizen" )
'''


'''
#Program 11:
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

#Exercise 1:
'''
def find_cubes(n):
    cubes = []
    for i in range(1, int(n ** (1/3)) + 1):
        cube = i ** 3
        cubes.append(cube)
    return cubes

def check_ramanujan_hardy_number(n):
    cube_pairs = []
    cubes = find_cubes(n)
    for i in range(len(cubes)):
        for j in range(i+1, len(cubes)):
            if cubes[i] + cubes[j] == n:
                cube_pairs.append((i+1, j+1))
    return cube_pairs

# Test the function
number = int(input("Enter a number to check if it's a Ramanujan Hardy number: "))
pairs = check_ramanujan_hardy_number(number)

if pairs:
    print(f"{number} is a Ramanujan Hardy number.")
    print("Cube pairs are:")
    for pair in pairs:
        print(pair)
else:
    print(f"{number} is not a Ramanujan Hardy number.")
'''
'''
#Program 12: Swap commas and dots in a String
A = "Aditya,Atharva,Nimish,Utkarsha"
print(str(A).replace("Aditya,Atharva,Nimish,Utkarsha","Aditya.Atharva.Nimish.Utkarsha"))
print(A)
'''
'''
#Program 13: Program to convert String to a List
A = "Aditya,Atharva,Nimish,Utkarsha"
print(str(A).split())
'''
'''
#Program 14: Count and Display vowels in a string

A = input("Enter any String:")
vowels = 'aeiouAEIOU'
count = 0
for char in A:
    if char in vowels :
        count+=1
        print(char,end=",")

print(f" Are the Vowels In a Given String and there are {count} vowels.")
'''
'''
print("Hello World")

a=5
b=2
print(a+b)

a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
print("Addintion of A and B=",a+b)
'''

'''
'''
#working with large dataset: hotel_bookings dataset

'''
import pandas as pd
import numpy as np
file="https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/hotel_bookings.csv"
#file="D:/datasets/gitdataset/hotel_bookings.csv"
df = pd.read_csv(file)
print("size of dataset: ",df.shape)
print("datatypes of dataset: \n",df.dtypes)

df_numeric = df.select_dtypes(include=[np.number])
df_objects = df.select_dtypes(exclude=[np.number])
print("Numeric columns:\n",df_numeric)
print("Object columns:\n",df_objects)

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
sns.heatmap(data=df.isnull(), cmap=sns.color_palette(['#F7CB06','#EE4B2B']))
plt.show()

# go through each column and find the number of missing values
print("1. checking all missing values")
for col in df.columns:
    pt_miss = np.mean(df[col].isnull())*100
    if pt_miss > 0.0:
        print(f"{col} - {pt_miss}")

# columns with more than 70% missing:
print("3. checking again after dropping columns")
for col in df.columns:
    pt_miss = np.mean(df[col].isnull())*100
    if pt_miss > 0.0:
        print(f"{col} - {pt_miss}")
        df[f'{col}_Missing']=df[col].isnull()

### ERROR fixed - use commented line instead of commented one
# now lets turn our attention to the rows
ismiss_cols = [col for col in df.columns if '_Missing' in col]
df['Num_Missing'] = df[ismiss_cols].sum(axis=1)
#df['Num_Missing'].value_counts().reset_index().sort_values(by="index").plot.bar(x='index', y="Num_Missing")
df['Num_Missing'].value_counts().sort_index().plot.bar(x='index', y="Num_Missing")
plt.show()


# columns with more than 70% missing:
print("2. checking columns > 70% missing")
for col in df.columns:
    pt_miss = np.mean(df[col].isnull())*100
    if pt_miss > 70.0:
        print(f"{col} - {pt_miss}")
#company is the result
cols_to_drop = ['company']
# axis = 0 - look for the values in the rows
# axis = 1 - look for the values in the columns
df = df.drop(cols_to_drop,axis=1)

ind_missing = df[df['Num_Missing']>12].index
print("Rows with more than 10 missing values:\n",ind_missing)
df = df.drop(ind_missing,axis=0)

## after dropping rows and columns check again for missing values:
print("11. checking all missing values")
for col in df.columns: # ['A','B','C']
    pt_miss = np.mean(df[col].isnull())*100
    if pt_miss > 0.0:
        print(f"{col} - {pt_miss}")

'''
#children - 2.0498257606219004 - numeric
#babies - 11.311318858061922 - numeric
#meal - 11.467129071170085 - categorical
#country - 0.40879238707947996 - categorical
#deposit_type - 8.232810615199035 - categorical
#agent - 13.687005763302507 - categorical
'''
# replace missing numeric values
avg = df['children'].mean()
df['children'] = df['children'].fillna(avg)
med = df['babies'].median()
df['babies'] = df['babies'].fillna(med)
# replace with specific values
#df['babies'] = df['babies'].fillna(-99)

#convert them into categorical calues
df['agent'] = pd.Categorical(df.agent)
df['meal'] = pd.Categorical(df.meal)
df['country'] = pd.Categorical(df.country)
df['deposit_type'] = pd.Categorical(df.deposit_type)

# lets recreate numeric and object sets of columns
df_numeric = df.select_dtypes(include=[np.number])
df_objects = df.select_dtypes(exclude=[np.number])


# replacing categorical values
for col in df.columns:
    # if col is in non-numeric, perform below code
    if col in df_objects:
        num_miss = np.sum(df[col].isnull())
        if num_miss > 0:
            #calculate mode and replace with mode
            top = df[col].describe()['top']
            df[col] = df[col].fillna(top)

        # if col is in numeric, perform below code
        if col in df_numeric:
            num_miss = np.sum(df[col].isnull())
            if num_miss > 0:
                # calculate median and replace with mode
                med = df[col].median()
                df[col] = df[col].fillna(med)

## after handling missing values
print("111. checking all missing values")
for col in df.columns: # ['A','B','C']
    pt_miss = np.mean(df[col].isnull())*100
    if pt_miss > 0.0:
        print(f"{col} - {pt_miss}")

print("Size of the dataset: ",df.shape)

# delete those extra add columns - _Missing
ismiss_cols = [col for col in df.columns if '_Missing' in col]
df = df.drop(ismiss_cols, axis=1)
print("Size of the dataset after dropping _Missing: ",df.shape)

## Outliers - identifying outliers and fixing them
# fixing outliers are very similar to handling missing values
#histogram
df['total_of_special_requests'].hist(bins=5)
plt.show()
#boxplot
df.boxplot(column=['total_of_special_requests'])
plt.show()

# descriptive statistics
print(df['total_of_special_requests'].describe())
'''
#In the next session - we will focus on further steps of data cleaning
#Outliers detection and handling, Duplicates, text data correction

'''

'''

