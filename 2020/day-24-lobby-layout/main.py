from data import DATA
from floor import TileFloor

instructions = DATA.splitlines()

if __name__ == "__main__":
    floor = TileFloor()

    for instruction in instructions:
        floor.execute(instruction)

    print(floor.count_black)