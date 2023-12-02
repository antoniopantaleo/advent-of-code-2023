import re

DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
lines = list(map(lambda x: x.strip(), open(input).readlines()))

rules = {"red": 12, "green": 13, "blue": 14}

result = 0

for game in lines:
    setup_regex = r"Game (\d+):(.+)"
    match = re.match(setup_regex, game)
    id = int(match.group(1))
    rounds = match.group(2).split(";")
    game_regex = r"(\d+) (red|green|blue)"
    try:
        for round in rounds:
            iterator = re.finditer(game_regex, round)
            try:
                for match in iterator:
                    color = match.group(2)
                    occurences = int(match.group(1))
                    if occurences > rules[color]:
                        raise StopIteration
            except StopIteration:
                raise StopIteration
        result += id
    except StopIteration:
        pass

print(result)
