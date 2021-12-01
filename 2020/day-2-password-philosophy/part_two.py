from data import DATA

def parse_policy(policy_string):
    range_string, letter = policy_string.split()
    first, second = [int(num) - 1 for num in range_string.split('-')]

    return letter, first, second

def validate_password(password, letter, first, second):
    letters = password[first] + password[second]

    return letters.count(letter) == 1

if __name__ == "__main__":
    valid_count = 0
    
    for password_string in DATA:
        policy_string, password = password_string.split(': ')
        letter, first, second = parse_policy(policy_string)
        
        valid_count += validate_password(password, letter, first, second)
    
    print(valid_count)
