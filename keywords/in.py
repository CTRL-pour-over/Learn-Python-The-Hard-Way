#--- in: Part of for-loops. Also a test of X in Y ----
def start(): # this is a function
    print """\nYou are playing track and field. It's the final lap and you are falling behind your
    opponents. You really need to win this if you wanna get that scholorship to university.\n """

    list = ['run', 'faster', 'hurry', 'rush'] # container of keywords the player can say.
    choice = raw_input("What do you do? ->>>   ") # user input saved into choice

    for thing in list: # if there is an argument in list[]
        if thing in choice: # if that argument is in choice()
            print """You give it your all, working your body beyond exhaustion. For
            the love of god and all that is holy, give yourself a break! People are
            too hard on themselves these days. Everything is a competition. Never the less
            you win the race."""
            break # dont print this more than once or anything else
        elif thing is not list: # if the player didnt say the right thing
            print """You trip and fall, scraping against the asphalt. Dreams of success
            turn into nightmares of failure. Your parents will disown you. Not only did
             you fail the race, you failed at life."""
            break # only run this once failsafe.
start() #start the program
