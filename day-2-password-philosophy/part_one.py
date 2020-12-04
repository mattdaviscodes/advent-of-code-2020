from data import DATA

def parse_policy(policy_string):
    range_string, letter = policy_string.split()
    min, max = [int(num) for num in range_string.split('-')]

    return letter, min, max

def validate_password(password, letter, min, max):
    count = password.count(letter)

    return count >= min and count <= max

if __name__ == "__main__":
    valid_count = 0
    
    for password_string in DATA:
        policy_string, password = password_string.split(': ')
        letter, min, max = parse_policy(policy_string)
        
        if validate_password(password, letter, min, max):
            valid_count += 1
    
    print(valid_count)
