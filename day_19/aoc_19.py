from itertools import combinations
import re
import sys

input_data_filename = "rules_msg_data.txt"
# input_data_filename = "rules_msg_data_short.txt"
# input_data_filename = "rules_msg_data_very_short.txt"

rules = []
messages = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        match = re.search("(\d+): (.+)", line)
        if match:
            rule_index = int(match.group(1))
            rule_str = match.group(2)
            submatch = re.search("\"(.)\"", rule_str)
            if submatch:
                rules.append(submatch.group(1))
            else:
                parts = rule_str.split(' | ')
                rule_list = []
                for part in parts:
                    rule_list.append([int(x) for x in part.split()])
                rules.append(rule_list)
        elif line == '':
            continue
        else:
            messages.append(list(line))
print(f"rules={rules}")
print(f"messages={messages}")


def is_valid_rec(rule_index, msg):
    print(f"is_valid_rec(rule_index={rule_index} msg={msg}")
    if isinstance(rules[rule_index], str):
        if len(msg) > 0 and msg[0] == rules[rule_index]:
            return 1
        else:
            return 0
    else:
        rule_list = rules[rule_index]
        print(f"rule_list={rule_list}")
        for rule in rule_list:
            print(f"rule={rule}")
            sub_results = []
            char_count = 0
            for rule_index in rule:
                print(f"rule_index={rule_index}")
                sub_result = is_valid_rec(rule_index, msg)
                print(f"sub_result={sub_result}")
                if sub_result == 0:
                    break
                sub_results.append(sub_result)
                char_count += sub_result
                msg = msg[sub_result:]
            if len(sub_results) == len(rule):
                return char_count
        return 0 


def is_valid(msg):
    result = is_valid_rec(0, msg)
    print(f"result={result} len(msg)={len(msg)}")
    return result == len(msg)


valid_msg_count = 0
for message in messages:
    print(f"\nValidating msg={message}")
    if is_valid(message):
        valid_msg_count += 1
print(f"valid_msg_count={valid_msg_count}")
