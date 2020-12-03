with open("input.txt", "rt") as handle:
    input_text = handle.read()

def get_password_data(line):
    policy_string, password = line.split(": ")
    range, term = policy_string.split(" ")
    minimum, maximum = range.split("-")
    return int(minimum), int(maximum), term, password

def validate_password_data_old(data):
    minimum, maximum, term, password = data
    return minimum <= password.count(term) <= maximum

def validate_password_data_new(data):
    first, last, term, password = data
    matches = 0
    try:
        matches += 1 if password[first - 1] == term else 0
        matches += 1 if password[last - 1] == term else 0
    finally:
        return matches == 1

password_data_list = [get_password_data(line) for line in input_text.split("\n") if line]

validated = [validate_password_data_new(data) for data in password_data_list]

validated_count = [bool for bool in validated if bool].__len__()
