import pypokedex
import requests
import json

#p = pypokedex.core()
Pokeapi_Base_Url_Pokemon = "https://pokeapi.co/api/v2/pokemon"
Pokeapi_Base_Url_Moves = "https://pokeapi.co/api/v2/move"

'''p = requests.get(f'{Pokeapi_Base_Url_Pokemon}/pikachu')
p = p.json()
print(p['moves'][0]['move'])'''
#query = input("move name")
#query = query.lower().replace(' ', '-')
query = 'scratch'
p = requests.get(f'{Pokeapi_Base_Url_Moves}/flip-turn')
p = p.json()
with open('p34.json', 'w+') as f:
    f.write(json.dumps(p, indent=3))
#print(p['flavor_text_entries'][0]['flavor_text'].replace('\n', ' '))