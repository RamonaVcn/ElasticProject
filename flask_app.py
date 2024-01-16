from flask import Flask, render_template, request
import pandas as pd
from elasticsearch import Elasticsearch

app = Flask(__name__)


username = 'elastic'
password = 'c9NGxWa76m74ALoQD2V3T843'
es = Elasticsearch('https://8c965989446641d19f0ba4fd20db082b.us-central1.gcp.cloud.es.io:9243', basic_auth=(username, password))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_data')
def load_data():
    rows = int(request.args.get('rows', 10))
    response = es.search(index='movies_index', body={"query": {"match_all": {}}}, size=rows)
    data = [doc['_source'] for doc in response['hits']['hits']]
    df = pd.DataFrame(data)
    return df.to_html(classes='table table-striped table-sm', header="true", index=False)

@app.route('/transform_data', methods=['GET', 'POST'])
def transform_data():
    # User input for transformation type and criteria
    transformation_type = request.args.get('type', 'sort')
    criteria = request.args.get('vote_count', 'popularity')  # Default sorting by rating
    value = request.args.get('value', '')  # Value for filtering

    # Elasticsearch query modification based on transformation type
    if transformation_type == 'sort':
        es_query = {"sort": {criteria: {"order": "desc"}}}
    elif transformation_type == 'filter':
        es_query = {"query": {"match": {criteria: value}}}
    else:
        es_query = {"query": {"match_all": {}}}

    # Execute Elasticsearch query
    response = es.search(index='movies_index', body=es_query)
    data = [doc['_source'] for doc in response['hits']['hits']]

    # Convert data to DataFrame and return as HTML
    df = pd.DataFrame(data)
    transformed_html = df.to_html(classes='table table-striped table-sm', header="true", index=False)
    return render_template('transformed_data.html', data=transformed_html)

if __name__ == '__main__':
    app.run(debug=True)

