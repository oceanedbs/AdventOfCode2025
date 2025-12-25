import re


def parse_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    presents = {}
    christmas_trees = []

    idx = 0

    # Parse presents until we reach the trees section (e.g., "38x36: ...")
    while idx < len(lines):
        line = lines[idx].strip()

        # Skip blank separator lines
        if line == "":
            idx += 1
            continue

        # If we reach the trees section, stop parsing presents
        if re.match(r"^\d+x\d+:", line):
            break

        # Expect a present index (a single integer on the line)
        if re.match(r"^\d+$", line):
            present_index = int(line)
            grid = []

            # Read the next 3 lines as the grid
            for j in range(3):
                if idx + 1 + j < len(lines):
                    grid.append(lines[idx + 1 + j].strip())
                else:
                    raise ValueError("Unexpected end of file while reading present grid")

            presents[present_index] = grid

            # Advance past the index + its 3 grid lines
            idx += 4
            continue

        # If the line doesn't match expected formats, skip it
        idx += 1
    # Parse christmas trees (area like "38x36:" followed by indices)
    while idx < len(lines):
        line = lines[idx].strip()
        print(f"Processing line: {line}, idx: {idx}")
        if line:
            area_part, indices_part = line.split(':', 1)
            area = area_part.strip()
            indices = [int(x) for x in indices_part.split()]
            christmas_trees.append((area, indices))
        idx += 1
    print(len(christmas_trees))
    return presents, christmas_trees

# Read the data
presents, trees = parse_data_file('data.txt')

# Example: print first present (if available)
if 0 in presents:
    print(f"Present 0: {presents[0]}")
else:
    print("Present 0 not found in input.")

print(f"Christmas trees: {trees}")

present_areas = [7,7,7,7,6,6]
presents_areas = [9,9,9,9,9,9]
present_fits = 0

for area, indices in trees:
    print(f"Area {area} has presents: {indices}")
    width, height = map(int, area.split('x'))
    print(f"  Width: {width}, Height: {height}")
    area_size = width * height
    print(f"  Area size: {area_size}")

    present_sizes = 0 
    for i, index in enumerate(indices):
        present_sizes += present_areas[i]*index

    print(f"  Total present sizes: {present_sizes}")

    if present_sizes <= area_size:
        print("  Presents fit in the area.")
        present_fits += 1

print(f"Number of areas where presents fit: {present_fits}")
print(len(trees))