from src.enums import Region
from src.user import User
from src.mobility import Random_walk_mobility
from src.base_station import BaseStation

def main():
    # Creation of a user in the centre region
    user=User(Region.CENTRE)
    print("\n\nWELCOME TO RL WORLD\n")
    # Creation of the mobility model
    mobility=Random_walk_mobility()
    # Creation of base station with 3 beams
    base_station=BaseStation(num_beams=3)
    print('Initial Position')
    user.display()
    print()
    base_station.display_beams()
    print('\nUser Movement')
    for step in range(20):
        mobility.move(user)
        print(f"Time Step {step+1}:",end="")
        user.display()
if __name__=="__main__":
    main()
