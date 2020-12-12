from data import DATA
from ship import Ship

if __name__ == "__main__":
    ship = Ship()
    for instruction in DATA.splitlines():
        ship.execute(instruction)
        
    print('PART ONE\n=======')
    print('Ship Manhattan distance: {}'.format(ship.manhattan))