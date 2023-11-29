#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def save_name(self, name):
        if (type(name) in (name, str)) and len(name) > 0 and len(name) < 25:
            self.name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(save_name)
    
    def save_breed(self, breed):
        if (type(breed) in (breed, str)) and breed in APPROVED_BREEDS:
            self.breed = breed
        
        else:
            print("Breed must be in list of approved breeds.")
            
    breed = property(save_breed)