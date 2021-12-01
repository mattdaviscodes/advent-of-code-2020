class InvalidActionError(Exception):
    pass

class Coordinate:

    def __init__(self, east=0, north=0):
        self.east = east
        self.north = north

    @property
    def manhattan(self):
        return abs(self.east) + abs(self.north)

class Ship:
    HEADINGS = ['E', 'N', 'W', 'S']

    def __init__(self, east=0, north=0, heading=0):
        self.location = Coordinate(east, north)
        self.heading = heading

    def __repr__(self):
        return repr('Ship(east={}, north={}, heading={}, manhattan={})'.format(self.location.east, self.location.north, self.heading, self.manhattan))

    @property
    def manhattan(self):
        return self.location.manhattan

    def go(self, direction, distance):
        if direction == 'N':
            self.location.north += distance
        elif direction == 'S':
            self.location.north -= distance
        elif direction == 'E':
            self.location.east += distance
        elif direction == 'W':
            self.location.east -= distance

    def turn(self, direction, degrees):
        if direction == 'L':
            self.heading = (self.heading + degrees // 90) % 4
        elif direction == 'R':
            self.heading = (self.heading - degrees // 90) % 4

    def execute(self, instruction):
        action, value = self.decode_instruction(instruction)

        if action in self.HEADINGS:
            self.go(action, value)
        elif action in ['L', 'R']:
            self.turn(action, value)
        elif action == 'F':
            self.go(self.HEADINGS[self.heading], value)

    def decode_instruction(self, instruction):
        try:
            action = instruction[0]
            value = int(instruction[1:])
            return action, value
        except:
            raise InvalidActionError('Malformed instruction: {}'.format(instruction))
