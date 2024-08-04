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
'''
print("******1********")

# convert range of values into numpy matrix
x = range(16)
x = np.reshape(x,(4,4))  # (rows,columns)
print(x)

print("*******2*******")

# convert 2-D list into matrix
l1 = [[2,3,1,5],[3,5,1,2],[2,3,5,1]]
print(l1)
l1 = np.array(l1)
print(l1)

print("********3******")

## indexing of numpy
print(x[0], x[2])
print(x[:,0])
#3rd row 2nd col
print(l1[2,1])

print("*********4*****")

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

'''
NUMPY: 2D array
'''
import numpy as np

'''

m1 = np.array([[2,1,3],[1,1,2],[2,2,1]], dtype=np.int32)
m2 = np.array([[2,3,3],[1,3,2],[1,2,1]], dtype=np.int32)
print("matrix m1=\n",m1)
print("matrix m2=\n",m2)

# Different operations:
print("Addition")
print(m1 + m2)
print(np.add(m1,m2))

print("Subtraction")
print(m1 - m2)
print(np.subtract(m1,m2))

print("Element Multiplcation")
print(m1 * m2)
print(np.multiply(m1,m2))

print("Division")
print(m1 / m2)
print(np.divide(m1,m2))

'''

# matrix multiplication
'''
1. Matrix multiplication is possible between M1 and M2 if and only if
 no. of columns of M1 is same as no. of rows of M2
2. Matrix multiplication is order driven - M1 @ M2 is same as M2 @ M1
3. resultant matrix will size of no. of rows of M1 X no. of cols of M2

M1 (p,q) @ M2 (x,y) is possible only if - q=x and the resultant will have size of p x y
M1 (2,3) M2(2,3) - multiplication is not possible
M1 (2,3) M2(3,2) - multiplication is possible and the resultant matrix is of size 2 x 2

'''
'''
m1 = np.array([[2,1,3],[1,1,2],[2,2,1]], dtype=np.int32)
m2 = np.array([[2,3,3],[1,3,2],[1,2,1]], dtype=np.int32)
print("matrix m1=\n",m1)
print("matrix m2=\n",m2)
print("Matrix Multiplication")
print(m1 @ m2)
print(np.matmul(m1,m2))
'''

'''
Square matrix: Matrix with no. of rows = no. of cols
3x3, 4x4, 2x2 ...

Identity matrix: Square matrix which has 1 on the main diagonal and rest is zero.
Determinant of I matrix is 1

Determinant: scalar number that represents the value entire values of a matrix

Inverse: A matrix when multiplied with inverse matrix result in an Identity matrix

All these concepts work on square matrix.
Inverse of a matrix which has determinant of 0, doesnt exist.

'''
'''
import numpy as np

print("creating an Identity matrix:")
m2 = np.identity(6, dtype=np.int32)
print(m2)

'''
'''
Square matrix: Matrix with no. of rows = no. of cols
3x3, 4x4, 2x2 ...

Identity matrix: Square matrix which has 1 on the main diagonal and rest is zero.
Determinant of I matrix is 1

Determinant: scalar number that represents the value entire values of a matrix

Inverse: A matrix when multiplied with inverse matrix result in an Identity matrix

All these concepts work on square matrix.
Inverse of a matrix which has determinant of 0, doesnt exist.

'''
'''
import numpy as np

print("creating an Identity matrix:")
m2 = np.identity(6, dtype=np.int32)
print(m2)
'''
# solving linear equation using numpy
'''
100 girls are looking at 2 types of dresses, blue which costs $50
and pink which costs $75. total budget is $6000

Step 1: frame linear equation:
assume,
x = girls opting blue dresses - $50
y = girls opting pink dresses - $75

x + y = 100 --- 1
50x + 75y = 6000   --- 2

Step 2: create matrices
Coefficient matrix, Coeff_Mat, [[1,1],[50,75]]
Variable matrix, var_mat, [[x],[y]]
output_matrix, out_mat, [[100],[6000]]

Step 3: Coeff_Mat * var_mat = out_mat
so, var_mat = Inverse(Coeff_Mat) * out_mat
'''
'''

