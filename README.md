## Build a data pipeline (data feed) on spoonacular API 
   A program that downloads pasta dishes from spoonacular api, using your personal api_key,  
   then saving the data to an SQLlite database. 
   
   The DB grows daily, with the data of your favourite pasta dish. There is
   possibility to view the frequency at which you view the pasta dish.
   
   For simplicity, I chose to work with only 20 data values.
   

## Features
   - Python
   - SQLAlchemy 
   - Airflow for jobs automation
   - Spoonacular API

## Process
   - ETL
   - Data validation

## Endpoints
  - GET	/v1/me/player/recently-played

## Note
  - With SQLAlchemy, you can query directly from python without querying the database