from pip._vendor import requests as r

poke_list = ['ditto', 'pikachu', 'eevee', 'snorlax', 'garchomp', 'lucario', 'charizard', 'gardevoir', 'piplup',
             'charmander', 'mewtwo', 'mew', 'dialga', 'palkia', 'gyarados', 'bulbasaur', 'squirtle', 'lopunny', 'infernape', 'combee']


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
            self.ability.append(
                self.request['abilities'][i]['ability']['name'].title())
        for i in range(len(self.request['types'])):
            self.type.append(self.request['types'][i]['type']['name'].title())
        self.info = {'Name': self.name, 'Type': self.type,
                     'Abilities': self.ability, 'Wegiht': self.weight}

    def poke_info(self):
        self.card = {'Name': self.name.title(), 'Type': self.type,
                     'Ability': self.ability, 'Weight': self.weight}
        return self.card


class Pokedex_info():
    def __init__(self):
        self.pokedexlib = []

    def lib_creation(self):
        for x in poke_list:
            poke_card = Pokemon_Info(x)
            poke_card.getandlabel()
            poke_card.sort_poke()
            poke_card.poke_info()
            self.pokedexlib.append(poke_card.poke_info())
            print(f'{poke_card.poke_info()["Name"]} | {" / ".join(poke_card.poke_info()["Type"])} Type | Abilities: {", ".join(poke_card.poke_info()["Ability"])} | {int((poke_card.poke_info()["Weight"]/10)*2.20462)} lbs')


def run():
    pokedex = Pokedex_info()
    pokedex.lib_creation()


run()
