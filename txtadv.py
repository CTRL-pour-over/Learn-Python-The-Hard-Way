from termcolor import colored
print colored('hello', 'red'), colored('world', 'green')

class Room(object):
    description = ""
    name = ""
    itemsContained = {}
    keyWords = []
    events = []
    hasBeenVisited = 0
    adacientRooms = []
    playerPresent = False

    def __init__(self, arg_description, arg_name, arg_itemsContained, arg_keyWords, arg_events, arg_hasBeenVisited, arg_adacientRooms, arg_playerPresent):
        self.description = arg_description
        self.name = arg_name
        self.itemsContained = arg_itemsContained
        self.keyWords = arg_keyWords
        self.events = arg_events
        self.hasBeenVisited = arg_hasBeenVisited
        self.adacientRooms = arg_adacientRooms
        self.playerPresent = arg_playerPresent

    def PrintRoom():
        print colored(description, 'yellow')
        print colored(name, 'red')
        

    def read_room(self):
        for thing in self.arg:
            print thing

class Player(object):
    name = "Thomas"
    health = 100.00
    min_damage = 0.0
    max_damage = 999.9

    def __init__(self, arg_name, arg_health, arg_min_damage, arg_max_damage):
        # setting the variable to the argument
        self.name = arg_name
        # setting the variable to the argument
        self.health = arg_health
        # setting the variable to the argument
        self.min_damage = 0.0
        # setting the variable to the argument
        self.max_damage = arg_max_damage

    def show_stats(self):
        print self.name, self.health, self.min_damage, self.max_damage

    def talk_to_game(self):
        answer = raw_input(">>> ")
        for thing in answer:
            if thing in keyword:
                return something
# instantiated a Player object
player_1 = Player("Thomas", 100.0, 1.0, 99.9)

captains_quarters = Room("This is the captains_quarters Do yopu walk out the door or na?", "captains_quarters", {'baby':'item'}, ['walk', 'door', 'go'], [], 0, [], True)

start = """ You are in a dark room. The walls are solid concrete,
it's very dark in here. Maybe you should feel around. """

deck = """ You have made it to the deck, its still really dark in here """

player_1.show_stats()
print start
print colored(start, 'yellow')
