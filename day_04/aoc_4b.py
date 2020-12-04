input_data_filename = "passport_data.txt"

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']


def is_year_valid(str, min, max):
    try:
        year = int(str)
        return year >= min and year <= max
    except:
        return False


def is_valid(passport):
    if 'byr' not in passport or not is_year_valid(passport['byr'], 1920, 2002):
        return False

    if 'iyr' not in passport or not is_year_valid(passport['iyr'], 2010, 2020):
        return False

    if 'eyr' not in passport or not is_year_valid(passport['eyr'], 2020, 2030):
        return False

    if 'hgt' not in passport:
        return False

    height_str = passport['hgt']
    try:
        height = int(height_str[:-2])
        if height_str.endswith("cm"):
            if height < 150 or height > 193:
                return False
        if height_str.endswith("in"):
            if height < 59 or height > 76:
                return False
    except:
        return False

    if 'hcl' not in passport:
        return False

    color = passport['hcl']
    if not color.startswith('#'):
        return False
    for c in color[1:]:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]:
            return False

    if 'ecl' not in passport:
        return False

    color = passport['ecl']
    if color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if 'pid' not in passport:
        return False

    pid_str = passport['pid']
    if len(pid_str) != 9: 
        return False
    for c in pid_str:
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    try:
        pid = int(pid_str)
    except:
        return False

    return True

passports = []
with open(input_data_filename, 'r') as input_file:
    passport = {}
    for line in input_file:
        if line == "\n":
            passports.append(passport)
            passport = {}
        pairs = line.strip().split()
        for pair in pairs:
            k, v = pair.split(":")
            passport[k] = v
    passports.append(passport)
print(f"{len(passports)} has been read.")

valid_count = 0
for passport in passports:
    if is_valid(passport):
        valid_count += 1

print(f"valid={valid_count} invalid={len(passports) - valid_count}")    

