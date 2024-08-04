import pandas as pd
import numpy as np

'''
'''
#For importing Data set from github, open file as a raw file in githum copy the link
#of the file and paste it and assign the link to variable.
#By default if dataset consist more than 10 rows and more than 4 columns it will show top 5 and bottom 5 rows
#and first 2 and last 2 coloumns.
'''

uu = "https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/user_usage.csv"
uu_df = pd.read_csv(uu)
print("Output 1")
#print(uu_df)
print("uu_df dimenssions:\n",uu_df.shape)

ud = "https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/user_device.csv"
ud_df = pd.read_csv(ud)
print("Output 2")
#print(ud_df)
print("uu_uu dimenssions:\n",ud_df.shape)

'''
#To merge the dataset, we need following parameters:
#on = common column on which you want to merge
#how = left, right, inner(default), outer
'''

result = pd.merge(uu_df, ud_df, on="use_id")
print("Output 3")
print("Columns & first rows of result:\n",result.head(3))

print("Output 4")
print("Results dimensions:\n",result.shape)
# 240  272 => 159 (inner) => 240 (left)  272 (right)  159+81+113=v (outer)
result_outer = result = pd.merge(uu_df, ud_df, on="use_id",how="outer")
print("Output 5")
print("Outer Results dimensions:\n",result_outer)
'''

'''
link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/master/Iris.csv"
df = pd.read_csv(link)
print("Top 5 rows:\n",df.head())
print("Bottom 6 rows:\n",df.tail(6))

print("Size of the dataset (rows.columns):", df.shape)

print("Basic Statistics:\n",df.describe())

print("**** Output ****")
print("Columns and their data types:^^",df.info())

print("Checking for missing values:\n",df.isnull().sum())

print("Checking for Duplicate values:\n")
df_2 = df.drop_duplicates(subset="Species")
print("Size of the dataset after dup removal:", df_2.shape)
print("DF_2:\n",df_2)

print("Balancing the dataset:\n")
print(df.value_counts("Species"))


#### Performing visualization
#### EDA - Exploratory Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns
## pip install matplotlib seaborn

sns.countplot(data=df,x="Species")
plt.title("Count Plot - Species")
plt.show()

# find correlation between Petel length and Sepal length
sns.scatterplot(data=df,x="PetalLengthCm",y="SepalLengthCm")
plt.title("Scatterplot: PetalLength v SepalLength")
plt.show()

## Histogram
fig,axes=plt.subplots(2,2, figsize=(10,10))
axes[0,0].set_title('PetalLengthCm')
axes[0,0].hist(df['PetalLengthCm'],bins=10)

axes[0,1].set_title('SepalLengthCm')
axes[0,1].hist(df['SepalLengthCm'],bins=10)

axes[1,0].set_title('PetalWidthCm')
axes[1,0].hist(df['PetalWidthCm'],bins=10)

axes[1,1].set_title('SepalWidthCm')
axes[1,1].hist(df['SepalWidthCm'],bins=10)
plt.show()

## BOXPLOT
sns.boxplot(data=df,x="Species",y="PetalLengthCm")
plt.title("Boxplot: Species v PetalLengthCm")
plt.show()

sns.boxplot(data=df,x="Species", y="SepalLengthCm")
plt.title("Boxplot: Species v SepalLengthCm")
plt.show()

sns.boxplot(data=df,x="Species",y="SepalWidthCm")
plt.title("Boxplot: Species v SepalWidthCm")
plt.show()

sns.boxplot(data=df,x="Species",y="PetalWidthCm")
plt.title("Boxplot: Species v PetalWidthCm")
plt.show()
'''


'''
working with large dataset: hotel_bookings dataset

'''

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
Handling inconsistency in the text data
'''
import pandas as pd
print("Original data: ")
address_df = pd.DataFrame(['No. 190', 'MaRIne NEsT Apartment',
                           '    Mahabalipuram Street    ','Rd       No. 8 .'], columns=["Address"])
print(address_df)

#1. Standardize the content
address_df["Address_Update"] = address_df["Address"].str.title()
#2. removing trailing and leading spaces if any
address_df["Address_Update"] = address_df["Address_Update"].str.strip()

#3. split and join to remove spaces in the text
address_df["Address_Update"] = address_df["Address_Update"].str.replace("      "," ")
address_df["Address_Update"] = address_df["Address_Update"].str.replace("Rd ","Road")
print("Modified Data:")
print(address_df)


import matplotlib.pyplot as plt
import numpy as np
x_axis = ('Virat','Rohit','Dhoni','Shreyas','Rahul')
y_runs= [21000,19000,17000,19500,20000]
plt.bar(np.arange(len(x_axis)), y_runs)
plt.xticks(np.arange(len(x_axis)),x_axis)
plt.title("Runs scored by top Indian Batsmen")
plt.show()

## stacked barchart
ipl1 = [1000,1100,750,900, 1250]
ipl2 = [1000,1900,750,1700, 1050]
ipl3 = [1000,1000,1250,1900, 1250]
ipl4 = [2000,1150,750,1200, 1250]

# ipl1 and ipl2
bars1 = np.add(ipl1,ipl2).tolist()
bars2 = np.add(bars1,ipl3).tolist()
pos = np.arange(len(x_axis))

# ipl1
plt.bar(pos,ipl1, color="blue")
#ipl2
plt.bar(pos,ipl2, bottom=ipl1, color="Yellow")
#ipl3
plt.bar(pos,ipl3, bottom=bars1, color="Brown")
#ipl4
plt.bar(pos,ipl4, bottom=bars2, color="Grey")

plt.xticks(np.arange(len(x_axis)),x_axis)
plt.title("Runs scored by top Indian Batsmen in each IPL")
plt.show()



