import pandas as pd 

data = {
    "Student": ["a" , "b", "c", "d", "e", "f", "g"],
    "Math": [70, 75, None, 38, 78, 110, 60],
    "Chem": [75, 28, 85, None, 78, 65, 40],
    "Phy": [None, None, 88, 158, 77, 68, 75]

}

df = pd.DataFrame(data)

df = df.dropna()

df = df[df['Math']< 101]
print(df)