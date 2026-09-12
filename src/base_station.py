from src.beam import Beam
class BaseStation:
    # Represents the 6G base station
    def __init__(self,num_beams:int):
        # This is the constructor and the parameter is the number of beams
        # available at the base station
        self.num_beams=num_beams
        self.beams=[Beam(beam_id) for beam_id in range(num_beams)]
    def display_beams(self):
        # This method displays all the available beams at the base station
        print('The available beams are :')
        for beam in self.beams:
            beam.display()