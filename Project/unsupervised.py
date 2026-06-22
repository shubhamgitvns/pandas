import pandas as pd

data = pd.read_csv('youtube_video_list.csv')

print(data.head())
n= len(data)

print(n)

filter_data = []
error_data = []

for i in range(n):
    row = data.iloc[i]
    try:
        float(row['views'])
        float(row['likes'])
        filter_data.append(row)
    except:
        error_data.append(row)

print(len(filter_data))       
