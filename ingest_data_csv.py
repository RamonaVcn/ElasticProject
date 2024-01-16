import pandas as pd
from elasticsearch import Elasticsearch

# Replace with the path to your CSV file
csv_file_path = 'popular_movies.csv' 
username = 'elastic'
password = 'c9NGxWa76m74ALoQD2V3T843'
es = Elasticsearch('https://8c965989446641d19f0ba4fd20db082b.us-central1.gcp.cloud.es.io:9243', basic_auth=(username, password))
df = pd.read_csv(csv_file_path)
df.dropna(inplace=True)

index_name = 'movies_index'
for index, row in df.iterrows():
    row_dict = row.to_dict()
    es.index(index=index_name, id=index, body=row_dict)
    
