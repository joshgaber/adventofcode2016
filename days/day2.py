with open('./days/day2.txt') as f:
    moves = f.readlines()

KEYMAP1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

KEYMAP2 = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]


def part1():
    start = [1, 1]
    keys = []
    for move in moves:
        for c in move:
            if c == 'U':
                start[1] = max(0, start[1] - 1)
            elif c == 'D':
                start[1] = min(2, start[1] + 1)
            elif c == 'L':
                start[0] = max(0, start[0] - 1)
            elif c == 'R':
                start[0] = min(2, start[0] + 1)
        keys.append(KEYMAP1[start[1]][start[0]])
    return f"Keycode: {''.join(keys)}"


def part2():
    start = [0, 2]
    keys = []
    for move in moves:
        for c in move:
            if c == 'U':
                start[1] = max(abs(2 - start[0]), start[1] - 1)
            elif c == 'D':
                start[1] = min(-abs(start[0] - 2) + 4, start[1] + 1)
            elif c == 'L':
                start[0] = max(abs(2 - start[1]), start[0] - 1)
            elif c == 'R':
                start[0] = min(-abs(start[1] - 2) + 4, start[0] + 1)
        keys.append(KEYMAP2[start[1]][start[0]])
    return f"Keycode: {''.join(keys)}"
