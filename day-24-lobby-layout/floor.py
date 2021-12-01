class Tile:
    def __init__(self, e=None, se=None, sw=None, w=None, nw=None, ne=None, color="white"):
        self.neighbors = {
            'e': e,
            'se': se,
            'sw': sw,
            'w': w,
            'nw': nw,
            'ne': ne
        }
        self.color = color

    def link(self, tile, direction):
        dir_map = {
            'e': 'w',
            'se': 'nw',
            'sw': 'ne',
            'w': 'e',
            'nw': 'se',
            'ne': 'sw',
        }
        self.neighbors[direction] = tile
        tile.neighbors[dir_map[direction]] = self


    def flip(self):
        if self.color == "white":
            self.color = "black"
        else:
            self.color = "white"

        return self.color

class TileFloor:
    def __init__(self, traverse=False):
        self.traverse = traverse
        self.reference = Tile()
        self.current = self.reference
        self.tiles = [self.reference]

    @property
    def count(self):
        return len(self.tiles)

    @property
    def count_white(self):
        return len(self.get_white())

    @property
    def count_black(self):
        return len(self.get_black())

    def get_color(self, color):
        tiles = []
        for tile in self.tiles:
            if tile.color == color:
                tiles.append(tile)
        return tiles
    
    def get_white(self):
        return self.get_color("white")

    def get_black(self):
        return self.get_color("black")

    def new_tile(self, direction, **kwargs):
        tile = Tile()

        tile = Tile(**kwargs)
        self.tiles.append(tile)
        return tile

    def visit(self):
        return self.current.flip()

    def move(self, direction):
        if direction == "e":
            if not self.current.e:
                self.current.e = self.new_tile(w=self.current, nw=self.current.ne, sw=self.current.se)
            self.current = self.current.e
        elif direction == "se":
            if not self.current.se:
                self.current.se = self.new_tile(nw=self.current, w=self.current.sw, ne=self.current.e)
            self.current = self.current.se
        elif direction == "sw":
            if not self.current.sw:
                self.current.sw = self.new_tile(ne=self.current, nw=self.current.nw, e=self.current.se)
            self.current = self.current.sw
        elif direction == "w":
            if not self.current.w:
                self.current.w = self.new_tile(e=self.current, ne=self.current.nw, se=self.current.sw)
            self.current = self.current.w
        elif direction == "nw":
            if not self.current.nw:
                self.current.nw = self.new_tile(se=self.current, sw=self.current.w, e=self.current.ne)
            self.current = self.current.nw
        elif direction == "ne":
            if not self.current.ne:
                self.current.ne = self.new_tile(sw=self.current, w=self.current.nw, se=self.current.e)
            self.current = self.current.ne

    def parse_instruction(self, instruction):
        allowed_directions = ['se', 'sw', 'ne', 'nw', 'e', 'w']
        steps = []

        while instruction:
            for direction in allowed_directions:
                if instruction.startswith(direction):
                    steps.append(direction)
                    instruction = instruction[len(direction):]

        return steps

    def execute(self, instruction):
        steps = self.parse_instruction(instruction)
        print(steps)
        self.current = self.reference
        for step in steps:
            self.move(step)
        # If we're traversing, update the reference node to the current node
        if self.traverse:
            self.reference = self.current
        self.visit()
