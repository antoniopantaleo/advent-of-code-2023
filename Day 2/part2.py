import re
from functools import reduce

DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
lines = list(map(lambda x: x.strip(), open(input).readlines()))

result = 0

for game in lines:
    setup_regex = r"Game \d+:(.+)"
    match = re.match(setup_regex, game)
    rounds = match.group(1).split(";")
    bag = {"red": 0, "green": 0, "blue": 0}
    game_regex = r"(\d+) (red|green|blue)"
    for round in rounds:
        iterator = re.finditer(game_regex, round)
        for match in iterator:
            color = match.group(2)
            count = int(match.group(1))
            if count > bag[color]:
                bag[color] = count
    power = reduce(lambda x, y: x * y, bag.values())
    result += power

print(result)
