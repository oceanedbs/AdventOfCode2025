import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Part 1 

start = 50 
count_0 = 0 

data_file = Path(__file__).with_name("data.txt")
with data_file.open("r", encoding="utf-8") as f:
    rows = []
    for line in f:
        line = line.rstrip("\n")
        if not line:
            continue
        first, rest = line[0], line[1:].strip()
        rows.append((first, rest))

print(rows)

for dir, step in rows:
    step = int(step)
    if dir == "R":
        start += step
        if start > 99:
            start = (start - 100)%100
    elif dir == "L":
        start -= step
        if start < 0:
            start = 100 - abs(start)%100
    if start == 0 or start == 100:
        count_0 += 1
    print(f"Direction: {dir} Step: {step} New position: {start} count_0: {count_0}")

print(f"Count of position 0: {count_0}")

# Part 2


# Part 2
print('\nPart 2\n')

count_0 = 0
position = 50
prev_position = 50


for dir, step in rows:
        step = int(step)
        for _ in range(step): # simulate EVERY click
            if dir == "R":
                position = (position + 1) % 100
            else:  # direction == "L"
                position = (position - 1) % 100
            
            if position == 0:
                count_0 += 1
        

print(f"Count of position 0: {count_0}")