import re

DEMO = False

input = open("input-demo.txt" if DEMO else "input.txt").readlines()
input = list(map(lambda x: x.strip(), input))

selected_numbers = []


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


def has_char_nearby(num_range, line_idx) -> bool:
    y = line_idx
    start = num_range[0]
    end = num_range[-1]
    special_char_regex = r"[^.\d\w]"
    intervals = create_intervals(start, end, y)
    for interval in intervals:
        x = interval[0]
        y = interval[-1]
        char = input[y][x]
        if re.search(special_char_regex, char) is not None:
            return True
    return False


for line_idx, line in enumerate(input):
    iterator = re.finditer(r"\d+", line)
    for match in iterator:
        num_range = match.span()
        if has_char_nearby(num_range, line_idx):
            number = match.group()
            selected_numbers.append(int(number))

print(sum(selected_numbers))
