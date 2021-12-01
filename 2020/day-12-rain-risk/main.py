from data import DATA
from ship import Ship, Coordinate

class WaypointShip(Ship):

    def __init__(self, east=0, north=0, heading=0):
        super().__init__(east=east, north=north, heading=heading)
        self.waypoint = Coordinate(10, 1)

    def move_waypoint(self, direction, distance):
        if direction == 'N':
            self.waypoint.north += distance
        elif direction == 'S':
            self.waypoint.north -= distance
        elif direction == 'E':
            self.waypoint.east += distance
        elif direction == 'W':
            self.waypoint.east -= distance

    def rotate_waypoint(self, direction, degrees):
        turns = (degrees // 90) % 4

        while turns:
            if direction == 'L':
                tmp = self.waypoint.east
                self.waypoint.east = self.waypoint.north * -1
                self.waypoint.north = tmp
            elif direction == 'R':
                tmp = self.waypoint.north
                self.waypoint.north = self.waypoint.east * -1
                self.waypoint.east = tmp

            turns -= 1

    def go_to_waypoint(self, times):
        self.location.east += self.waypoint.east * times
        self.location.north += self.waypoint.north * times
    
    def execute(self, instruction):
        action, value = self.decode_instruction(instruction)

        if action in self.HEADINGS:
            self.move_waypoint(action, value)
        elif action in ['L', 'R']:
            self.rotate_waypoint(action, value)
        elif action == 'F':
            self.go_to_waypoint(value)

if __name__ == "__main__":
    ship = Ship()
    for instruction in DATA.splitlines():
        ship.execute(instruction)
        
    print('PART ONE\n=======')
    print('Ship Manhattan distance: {}'.format(ship.manhattan))

    w_ship = WaypointShip()
    for instruction in DATA.splitlines():
        w_ship.execute(instruction)

    print('\nPART TWO\n=======')
    print('WaypointShip Manhattan distance: {}'.format(w_ship.manhattan))