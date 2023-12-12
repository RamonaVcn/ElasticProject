import pandas as pd
from elasticsearch import Elasticsearch

csv_file_path = 'popular_movies.csv'
username = 'elastic'
password = ''
df = pd.read_csv(csv_file_path)
df.dropna(inplace=True)
es = Elasticsearch('https://elasticsearchapp.es.northeurope.azure.elastic-cloud.com:9243', basic_auth=(username, password))

index_name = 'movies_index'


for index, row in df.iterrows():
    row_dict = row.to_dict()
    es.index(index=index_name, id=index, document=row_dict)
