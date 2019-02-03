def start():
    print """You are in the captains quarters on a pirate ship.
    There is a book on a table and a door to the
    outside deck. What would you like to do?"""

    choice = raw_input("> ")
    list = ['open', 'door', 'deck', 'outside']

    for thing in list:
        if thing in choice:
            outside_deck()

def outside_deck():
    print """This is the outside deck. You see an array of cannons,
    a crows nest with a ladder, and a top deck with the steering
    wheel for the vessel. What do you do?"""

    choice = raw_input('> ')
    list = ['back', 'captain', 'start']

    for thing in list:
        if thing in choice:
            start()

start()
