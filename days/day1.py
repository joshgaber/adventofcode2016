with open('./days/day1.txt') as f:
    content = f.readlines()[0]
    instructions = content.split(', ')


def part1():
    location = _traverse()

    return f"{abs(location[0]) + abs(location[1])} steps away from origin"


def part2():
    location = _traverse(True)

    return f"{abs(location[0]) + abs(location[1])} steps away from origin at a previously visited point"


def _traverse(stop_at_repeat_location=False):
    location = [0, 0]
    direction = [0, 1, 0, -1]
    visited = ['0,0']

    for i in instructions:
        if i[0] == 'R':
            direction.append(direction.pop(0))
        else:
            direction.insert(0, direction.pop())
        for _ in range(int(i[1:])):
            location[0] += direction[0]
            location[1] += direction[1]
            if stop_at_repeat_location:
                location_s = ','.join(map(lambda x: str(x), location))
                if location_s in visited:
                    return location
                visited.append(location_s)

    return location
