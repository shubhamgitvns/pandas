import pandas as pd 

data = {
    "Student": ["a" , "b", "c", "d", "e", "f", "g"],
    "Math": [70, 75, None, 38, 78, 110, 60],
    "Chem": [75, 28, 85, None, 78, 65, 40],
    "Phy": [None, None, 88, 158, 77, 68, 75]

}

df = pd.DataFrame(data)
print(df)
# handel null values

# print all values in datframe in boolian if none true else false
print(df.isnull())

# print only null columns and show how value nane of each columns
print(df.isnull().sum())

# print only null rows
print(df[df.isnull().any(axis=1)])

# remove all nane rows in data framne
print(df.dropna())
# remove only specifc colums row where the nane exit
print(df.dropna(subset=['Phy']))
