import random
from src.enums import Region
class Mobility_model:
    # base class for mobility models
    pass
class Random_walk_mobility(Mobility_model):
    # Random walk mobility model in which the user can stay in the current region
    # or move to the neighbouring region.
    def __init__(self):
        self.transition_table={Region.LEFT:{Region.LEFT:.8,Region.CENTRE:.2},
                               Region.CENTRE:{Region.LEFT:.2,Region.CENTRE:.6,Region.RIGHT:.2},
                               Region.RIGHT:{Region.CENTRE:.2,Region.RIGHT:.8}}
    def move(self,user):
        # moving the user according to the transition probabilities
        transitions=self.transition_table[user.region]
        next_regions=list(transitions.keys())
        probabilities=list(transitions.values())
        user.region=random.choices(next_regions,weights=probabilities,k=1)[0]
