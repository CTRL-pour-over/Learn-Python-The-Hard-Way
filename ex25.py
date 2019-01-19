# This script must be imported into the python interpreter in real time.
# Create a sentence variable and plug it into some of the functions!

# the .split() method splits a string into a list
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
# sorted() method sorts the contents of a list in alphabetical order.
def sort_words(words):
     """Sorts the words."""
     return sorted(words)
# removes a specified word and returns it as its own list. (0) in the list
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
# same function as above only different specification for pop() resulting in the last word removed and returned as its own list.
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
# this is where the script gets more complicated, we're using functions inside of functions... help me
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
# combines two existing functions to make a new function
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
# combines three functions to make a function! this is getting crazy!
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
