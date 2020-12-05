with open("input.txt", "rt") as handle:
    input_text = handle.read()

meta, is_between, noop = (lambda *args: args), (lambda a, b, *v: a <= int(*v) <= b), (lambda *v: True)
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

field_validators = {
    "byr": lambda v: is_between(1920, 2002, v),
    "iyr": lambda v: is_between(2010, 2020, v),
    "eyr": lambda v: is_between(2020, 2030, v),
    "hgt": lambda v: is_between(59, 76, v.split("in")[0]) if "in" in v else is_between(150, 193, v.split("cm")[0]),
    "hcl": lambda v: v[0] is "#" and is_between(0, 8**8-1, v[1:], 16),
    "ecl": lambda v: v in eye_colors,
    "pid": lambda v: str(int(v)) and len(v) is 9,
    "cid": noop,
}

def create_passport_entries(passport_string):
    passport_data = passport_string.split()
    return {entry.split(":")[0]: entry.split(":")[1] for entry in passport_data}

def validate_passport(passport):
    try:
        for field, validator in field_validators.items():
            assert(validator(passport.get(field)))
    except: return False
    return True


passports = [
    create_passport_entries(passport_string)
    for passport_string
    in [line for line in input_text.split("\n\n") if line]
    if validate_passport(create_passport_entries(passport_string))
]
