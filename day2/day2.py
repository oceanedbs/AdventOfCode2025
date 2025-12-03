import numpy as np
from pathlib import Path

data_path = Path(__file__).parent / "data.txt"
raw = data_path.read_text().strip()

parts = [p.strip() for p in raw.split(",") if p.strip()]

def to_tuple(s):
    items = [it.strip() for it in s.split("-")]
    out = []
    for it in items:
        try:
            out.append(int(it))
        except ValueError:
            out.append(it)
    return tuple(out)

tuples = [to_tuple(p) for p in parts]

print(tuples)

### Part 1 #####

invalidID = 0
for t in tuples:
    if len(t) < 2:
        continue

    a, b = t[0], t[1]
    if isinstance(a, int) and isinstance(b, int):
        seq = list(range(a, b + 1)) if a <= b else list(range(a, b - 1, -1))
    else:
        seq = []

    print(seq)
    parts_of_number = []
    for num in seq:
        s = str(num)
        neg = s.startswith('-')
        digits = s[1:] if neg else s

        if len(digits) % 2 == 0 and len(digits) > 0:
            mid = len(digits) // 2
            left = int(digits[:mid]) * (-1 if neg else 1)
            right = int(digits[mid:])
            result = (left, right)
            if left == right: 
                invalidID += num 
       

print('Final invalid ID sum:', invalidID)

#### Part 2 #####
print('\nPart 2\n')

def is_repeated_pattern(s):
    return s in (s + s)[1:-1]


invalidID = 0
for t in tuples:
    if len(t) < 2:
        continue

    a, b = t[0], t[1]
    if isinstance(a, int) and isinstance(b, int):
        seq = list(range(a, b + 1)) if a <= b else list(range(a, b - 1, -1))
    else:
        seq = []

    print(seq)
    parts_of_number = []
    for num in seq:
        s = str(num)
        neg = s.startswith('-')
        digits = s[1:] if neg else s

        if is_repeated_pattern(digits):
            invalidID += num
            print(f"Number {num} has repeated pattern.")

print('Final invalid ID sum for Part 2:', invalidID)
       