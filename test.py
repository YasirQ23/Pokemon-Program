from unicodedata import name
from pip._vendor import requests as r


class Pokemon_Info():
    def __init__(self):
        self.name = 'ditto'
        self.weight = int
        self.ability = []
        self.type = []

    def getandlabel(self):
        request = r.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        self.request = request.json()

    def sort_poke(self):
        self.weight = self.request['weight']
        for i in range(len(self.request['abilities'])):
            self.ability.append(self.request['abilities'][i]['ability']['name'])
        self.type = self.request['types'][0]['type']['name'].title()
        self.name = {'Name': self.name, 'Type': self.type,
                     'Abilities': self.ability, 'Wegiht': self.weight}


poke_card = Pokemon_Info()
