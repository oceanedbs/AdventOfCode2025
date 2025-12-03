import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Part 1 

start = 50 
count_0 = 0 

data_file = Path(__file__).with_name("dataExemple.txt")
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
    print(f"Direction: {dir} Step: {step} New position: {start}")

print(f"Count of position 0: {count_0}")

# Part 2


# Part 2
print('\nPart 2\n')

count_0 = 0
position = 50
prev_position = position

for i, (dir, step) in enumerate(rows):
    print(f"\n Step {i}: Current Position: {position} Direction: {dir} Step: {step} Counter Value: {count_0}")
    step = int(step)
    # Handling 'R' (Right) direction:
    if dir == "R":
        prev_position = position  # Save the previous position before moving
        position += step
        
        # Check for crossing from below to exactly 100 (only if we were below 100)
        if prev_position < 100 and position >= 100:  # Crossing from below to 100
            count_0 += 1
            position = 0  # Reset the position to 0 (wrap around)
            print(f"Increment +1 at position 100. Updated Counter: {count_0} New position: {position}")
        elif position > 100:  # Going beyond 100 (wrap around)
            count_0 += position // 100  # Increment based on how many times it wrapped
            position = position % 100   # Reset position to within 100
            print(f"Increment: {position // 100}. Updated Counter: {count_0} New position: {position}")
    
    # Handling 'L' (Left) direction:
    elif dir == "L":
        prev_position = position  # Save the previous position before moving
        position -= step
        
        # Check for crossing from above to exactly 0 (only if we were above 0)
        if prev_position > 0 and position <= 0:  # Crossing from above to 0
            count_0 += 1
            position = 0  # Reset to position 0
            print(f"Increment +1 at position 0. Updated Counter: {count_0} New position: {position}")
        elif position < 0:  # Going below 0 (wrap around)
            count_0 += (abs(position) // 100) + 1  # Count how many wraps around
            position = (100 + position) % 100  # Reset position within [0, 100] range
            print(f"Increment: {abs(position) // 100 + 1}. Updated Counter: {count_0} New position: {position}")

    
    # Print the direction, step, and position at each step
    print(f"Direction: {dir} Step: {step} New position: {position}, new count_0: {count_0}")

print(f"Count of position 0: {count_0}")