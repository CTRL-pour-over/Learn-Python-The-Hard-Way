inventory = []

def start():
    print """\nYou are in the captains quarters on a pirate ship.
    There is a book on a table and a door to the
    outside deck. What would you like to do?"""

    choice = raw_input("> ").lower()
    list = ['door', 'deck', 'outside', 'back']
    book = ['read', 'book', 'desk']

    for thing in list:
        if thing in choice:
            outside_deck()
    for thing in book:
        if thing in choice:
            read_book()
    print "\nI don't know what that means."
    start()

def read_book():
    print """ \nCaptains Log, September 12, 1829:
    It's been months since we've drifted astray from transit route.
    Some of our men have been burdouned with scurvy. There's not enough fruit
    or grain to keep our men healthy. I've been left with no other choice but to
    throw the weak off the plank. We cannot afford to feed our remaining rations
    to the sick. Jack Sparrow spoke out against my actions, which resulted in another casualty.
    I'm not worried about what they will say at shore. Truthfully, I don't know if any of us will make it.
    END LOG:

    Go Back?"""

    #Broken List
    list = ["yes", "end", "sure", "go", "back"]
    choice = raw_input("> ").lower()

    for thing in list:
        if thing in choice:
            start()

    print "\nI don't know what that means."
    read_book()

def outside_deck():
    print """\nThis is the outside deck. You see an array of cannons, and a pile of heavy
    looking cannon balls. It looks like you might be able to load and fire the cannons.
    What do you do?"""

    choice = raw_input('> ').lower()
    list = ['back', 'captain', 'start']
    ball = ['get', 'grab', 'look', 'ball', 'cannon']
    for thing in list:
        if thing in choice:
            start()
        elif inventory > 0:
            print "i see you have a cannon ball in your inventory... load the cannon?"

    else:
        for thing in ball:
            if thing in choice:
                inventory.append(1)
                print "You picked up a cannon ball and are now holding it."
                print "You now have %s cannon balls. don't pick up any more." % inventory


    print "\nI don't know what that means."

    outside_deck()

#add cannon balls

start()

#gameOn = True

#while gameOn:
    #Gameplay loop
#    read_book()
#    outside_deck()
