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
clean_data['views'] = clean_data['views'].astype(float)
print(type(clean_data['views']))
range_of_views = (clean_data['views'].max() - clean_data['views'].min())
mean_of_views = clean_data['views'].mean()
median_of_views = clean_data['views'].median()
std_of_views = clean_data['views'].std()
print(range_of_views)
print(mean_of_views)
print(median_of_views)
print(std_of_views)

