class Song(object):
    cVolume = 100.0
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def AdjustVolume(argNewVolume):
        cVolume = argNewVolume

# data_type Song
happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
# data_type Song
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

MaxVolume = "qerkjqerkjh"
# data_type String
lyr = "these are the lyrics to my song"
# data_type Song
lyr = Song(["ghfjytjytr"])
# data_type Song
lyr.sing_me_a_song()
# data_type Song
happy_bday.sing_me_a_song()
# data_type Song
bulls_on_parade.sing_me_a_song()
happy_bday.volume = 0
