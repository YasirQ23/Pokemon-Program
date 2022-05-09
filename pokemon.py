from pip._vendor import requests as r


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
        self.name = self.request['forms'][0]['name']
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
        self.currentteam = []

    def lib_creation(self):
        for i in range(1, 152):
            poke_card = Pokemon_Info(i)
            poke_card.getandlabel()
            poke_card.sort_poke()
            poke_card.poke_info()
            self.pokedexlib.append(poke_card.poke_info())

    def ui(self):
        print(f'\nWelcome to Yasir\'s Pokemon Resource Center')
        while True:
            x = input(
                "\nMain Menu:\n[1] Search Pokemon by type\n[2] Team Builder\n[3] Get Pokemon info\n[4] Quit\nChoose An Option By Simply Typing The Number Below.\n")
            if x == '1':
                typename = ['Normal', 'Fighting', 'Fire', 'Water', 'Flying', 'Grass', 'Poison', 'Electric',
                            '\n''Ground', 'Psychic', 'Rock', 'Ice', 'Bug', 'Dragon', 'Ghost', 'Dark', 'Steel', 'Fairy']
                print(f'\nThe Pokemon types are:\n{", ".join(typename)}')
                y = input(
                    '\nWhat type of Pokemons would you like to see?: \n').title()
                if y in typename:
                    typelist = [x['Name']
                                for x in self.pokedexlib if y in x['Type']]
                    print(
                        f'\nThese are our {y} type Pokemons:\n{", ".join(typelist)}')
                else:
                    print(f'\nInvalid Input. Redirecting to Main Menu.')
            elif x == '2':
                while True:
                    x = input(
                        "\nTeam Builder Menu:\n[1] Add Pokemon to team\n[2] Remove Pokemon from team\n[3] View Pokemon team\n[4] Return to Main Menu\nChoose An Option By Simply Typing The Number Below.\n")
                    if x == '1':
                        if len(self.currentteam) == 4:
                            print(
                                f'Sorry you have to many Pokemon on your team.\nThe team max is 4 Pokemons, If you would like to add a new pokemon\nPlease remove one from your team first.')
                            break
                        y = input(
                            f'\nWhich Pokemon would you like to add to your team?:\n').title()
                        namelist = [x['Name'] for x in self.pokedexlib]
                        if y in namelist:
                            self.currentteam.append(y)
                            print(f'\n{y} was succesfully added to your team.')
                        else:
                            print(
                                f'Invalid Input. That Pokemon does not exist in our database.')
                    elif x == '2':
                        if self.currentteam == []:
                            print(
                                f'Your current team is empty.\nReturning to Team Builder Meni')
                        else:
                            print(
                                f'\nThe Pokemon currently in your team are:\n{", ".join(self.currentteam)}')
                            y = input(
                                f'Which Pokemon would you like to remove?:\n').title()
                            if y in self.currentteam:
                                self.currentteam.remove(y)
                                print(
                                    f'{y} was successfully removed from team!')
                            else:
                                print(
                                    f'Invalid Input. That Pokemon is not in your team!\n Returning to Team Builder Menu')
                    elif x == '3':
                        if self.currentteam != []:
                            print(
                                f'This is your current team:\n{", ".join(self.currentteam)}')
                        else:
                            print(f'Your team is currently empty')
                    elif x == '4':
                        break
            elif x == '3':
                namelist = [x['Name'] for x in self.pokedexlib]
                y = input(
                    f'\nSimply enter the Pokemons name below to view its basic info card.\n').title()
                if y in namelist:
                    for x in self.pokedexlib:
                        if x['Name'] == y:
                            card = x
                            print(
                                f"\n{card['Name']} | {' / '.join(card['Type'])} Type | Abilities: {', '.join(card['Ability'])} | {int(card['Weight']*.220462)} lbs")
                else:
                    print(
                        f'\nInvalid Input. That Pokemon does not exist in our database.')
            elif x == '4':
                print(f'Thanks For Stopping By Have Nice Day!')
                break


def run():
    pokedex = Pokedex_info()
    pokedex.lib_creation()
    pokedex.ui()


run()
