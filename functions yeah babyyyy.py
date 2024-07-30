namer = "....?"
import random
class Diece:
    def roll():
        namer = (1, 2, 3, 4, 5, 6)
        print(f'({random.choice(namer)}, {random.choice(namer)})')
Diece.roll()