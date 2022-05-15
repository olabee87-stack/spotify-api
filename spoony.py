import requests
import pandas as pd
import sqlalchemy
import sqlite3

from api_keys import spoon_api
from modules.validation_helper import check_if_valid_data

DATABASE_LOCATION = 'sqlite:///pasta_dishes.sqlite'


def extract_data():
    # fill your spoonacular api key
    api_key = spoon_api()

    # get some sample endpoints from spoonacular
    url = f'https://api.spoonacular.com/recipes/715538/similar?apiKey={api_key}'
    url2 = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query=pasta&maxFat=25&number=20'
    response = requests.get(url2)
    response_data = response.json()

    # create empty lists for data
    title = []
    nutrition = []

    for r in response_data['results']:
        title.append(r['title'])
        nutrition.append(r['nutrition']['nutrients'][0]['amount'])

    # Put data in dataframe (Transform)
    pasta_dict = {
        "title": title,
        "nutrition": nutrition
    }

    pasta_df = pd.DataFrame(pasta_dict, columns=["title", "nutrition"])

    # Validate
    if check_if_valid_data(pasta_df):
        print('Data works fine, You can load it!')
        # return pasta_df

    # Load data
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('pasta_dishes.sqlite')
    cursor = conn.cursor()

    sql_query = """
        CREATE TABLE IF NOT EXISTS pasta_dishes(
        title VARCHAR(300),
        nutrition FLOAT(5, 2),
        pk INTEGER PRIMARY KEY DESC
        )
        """

    cursor.execute(sql_query)
    print('Database successfully mounted')

    # Load data from dataframe to database

    try:
        pasta_df.to_sql('pasta_dishes', engine, index=False, if_exists='append')
    except:
        print('Data already exists in the database')

    conn.close()
    print('Database successfully closed')





# Schedule jobs


print(extract_data())
