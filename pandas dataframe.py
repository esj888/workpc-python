# ************** dataframe **************
#      Address  Age    Name Qualification
# 0      Delhi   27     Jai           Msc
# 1     Kanpur   24  Princi            MA
# 2  Allahabad   22  Gaurav           MCA
# 3    Kannauj   32    Anuj           Phd
# ***************************************

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age':[27, 24, 22, 32],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

# print dataframe
#print(df)

# select two columns
#print(df[['Name', 'Qualification']])

# print row 1
#print(df.loc[1])
#print(type(df.loc[1]))

# sum ages
#print(df["Age"])
#print(type(df["Age"]))
#print(df["Age"].shape)  # shape attribute (no parens) containing num of rows and columns
#print(df["Age"].sum())   # sum series

# convert names to a list
#print(df["Name"])
name_series = df["Name"]
name_list = name_series.to_list()
print(name_list)
print(type(name_list))