Coeff_Mat = np.array([[1,1],[50,75]])
out_mat=np.array([[100],[6000]])
det_coeff = np.linalg.det(Coeff_Mat)
if det_coeff==0:
    print("Since determinant of coefficient matrix is zero, we cant solve this problem")
else:
    print("Determinant = ",det_coeff)
    Coeff_Inv = np.linalg.inv(Coeff_Mat)
    var_mat = Coeff_Inv @ out_mat
    print("Solution is: \n",var_mat)
    print(f"X = {var_mat[0,0]} and Y = {var_mat[1,0]}")

'''

'''
## pip install pandas - at the commant prompt
## PANDAS
import pandas as pd
df1 = pd.DataFrame()
print(df1)
print(type(df1))

df1 = pd.DataFrame([10,20,30,40,50,60])
print(df1)

data = [['Tennis','Paes','India'],['Chess','Anand','India'],['Cricket','Sachin','India']]
df1 = pd.DataFrame(data,columns=['Sports','Legand','Country'])
print(df1)

data = {"Apple":[25,32,43],"Banana":[19,49,54], "Mango":[1,29,40]}
df1 = pd.DataFrame(data)
print(df1)
df1 = pd.DataFrame(data, index=['January','February','March'])
print(df1)


### connecting to MYSQL database  ###
## pymysql library to connect MYSQL
## pip install pymysql
import pymysql
dc = pymysql.connect(host="localhost",database="visitor_management",user="root",passwd="Aditya@8624")
cursor = dc.cursor()

q1 = "Select * from employees"
df2 = pd.read_sql_query(q1,dc)

q2 = "insert into employees values (1008,'Leander Paes','p@pa.com',123321,'Mumbai')"
#cursor.execute(q2)

dc.commit()

print(df2)
dc.close()



import pandas as pd

data = {"Apple":[25,32,43],"Banana":[19,49,54], "Mango":[1,29,40]}
df1 = pd.DataFrame(data)
print(df1)
df1 = pd.DataFrame(data, index=['January','February','March'])
print(df1)

'''

'''
Pandas - indexing using iloc and loc

'''
'''
import pandas as pd

data = {"Apple":[25,32,43],"Banana":[19,49,54], "Mango":[1,29,40]}
df1 = pd.DataFrame(data)
print("*****1*****")
print(df1)
print("*****2*****")
print(df1.iloc[1:3,0:-1])
print("*****3*****")
print(df1.iloc[[0,2],0:-1])
print("*****4*****")
print(df1.loc[[0,1],['Apple','Banana']])



df1 = pd.DataFrame(data, index=['January','February','March'])
print("*****5*****")
print(df1)
print("*****6*****")
print(df1.iloc[1:3,0:2])
print("*****7*****")
print(df1.loc[['February','March'],['Apple','Banana']])

'''
'''
import pandas as pd
import numpy as np
#generate random arrays of date
date_data_1 = pd.date_range('2024-04-20 10:00:00',periods=10,freq="3A")
print("*****1*****")
print(date_data_1)

date_df = pd.DataFrame({'Matches to be Played On':date_data_1,
                        'Exact Date': np.random.randn(len(date_data_1))})
print("*****2*****")
print(date_df)
'''
#frequency per minute = T
#frequency per day = D
#every three years = 3A
'''
'''
'''
import pandas as pd

data = {"Apple":[25,32,43],"Banana":[19,49,54], "Mango":[1,29,40]}
df1 = pd.DataFrame(data)
print("*****1*****")
print(df1)

df1 = pd.DataFrame(data, index=['January','February','March'])

df1['Orange'] = pd.Series([20,40,30], index=['March','January','February'])
print("*****2*****")
print("After adding Orange\n",df1)

df1['Total'] = df1['Apple']+df1['Banana']+df1['Mango']+df1['Orange']
print("*****3*****")
print(df1)

# deleting columns using del and pop options
del df1['Apple']
df1.pop('Banana')
print("*****4*****")
print(df1)

'''

import math

def calculate_area_of_circle(radius):
    # Use the math library to get the value of pi
    area = math.pi * (radius ** 2)
    return area

# Input: Radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = calculate_area_of_circle(radius)

# Output: Area of the circle
print(f"The area of the circle with radius {radius} is: {area:.2f}")

