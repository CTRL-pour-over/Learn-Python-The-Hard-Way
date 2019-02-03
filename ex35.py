from sys import exit

def readint():
    while True:
        choice = raw_input("Type something and ill make sure its a number.")
        try:
            num = int(choice)
            return num
        except ValueError:
            print "Man, learn how to type a number."


def gold_room(): #also a subroutine
    print "This room is full of gold. How much do you take?"

    how_much = readint()
    print "this is the how_much value %r" % how_much
    if how_much < 100:
        print "Great! You aren't gready! You win!"
        exit(0)
    else:
        dead("So greedy... Much shame.")



#probably the most complex block of code in this script.
#this is due to the door opening function using the while loop.
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True: # it is true the bear_moved = False
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through is now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
