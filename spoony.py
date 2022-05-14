import requests
import pandas as pd

from api_keys import spoon_api
from validation_helper import check_if_valid_data


def extract_data():
    # fill your spoonacular api key
    api_key = spoon_api()

    # get some sample endpoints from spoonacular
    url = f'https://api.spoonacular.com/recipes/715538/similar?apiKey={api_key}'
    url2 = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&query=pasta&maxFat=25&number=20'
    response = requests.get(url2)
    response_data = response.json()

    # create empty list for your data
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
        return pasta_df

    # Load data

    # Schedule jobs


print(extract_data())
