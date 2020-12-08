from data import DATA
from pprint import pprint

instructions = DATA.splitlines()

if __name__ == "__main__":
    acc = 0
    pc = 0

    pc_history = []
    pc_exit = len(instructions)

    while True:
        if pc in pc_history:
            break

        pc_history.append(pc)

        op, arg = instructions[pc].split()
        arg = int(arg)

        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        else:
            pc += 1

    print('PART ONE\n=======')
    print('Accumulator before loop: {}'.format(acc))





