import spoonacular as sp
import json
from api_keys import spoon_api

my_api = sp.api(spoon_api())

resp = my_api.parse_ingredients("3.5 cups King Arthur flour", servings=2)
data = resp.json()
print(data[0]['name'])