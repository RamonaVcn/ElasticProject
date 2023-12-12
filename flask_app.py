from flask import Flask, render_template, request
import pandas as pd
from elasticsearch import Elasticsearch

app = Flask(__name__)


username = 'elastic'
password = ''
es = Elasticsearch('https://elasticsearchapp.es.northeurope.azure.elastic-cloud.com:9243', basic_auth=(username, password))

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

if __name__ == '__main__':
    app.run(debug=True)