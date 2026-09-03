from enum import IntEnum

class Region(IntEnum):
    # User regions
    LEFT=0
    CENTRE=1
    RIGHT=2

    def __str__(self):
        return self.name