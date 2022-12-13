import time

class Monkey:
    def __init__(self, manage_worry=True):
        self.manage_worry = manage_worry
        self.id = 0
        self.items = []
        self.operation = ""  # stringified python code to exec later
        self.divisible_by = 0
        self.if_true = 0
        self.if_false = 0
        self.inspect_count = 0

    def __repr__(self):
        return "Monkey(id={}, items={}, operation='{}', divisible_by={}, if_true={}, if_false={}, inspect_count={})".format(self.id, self.items, self.operation, self.divisible_by, self.if_true, self.if_false, self.inspect_count)

    @classmethod
    def from_input(cls, input, manage_worry=True):
        new_monkey = cls(manage_worry)

        for i, line in enumerate(input):
            if i == 0:
                new_monkey.id = int(line.split(" ")[1].replace(":", ""))
            elif i == 1:
                line = line.replace("Starting items:", "").replace(" ", "")
                new_monkey.items = [int(item) for item in line.split(",")]
            elif i == 2:
                line = line.replace("  Operation: new = ", "")
                new_monkey.operation = "lambda old: {}".format(line)
            elif i == 3:
                new_monkey.divisible_by = int(line.replace("  Test: divisible by ", ""))
            elif i == 4:
                new_monkey.if_true = int(line.replace("    If true: throw to monkey ", ""))
            elif i == 5:
                new_monkey.if_false = int(line.replace("    If false: throw to monkey ", ""))

        return new_monkey

    def throw_item(self, item):
        if item % self.divisible_by == 0:
            return (item, self.if_true)

        return (item, self.if_false)

    def inspect_items(self):
        throws = []
        items_copy = list(self.items)
        for i, item in enumerate(items_copy):
            self.inspect_count += 1
            self.items[i] = eval(self.operation)(item)

            if self.manage_worry:
                self.items[i] = self.items[i] // 3

            throws.append(self.throw_item(self.items[i]))
        
        # monkey should have no items after their turn
        self.items = []

        return throws


def get_input():
    with open("test-input.txt", "r") as f:
        return f.read().splitlines()

def part_one(input):
    manage_worry = True
    monkeys = []
    monkey_lines = []
    for i, line in enumerate(input):
        if line == "":
            monkey = Monkey.from_input(monkey_lines, manage_worry)
            monkeys.append(monkey)
            monkey_lines = []
        else:
            monkey_lines.append(line)

    # last monkey gets left out without this
    monkey = Monkey.from_input(monkey_lines, manage_worry)
    monkeys.append(monkey)

    # 20 rounds
    for _ in range(20):

        for monkey in monkeys:
            throws = monkey.inspect_items()
            for item, monkey_id in throws:
                monkeys[monkey_id].items.append(item)

    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    monkey_business = monkeys[0].inspect_count * monkeys[1].inspect_count

    print("Part One: {}".format(monkey_business))


def part_two(input):
    manage_worry = False
    monkeys = []
    monkey_lines = []
    for i, line in enumerate(input):
        if line == "":
            monkey = Monkey.from_input(monkey_lines, manage_worry)
            monkeys.append(monkey)
            monkey_lines = []
        else:
            monkey_lines.append(line)

    # last monkey gets left out without this
    monkey = Monkey.from_input(monkey_lines, manage_worry)
    monkeys.append(monkey)

    # 10,000 rounds
    for _ in range(1000):
        print("ROUND {} START".format(_))

        for monkey in monkeys:
            throws = monkey.inspect_items()
            for item, monkey_id in throws:
                monkeys[monkey_id].items.append(item)

        print("COMPLETE")

    monkeys.sort(key=lambda x: x.inspect_count, reverse=True)
    monkey_business = monkeys[0].inspect_count * monkeys[1].inspect_count

    print(monkeys[0].inspect_count, monkeys[1].inspect_count)

    print("Part Two: {}".format(monkey_business))

if __name__ == "__main__":
    input = get_input()

    # part_one(input)
    part_two(input)