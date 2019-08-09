class Song:
    tags = []

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add_tags(self, *args):
        self.tags.extend(args)


song1 = Song("one","two")
song1.add_tags("a1","b1")

song2 = Song("three","four")
song2.add_tags("a2","b2")

print(song2.tags)

