import re
from functools import reduce

DEMO = False

input = open("input-demo.txt" if DEMO else "input.txt").readlines()
input = list(map(lambda x: x.strip(), input))

powers = []

def search_recursively_right(line, index, offset=1):
    if index + offset >= len(line):
        return ""
    if not line[index + offset].isdigit():
        return ""
    number = line[index + offset]
    return number + search_recursively_right(line, index, offset + 1)


def search_recursively_left(line, index, offset=-1):
    number = line[index + offset]
    if not line[index + offset].isdigit() or index + offset < 0:
        return ""
    return search_recursively_left(line, index, offset - 1) + number


def get_number(line, index):
    if not line[index].isdigit():
        return None
    number = (
        search_recursively_left(line, index)
        + line[index]
        + search_recursively_right(line, index)
    )
    number = int(number)
    return number


def create_intervals(start, end, y):
    intervals = []
    for i in range(start, end):
        if i == start:
            if i - 1 >= 0:
                left = (i - 1, y)
                intervals.append(left)
                if y - 1 >= 0:
                    upper_left = (i - 1, y - 1)
                    intervals.append(upper_left)
                if y + 1 < len(input):
                    bottom_left = (i - 1, y + 1)
                    intervals.append(bottom_left)
        if i == end - 1:
            if i + 1 < len(input[0]):
                right = (i + 1, y)
                intervals.append(right)
                if y - 1 >= 0:
                    upper_right = (i + 1, y - 1)
                    intervals.append(upper_right)
                if y + 1 < len(input):
                    bottom_right = (i + 1, y + 1)
                    intervals.append(bottom_right)
        if y - 1 >= 0:
            top = (i, y - 1)
            intervals.append(top)
        if y + 1 < len(input):
            down = (i, y + 1)
            intervals.append(down)
    return intervals

for line_idx, line in enumerate(input):
    iterator = re.finditer(r"\*", line)
    for match in iterator:
        numbers = set()
        pos = match.span()[0]
        intervals = create_intervals(pos, pos + 1, line_idx)
        for interval in intervals:
            x = interval[-1]
            y = interval[0]
            char = input[y][x]
            if number := get_number(input[x], y):
                numbers.add(number)
        if len(numbers) == 2:
            power = reduce(lambda x, y: x * y, numbers)
            powers.append(power)

print(sum(powers))
