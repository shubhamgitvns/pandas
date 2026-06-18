import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df)
x = df['x']
y = df['y']
plt.scatter(x,y,color="green")
plt.xlabel("View")
plt.ylabel("Likes")
plt.show()