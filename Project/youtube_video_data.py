import pandas as pd

movie_data = pd.read_csv("youtube_video_list.csv")
print(movie_data.head())
filter_data = []
error_data =[]
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

print(filter_data)

