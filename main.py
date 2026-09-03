from src.enums import Region
from src.user import User

def main():
    user=User(Region.CENTRE)
    print('Initial Position')
    user.display()
    print('\nUser Movement')
    for step in range(10):
        user.move()
        print(f"Step {step+1}:",end="")
        user.display()
if __name__=="__main__":
    main()