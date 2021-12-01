from data import DATA
from pprint import pprint

rules = DATA.splitlines()

def process_bags(rules):
    bags = {}
    for rule in rules:
        bag, contents = rule.split(' contain ')
        
        bag = bag.replace(' bags', '')
        contents = contents[:-1]  # remove period

        if bag not in bags:
            bags[bag] = {}

        if contents == 'no other bags':
            continue

        for content in contents.split(', '):
            content_split = content.split()

            count = int(content_split[0])
            content_bag = ' '.join(content_split[1:3])

            bags[bag][content_bag] = count

    return bags

def search(bags, search):
    valid_bags = []
    
    for bag in bags:

        if search in bfs(bags, bag):
            valid_bags.append(bag)

    return valid_bags

def bfs(graph, source):
    queue = [source]
    visited = []  # Don't include source node in visited to avoid false positives

    while queue:
        current = queue.pop(0)

        for neighbor in graph[current]:
            visited.append(neighbor)
            queue.append(neighbor)

    return visited


if __name__ == "__main__":
    bags = process_bags(rules)
    valid_bags = search(bags, 'shiny gold')

    print("PART ONE\n=======")
    print('Bags which may eventually hold Shiny Gold: {}'.format(len(valid_bags)))

    