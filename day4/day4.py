import numpy as np
from pathlib import Path

# roll available if < 4 rolls in the 8 adjacent positions


def load_char_grid(path: str | Path | None = None) -> np.ndarray:
    if path is None:
        path = Path(__file__).parent / "data.txt"
    else:
        path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        rows = [list(line.rstrip("\n")) for line in f]
    if not rows:
        return np.empty((0, 0), dtype="U1")
    max_cols = max(len(r) for r in rows)
    grid = np.full((len(rows), max_cols), " ", dtype="U1")
    for i, r in enumerate(rows):
        grid[i, : len(r)] = r
    return grid

roll_grid = load_char_grid()
print(roll_grid.shape)

###### Part 1 #####

n_rolls = 0
for i in range(roll_grid.shape[0]):
    for j in range(roll_grid.shape[1]):
        print(f"Cell ({i}, {j}): '{roll_grid[i, j]}'")
        if roll_grid[i, j] == "@":
            n_adjacent = 0
            for id_x in np.arange(-1, 2):
                for id_y in np.arange(-1, 2):
                    if id_x == 0 and id_y == 0:
                        continue
                    ni, nj = i + id_x, j + id_y                
                    
                    if 0 <= ni < roll_grid.shape[0] and 0 <= nj < roll_grid.shape[1]:
                        print(f"  Adjacent ({ni}, {nj}): '{roll_grid[ni, nj]}'")
                        if roll_grid[ni, nj] == "@":
                            n_adjacent +=1

            if n_adjacent < 4:
                print(f"  --> Cell ({i}, {j}) has less than 4 adjacent '@' characters, roll is available.")
                n_rolls += 1

print(f"Total available rolls: {n_rolls}")


###### Part 2 #####n_rolls = 0
n_rolls_total = 0
n_removed = 1
while n_removed != 0:
    n_removed = 0
    for i in range(roll_grid.shape[0]):
        for j in range(roll_grid.shape[1]):
            print(f"Cell ({i}, {j}): '{roll_grid[i, j]}'")
            if roll_grid[i, j] == "@":
                n_adjacent = 0
                for id_x in np.arange(-1, 2):
                    for id_y in np.arange(-1, 2):
                        if id_x == 0 and id_y == 0:
                            continue
                        ni, nj = i + id_x, j + id_y                
                        
                        if 0 <= ni < roll_grid.shape[0] and 0 <= nj < roll_grid.shape[1]:
                            print(f"  Adjacent ({ni}, {nj}): '{roll_grid[ni, nj]}'")
                            if roll_grid[ni, nj] == "@":
                                n_adjacent +=1

                if n_adjacent < 4:
                    print(f"  --> Cell ({i}, {j}) has less than 4 adjacent '@' characters, roll is available.")
                    n_rolls_total += 1
                    n_removed += 1
                    roll_grid[i, j] = "."

print(f"Total available rolls: {n_rolls_total}")