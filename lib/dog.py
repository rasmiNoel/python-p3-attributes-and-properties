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
        
    def get_name(self):
        print("Getting name...")
        return self.name
    
    def set_name(self, name):
        if (type(name) in (name, str)) and len(name) > 0 and len(name) < 25:
            print ("Setting name...")
            self.name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
    
    def get_breed(self):
        print("Getting breed...")
        return self.breed
    
    def set_breed(self, breed):
        if (type(breed) in (breed, str)) and breed in APPROVED_BREEDS:
            print ("Setting breed...")
            self.breed = breed
        
        else:
            print("Breed must be in list of approved breeds.")
            
    breed = property(get_breed, set_breed)