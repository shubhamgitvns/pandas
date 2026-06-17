import pandas as pd

movie_data = pd.read_csv("youtube_video_list.csv")
print(movie_data.head())
filter_data = []
error_data =[]
view_list =[]
like_list = []
n = len(movie_data)

print(movie_data.head())

# print(movie_data.info())

print(movie_data.describe)

# Start cleanning process

# remove null value
movoe_data = movie_data.dropna()

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
    view_list.append(rows['views'])
    like_list.append(rows['likes'])

X = view_list
y = like_list

