from pip._vendor import requests as r

poke_list=['ditto','pikachu','eevee','snorlax','garchomp','lucario','charizard','gardevoir','piplup','charmander','mewtwo','mew','dialga','palkia','gyarados','bulbasaur','squirtle','lopunny','infernape','combee']

class Pokemon_Info():
    def __init__(self, name):
        self.name = name
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
        self.info = {'Name': self.name, 'Type': self.type,
                     'Abilities': self.ability, 'Wegiht': self.weight}
    
    def poke_info(self):
        card = {'Name': self.name, 'Type':self.type , 'Ability': self.ability, 'Weight': self.weight}
        print(card)


def run():
    for x in poke_list:
        poke_card = Pokemon_Info(x)
        poke_card.getandlabel()
        poke_card.sort_poke()
        poke_card.poke_info()

run()
