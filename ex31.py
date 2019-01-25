# Making Decisions

# This script plays a short text adventure game. The user is able to choose door 1, or door 2.
# There are multiple options to choose in each room, this is done using if, elif, and else nesting.
# The only way to "win" this game is to choose niether 1 or 2 when in the flower room. (he runs away.)

print "You enter a dark room with two doors, you are filled with DETERMINATION. Do you go through door #1 or door #2?"

door = raw_input("> ") # chooses door 1, 2 or debug output at the bottom of the script.

if door == "1":
    print "There's a giant f l o w e r here eating a child. What do you do?"
    print "1. Try to save the child."
    print "2. Scream at the flower."

    flower = raw_input("> ")

    if flower == "1":
        print "The child cannot be saved. The f l o w e r eats your face off, steals your soul, and breaks the barrier into the human world. With the power of your human soul, the flower grows god-like powers and rips humanity into a pile of red sludge. Rest in Reeces Pieces."
    elif flower == "2":
        print "The flower shoots thorns into your eyes, you are blinded in the dungeon and ultimately, you will die a cold dark death. Rest in Reeces Pieces."
    else:
        print "Well, doing %s is probably better. The F L O W E R runs away. VICTORY" % flower

elif door == "2":
    print "You stare into the eyes of the all mighty and powerful."
    print "1. Blueberries."
    print "2. Bacterial infection."
    print "3. I think I'm losing my mind."

    insanity = raw_input("> ")

    if insanity == "1":
        print "The f  l  o  w  e  r  offers you some blueberries upon request. You eat the blueberries without realising they are GMO non organic brand and start to get sick from pesticide poisoning. Guess we all gotta go some way. RIP."
    elif insanity == "2":
        print "You trick yourself into believing you have a bacterial infection just by thinking about it. The devil takes advantage of your weakness. You are nothing now. RIP."
    else:
        print "You start thinking to yourself in wingdings font. Truly these are the last days, you cant even think to yourself in a comprehendible language. Such a sad sight, get thrown in the trash loser."
else:
    print "you stumble around and fall on a knife and die. Good job!"
