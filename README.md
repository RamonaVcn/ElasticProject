# Flask Elasticsearch Movie Data Application

## Overview
This application is a Flask-based web interface for searching and displaying movie data stored in an Elasticsearch index. It includes functionality for loading data from a CSV file into Elasticsearch and rendering search results in a web page.

## Requirements
- Python 3.x
- Flask
- pandas
- Elasticsearch Python Client

## Setup and Configuration
1. *Elasticsearch Setup*: Ensure that you have an Elasticsearch instance running. Update the username, password, and Elasticsearch URL in both flask_app.py and the script for data ingestion.

2. *CSV File*: The data ingestion script assumes a CSV file named popular_movies.csv. The format of the CSV should match the mapping defined in the script.

## Application Structure
- flask_app.py: This is the main Flask application file. It handles web requests and communicates with the Elasticsearch instance.
- Data Ingestion Script: A separate script for reading data from popular_movies.csv and indexing it into Elasticsearch.

## Features
- *Web Interface*: The Flask app provides a simple web interface for data visualization.
- *Data Loading Endpoint*: The /load_data route in the Flask app allows for dynamic loading of data from Elasticsearch based on user input.
- *Elasticsearch Indexing*: The data ingestion script reads from a CSV file and indexes data into Elasticsearch with a predefined mapping.

## How to Run
1. *Start Elasticsearch*: Ensure your Elasticsearch instance is up and running.
2. *Data Ingestion*: Run the data ingestion script to load data from popular_movies.csv into Elasticsearch.
3. *Flask App*: Run flask_app.py to start the Flask server.
4. *Access Web Interface*: Go to http://localhost:5000 in your web browser to view and interact with the application.

## Note
- Make sure to fill in the username and password fields for Elasticsearch in both scripts.
- Ensure that your CSV file is correctly formatted and matches the mapping specified in the ingestion script.
- The application is set to run in debug mode for development purposes. Disable debug mode in a production environment.