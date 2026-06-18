import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

movie_data = pd.read_csv("youtube_video_list.csv")
print(movie_data.head())
filter_data = []
error_data =[]
view_list =[]
like_list = []
n = len(movie_data)

print(movie_data.head())

# Start cleanning process

# remove null value
movie_data = movie_data.dropna()

# remove dupplicates
movie_data = movie_data.drop_duplicates()

for i in range(n):
    row = movie_data.iloc[i]
    try:
        float(row['views'])
        float(row['likes'])
        float(row['dislikes'])
        float(row['comment'])
        filter_data.append(row)
    except:
        error_data.append(row)


for rows in filter_data:
    view_list.append(float(rows['views']))
    like_list.append(float(rows['likes']))

# Convert the view_list(1D) to 2D
# x = np.array(view_list).reshape(-1,1)
# y = like_list

# data prediction throw the pollynomial
x = np.array(view_list)
y = np.array(like_list)


# model = LinearRegression()

# model fit for using pollynomial
model = np.polynomial.Polynomial.fit(x,y,1)
print(model)
# predict the data given the x value and predict y
print(model([10000]))




