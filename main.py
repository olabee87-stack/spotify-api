import json
import sqlite3

import requests
import sqlalchemy
import pandas as pd
import base64

from datetime import datetime
import datetime
from sqlalchemy.orm import sessionmaker

import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/4632/summary"

headers = {
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "03e5c1eecamshfdc67ca870a8cc1p1314cdjsn8d6a3d0a76e3"
}

response = requests.request("GET", url, headers=headers)

print(response.text)