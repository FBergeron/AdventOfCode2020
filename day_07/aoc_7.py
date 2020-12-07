input_data_filename = "rules.txt"

bag_content = {}
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        bag = None
        content = []
        line = line.strip()
        container_part, content_part = line.split(" contain ")
        bag = container_part[:-5]
        if content_part == "no other bags.":
            content = []
        else:
            subcontent_parts = content_part.split(", ")
            for subcontent_part in subcontent_parts:
                number_str = subcontent_part[:subcontent_part.index(" ")]
                subbag = subcontent_part[subcontent_part.index(" ") + 1:subcontent_part.index(" bag")]
                content.append((int(number_str), subbag))
        bag_content[bag]=content
print(bag_content)


# Part 1.

def find_bag_that_contains(looked_for_bag):
    bags = set()
    for bag in bag_content:
        content = bag_content[bag]
        # print(f"bag={bag} content={content}")
        for subcontent in content:
            # print(f"subcontent={subcontent}")
            number, subbag = subcontent
            # print(f"number={number} subbag={subbag}")
            if subbag == looked_for_bag:
                bags.add(bag)
                break
    return bags

def search_bag_rec(bag):
    bags = set()
    print(f"\nsearch_bag_rec bag={bag}")
    container_bags = find_bag_that_contains(bag)
    if len(container_bags) == 0:
        return bags
    bags = bags.union(container_bags)
    for container_bag in container_bags:
        bags = bags.union(search_bag_rec(container_bag))
    return bags

bags = search_bag_rec("shiny gold")
print(bags)
print(len(bags))

# Part 2.

def count_bag_rec(bag):
    print(f"count_bag_rec bag={bag}")
    count = 0
    for content in bag_content[bag]:
        number, bag = content
        count += number + number * count_bag_rec(bag)
    return count

count = count_bag_rec("shiny gold")
print(count)
