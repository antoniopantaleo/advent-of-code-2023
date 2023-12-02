import re

DEMO = False

input = "demo2.txt" if DEMO else "input.txt"
lines = list(map(lambda x: x.strip(), open(input).readlines()))

digits_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert_digit_if_possible(string):
    try:
        digit = digits_mapping[string]
        return digit
    except KeyError:
        return string


digits_groups = "|".join(digits_mapping.keys())
digits_regex = f"(?=(\\d|{digits_groups}))"
digits_per_line = [re.findall(digits_regex, i) for i in lines]
digits_per_line = list(
    map(lambda x: [convert_digit_if_possible(digit) for digit in x], digits_per_line)
)
pairs = [f"{digits[0]}{digits[-1]}" for digits in digits_per_line]
pairs = list(map(lambda x: int(x), pairs))

print(sum(pairs))
