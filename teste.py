import random

chances = ['fugiu', 'naofugiu']
chance = random.choices(chances, weights = [65, 100-65])

print(chance)
