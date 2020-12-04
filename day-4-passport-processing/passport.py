from validator import Validator

class Passport:
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    optional_keys = ['cid']

    validators = {
        'byr': Validator.byr,
        'iyr': Validator.iyr,
        'eyr': Validator.eyr,
        'hgt': Validator.hgt,
        'hcl': Validator.hcl,
        'ecl': Validator.ecl,
        'pid': Validator.pid,
        'cid': Validator.cid,
    }

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def validate_part_one(self):
        return all([getattr(self, key) for key in Passport.required_keys])

    def validate_part_two(self):
        for key, validate in Passport.validators.iteritems():
            value = getattr(self, key)
            if not validate(value):
                return False

        return True

    @classmethod
    def from_string(cls, data_string):
        passport = cls()
        pairs = data_string.split()
        
        for pair in pairs:
            key, val = pair.split(':')
            
            if key in cls.required_keys or key in cls.optional_keys:
                setattr(passport, key, val)

        return passport
