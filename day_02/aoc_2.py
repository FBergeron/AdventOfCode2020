import sys

input_data_filename = "my_password_entries.txt"

entries = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        freq_policy, char_policy, password = line.strip().split()
        entries.append((freq_policy, char_policy, password))

valid_password_count = 0
for entry in entries:
    freq_policy, char_policy, password = entry
    min_freq, max_freq = freq_policy.split('-')
    char = char_policy[0]
    char_count = 0
    for c in password:
        if c == char:
            char_count += 1
    if char_count >= int(min_freq) and char_count <= int(max_freq):
        valid_password_count += 1
print(valid_password_count)



