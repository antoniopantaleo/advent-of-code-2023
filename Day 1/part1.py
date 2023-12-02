import re

DEMO = False

input = "demo1.txt" if DEMO else "input.txt"
lines = list(map(lambda x: x.strip(), open(input).readlines()))

digits_regex = r"\d"
digits_per_line = [re.findall(digits_regex, i) for i in lines]
pairs = [f"{digits[0]}{digits[-1]}" for digits in digits_per_line]
pairs = list(map(lambda x: int(x), pairs))

print(sum(pairs))
