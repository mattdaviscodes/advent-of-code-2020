class Validator:

    @staticmethod
    def _range(val, min, max):
        return val >= min and val <= max

    @staticmethod
    def byr(val):
        try:
            return Validator._range(int(val), 1920, 2002)
        except:
            return False

    @staticmethod
    def iyr(val):
        try:
            return Validator._range(int(val), 2010, 2020)
        except:
            return False
    
    @staticmethod
    def eyr(val):
        try:
            return Validator._range(int(val), 2020, 2030)
        except:
            return False

    @staticmethod
    def hgt(val):
        try:
            if val.endswith(('cm')):
                return Validator._range(int(val[:-2]), 150, 193)
            elif val.endswith(('in')):
                return Validator._range(int(val[:-2]), 59, 76)
        except:
            pass

        return False
    
    @staticmethod
    def hcl(val):
        hex_chars = '0123456789abcdef'
        valid = True
        
        try:
            if not val.startswith('#'):
                return False
            
            for char in val[1:]:
                if char not in hex_chars:
                    return False
                
            return True
        except:
            return False

    @staticmethod
    def ecl(val):
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    @staticmethod
    def pid(val):
        try:
            return len(val) == 9
        except:
            return False

    @staticmethod
    def cid(val):
        return True
