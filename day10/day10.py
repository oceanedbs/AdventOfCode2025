# light []
# button wiring ()
# joltage requirement {}

# # = on 
# . = off (initially off)
from collections import deque 

def parse_data(filename):
    machines = []
    with open(filename) as f:
        for line in f:
            line = line.strip()

            # lights
            lights = line[line.index('[')+1:line.index(']')]

            # buttons
            buttons = []
            i = 0
            while '(' in line[i:]:
                start = line.index('(', i)
                end = line.index(')', start)
                buttons.append(tuple(map(int, line[start+1:end].split(','))))
                i = end + 1

            machines.append((lights, buttons))
    return machines

def lights_to_mask(lights):
    mask = 0
    for i, c in enumerate(lights):
        if c == '#':
            mask |= (1 << i)
    return mask


def button_to_mask(button):
    mask = 0
    for i in button:
        mask |= (1 << i)
    return mask

def min_presses(lights, buttons):
    n = len(lights)
    target = lights_to_mask(lights)
    button_masks = [button_to_mask(b) for b in buttons]

    start = 0
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, presses = queue.popleft()
        if state == target:
            return presses

        for b in button_masks:
            next_state = state ^ b
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, presses + 1))

    return float('inf')  # should never happen

machines = parse_data("data.txt")

total = 0
for lights, buttons in machines:
    total += min_presses(lights, buttons)

print("Fewest total button presses:", total)
