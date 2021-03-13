import re

with open('./days/day3.txt') as f:
    fileInput = f.readlines()
    triangles = list(map(lambda l: list(map(int, re.split(' +', l.strip()))), fileInput))


def part1():
    return len(list(filter(lambda t: sum(t) > max(t) * 2, triangles)))
