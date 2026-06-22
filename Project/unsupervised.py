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
        float(row['dislikes'])
        float(row['comment'])
        filter_data.append(row)
    except:
        error_data.append(row)

# convert the filter data list in pandas
clean_data = pd.DataFrame(filter_data)
print(clean_data.head())

