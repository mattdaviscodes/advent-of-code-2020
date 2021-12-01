from data import DATA
from pprint import pprint

def parse_mask(mask_line):
    mask_string = mask_line.split(' = ')[-1]
    or_mask = int(mask_string.replace('X', '0'), 2)
    and_mask = int(mask_string.replace('X', '1'), 2)
    return or_mask, and_mask

def parse_instruction(input_line):
    mem_string, val_string = input_line.split(' = ')
    address = int(mem_string[4:-1])
    value = int(val_string)
    return address, value


if __name__ == "__main__":
    mem = {}
    or_mask = 0
    and_mask = 0

    for line in DATA.splitlines():
        if line[:4] == 'mask':
            or_mask, and_mask = parse_mask(line)
            continue

        address, value = parse_instruction(line)

        mem[address] = (value | or_mask) & and_mask

    mem_sum = sum([val for val in mem.values()])

    
    print(mem_sum)