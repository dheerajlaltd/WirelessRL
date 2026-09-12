class Beam:
    # Represents a transmission beam from the base station/gNB
    def __init__(self,beam_id:int):
        # This is the constructor and the parameter is the beam_id which is the 
        # unique identifier of the beam
        self.beam_id=beam_id
    def display(self):
        # displays the beam info
        print(f'Beam ID:{self.beam_id}')
