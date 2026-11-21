# OldMacDonald.py

import string

class Animal:
    def __init__(self, art1: string, name: string, art2: string, noise: string):
        self.art1 = art1
        self.name = name
        self.art2 = art2
        self.noise = noise

    def printVerse(self):
        print("Old McDonald had a farm, E-I-E-I-O")
        print(f"""And on his farm he had {self.art1} {self.name}, E-I-E-I-O""")
        print(f"""With {self.art2} "{self.noise}-{self.noise}" here and a "{self.noise}-{self.noise}" there""")
        print(f"""Here {self.art2} "{self.noise}", there {self.art2} "{self.noise}" """)
        print(f"""Everywhere {self.art2} "{self.noise}-{self.noise}" """)
        print("Old McDonald had a farm, E-I-E-I-O\n")

animals = [
            Animal("an", "alligator", "a", "hiss"),
            Animal("an", "alpaca", "a", "hum"),
            Animal("an", "antelope", "a", "snort"),
            Animal("a", "badger", "a", "growl"),
            Animal("a", "bat", "a", "squeak"),
            Animal("a", "bear", "a", "roar"),
            Animal("a", "beaver", "a", "gnaw"),
            Animal("a", "bee", "a", "buzz"),
            Animal("a", "camel", "a", "grunt"),
            Animal("a", "capybara", "a", "chatter"),
            Animal("a", "cat", "a", "meow"),
            Animal("a", "cow", "a", "moo"),
            Animal("a", "chicken", "a", "bawk"),
            Animal("a", "chincilla", "a", "squeak"),
            Animal("a", "crab", "a", "click"),
            Animal("a", "cricket", "a", "chirp"),
            Animal("a", "crow", "a", "caw"),
            Animal("a", "dolphin", "a", "whistle"),
            Animal("an", "elephant", "a", "trumpet"),
            Animal("an", "elk", "a", "bugle"),
            Animal("a", "ferret", "a", "squeak"),
            Animal("a", "gnat", "a", "buzz"),
            Animal("a", "fish", "a", "glub"),
            Animal("a", "frog", "a", "ribbet"),
            Animal("a", "giraffe", "a", "hum")
]

for animal in animals:
    animal.printVerse()