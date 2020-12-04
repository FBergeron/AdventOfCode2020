input_data_filename = "passport_data.txt"

mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

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

invalid_count = 0
for passport in passports:
    for field in mandatory_fields:
        # print(f"field={field} password.keys={passport.keys()} member? = {field in passport.keys()}")
        if field not in list(passport.keys()):
            invalid_count += 1
            break
print(f"valid={len(passports)-invalid_count} invalid={invalid_count}")    
