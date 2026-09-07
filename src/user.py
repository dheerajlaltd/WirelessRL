import random
from src.enums import Region

class User:
    def __init__(self,region:Region):
        self.region=region
    def display(self):
        print(f'User Region:{self.region}')
    def move(self):
        if self.region==Region.LEFT:
            self.region=random.choice([Region.LEFT,Region.CENTRE])
        elif self.region==Region.CENTRE:
            self.region=random.choice([Region.LEFT,Region.CENTRE,Region.RIGHT])
        elif self.region==Region.RIGHT:
            self.region=random.choice([Region.CENTRE,Region.RIGHT])