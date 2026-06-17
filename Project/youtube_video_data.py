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

# print(movie_data.info())

print(movie_data.describe())

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

# print(filter_data)

# print(type(filter_data[0]))

for rows in filter_data:
    view_list.append(float(rows['views']))
    like_list.append(float(rows['likes']))

print(type(view_list[0]))
# Convert the view_list(1D) to 2D
x = np.array(view_list).reshape(-1,1)
y = like_list


model = LinearRegression()
model.fit(x,y)

print(model.coef_)
print(model.intercept_)

new_x = np.array([[440238]])
print(model.predict(new_x))



# create the graph
# actual data
plt.scatter(x, y, color='blue')

# model prediction line
predicted_y = model.predict(x)

plt.plot(x, predicted_y, color='red')
plt.xlabel("Views")
plt.ylabel("Likes")
plt.title("Linear Regression - Views vs Likes")

plt.show()