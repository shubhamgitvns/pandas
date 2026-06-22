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
print(len(clean_data))
# convert the column data types
clean_data['views'] = clean_data['views'].astype(float)
clean_data['likes'] = clean_data['likes'].astype(float)
# find the numerical terms (range(), mean(), median(), std()) of each data 
range_of_views = (clean_data['views'].max() - clean_data['views'].min())
mean_of_views = clean_data['views'].mean()
median_of_views = clean_data['views'].median()
std_of_views = clean_data['views'].std()

# find top 5% and min 5% data in view column data
top5_of_views = clean_data['views'].sort_values(ascending=False).head(5)
min5_of_views = clean_data['views'].sort_values(ascending=False).tail(5)



range_of_likes = (clean_data['likes'].max() - clean_data['likes'].min())
mean_of_likes = clean_data['likes'].mean()
median_of_likes = clean_data['likes'].median()
std_of_likes = clean_data['likes'].std()

# find top 5% and min 5% data in likes column data
top5_of_likes = clean_data['likes'].sort_values(ascending=False).head(5)
min5_of_likes = clean_data['likes'].sort_values(ascending=False).tail(5)


# remove the top and min 5% data in the df
remove_values = list(top5_of_views) + list(min5_of_views) +list(top5_of_likes) + list(min5_of_likes)
clean_data = clean_data[

    ~clean_data['views'].isin(remove_values)
]



print(len(clean_data))


