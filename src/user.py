import random
from src.enums import Region

class User:
    def __init__(self,region:Region):
        self.region=region

        self.transition_table={
            Region.LEFT:{Region.LEFT:.8,Region.CENTRE:.2},
            Region.CENTRE:{Region.LEFT:.2, Region.CENTRE:.6,Region.RIGHT:.2},
            Region.RIGHT:{Region.CENTRE:.2,Region.RIGHT:.8}
            
        }# Nested dictionary
    def display(self):
        print(f'User Region:{self.region}')
    # def move(self):
    #     if self.region==Region.LEFT:
    #         self.region=random.choice([Region.LEFT,Region.CENTRE])
    #     elif self.region==Region.CENTRE:
    #         self.region=random.choice([Region.LEFT,Region.CENTRE,Region.RIGHT])
    #     elif self.region==Region.RIGHT:
    #         self.region=random.choice([Region.CENTRE,Region.RIGHT])
    def move(self):
        transitions=self.transition_table[self.region] # is the current dictionary
        possible_regions=list(transitions.keys())
        probabilities=list(transitions.values)
        self.region=random.choices(possible_regions,weights=probabilities,k=1)[0]