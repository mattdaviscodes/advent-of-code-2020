from data import DATA
from passport import Passport
from pprint import pprint

# Split on blank lines, then replace newlines with spaces
data_clean = [block.replace('\n', ' ') for block in DATA.split('\n\n')]

if __name__ == "__main__":
    valid = 0
    for item in data_clean:
        passport = Passport.from_string(item)
        valid += passport.validate_part_one()

    print("PART ONE\n=======")
    print('Valid Passports: {}'.format(valid))

    valid = 0
    for item in data_clean:
        passport = Passport.from_string(item)
        valid += passport.validate_part_two()

    print("\nPART TWO\n=======")
    print('Valid Passports: {}'.format(valid))