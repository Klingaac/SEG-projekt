import random as r
import globals

# Globals

all_marbles = {}
marble_id = 0

class marble:
    def __init__(self, x=0, y=0):
        global marble_id
        global all_marbles

        # position
        self.x = x
        self.y = y

        # physics properties
        self.velocity = 0
        self.weight = 1

        # incase i'd like to add varity to radii of marbles, just randomize ts value
        self.radius = globals.MARBLE_RADIUS 

        self.color = random_color()

        # give marble a unique id
        marble_id += 1
        self.ID = marble_id

        all_marbles[marble_id] = self

    def newPos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y




def getMarbles() -> dict[int, any]:
    return all_marbles

def getMarble(ID):
    return all_marbles[id]

def random_color():
    return (r.randint(1,255), r.randint(1,255), r.randint(1,255))