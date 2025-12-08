from pathlib import Path
from typing import Set, Tuple, Optional
from collections import deque

# /home/dubois/Documents/AdventOfCode2025/day7/day7.py

Coord = Tuple[int, int]

def read_grid(path: str = "dataExemple.txt"):
    p = Path(path)
    lines = [line.rstrip("\n") for line in p.open(encoding="utf-8")]
    grid = []
    for line in lines:
        # support both space-separated tokens and compact rows
        if " " in line:
            tokens = line.split()
        else:
            tokens = list(line)
        grid.append(tokens)
    n_rows = len(grid)
    n_cols = len(grid[0]) if n_rows > 0 else 0
    return grid, n_rows, n_cols

def find_symbols(grid) -> Tuple[Set[Coord], Optional[Coord]]:
    carets: Set[Coord] = set()
    start_coord: Optional[Coord] = None
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "^":
                carets.add((r, c))
            elif ch == "S" and start_coord is None:
                start_coord = (r, c)
    return carets, start_coord

def print_grid(token_set, caret_coords, start, n_row, n_col):
        """
        Print a grid of size n_row x n_col.
        Tokens override start and carets when they overlap.
        """
        # initialize grid with dots
        grid = [["." for _ in range(n_col)] for _ in range(n_row)]

        # place carets
        for r, c in caret_coords or set():
            if 0 <= r < n_row and 0 <= c < n_col:
                grid[r][c] = "^"

        # place start (if any)
        if start is not None:
            r, c = start
            if 0 <= r < n_row and 0 <= c < n_col:
                grid[r][c] = "S"

        # place tokens (override other symbols)
        for r, c in token_set or set():
            if 0 <= r < n_row and 0 <= c < n_col:
                grid[r][c] = "|"

        # print rows
        for row in grid:
            print("".join(row))

def simulate(token_new_pos, caret_coords, start, n_rows, n_cols, i, n_timeline):
    print("simulate")
    print(n_timeline)
    if i < n_rows - 1:
        matches  = {p for p in caret_coords if p[0] == i}
        print(matches)
        if not matches : 
            print('No matches')
            simulate((token_new_pos[0] + 1, token_new_pos[1]), caret_coords, start, n_rows, n_cols, i + 1, n_timeline+1)
        if matches :
            for x, y in matches:
                n_timeline = simulate((x, y-1), caret_coords, start, n_rows, n_cols, i + 1, n_timeline+1)
                n_timeline = simulate((x, y+1), caret_coords, start, n_rows, n_cols, i + 1, n_timeline+1)

    return n_timeline


if __name__ == "__main__":
    grid, n_rows, n_cols = read_grid("dataExemple.txt")
    caret_coords, start = find_symbols(grid)
    print("caret_coords (set of (row,col)):", caret_coords)
    print("start_coord (first S found)         :", start)
    print("Number of rows in grid               :", n_rows)
    
    n_split = 0

    token_set = set()
    if start is not None:
        token_set.add((start[0] + 1, start[1]))
    # caret_coords was populated by find_symbols(); do not reset it here.
    i = 1
    while i < n_rows - 1:
        print(i)
        matches  = {p for p in caret_coords if p[0] == i}
        print(matches)
        if not matches : 
            last_added_tokens = {p for p in token_set if p[0] == i - 1}
            for last_added_token in last_added_tokens:
                token_set.add((i, last_added_token[1]))
                print(f"Added token at {(i, last_added_token[1])} based on last added token {last_added_token}")
        if matches :
            for x, y in matches:
                if (x - 1, y) in token_set:
                    token_set.add((x, y - 1))
                    token_set.add((x, y + 1))
                    n_split += 1
            
            token_list_not_in_matches = token_set - matches
            for token in token_list_not_in_matches:
                if token[0] == i - 1 and (i, token[1]) not in caret_coords:
                    token_set.add((i, token[1]))
                    print(f"Added token at {(i, token[1])} based on last added token {token}")
        print('Number of splits so far:', n_split)
        print_grid(token_set, caret_coords, start, n_rows, n_cols)
        
        i += 1
        # try:
        #     input("Press Enter to continue...")
        # except (KeyboardInterrupt, EOFError):
        #     print("\nInterrupted. Exiting loop.")
        #     break
        
    print("Final token positions:", token_set)
    print(f"Number of splits encountered: {n_split}")
    

        
#### Part 2 #########

def build_caret_graph(token_set, caret_coords, n_rows, n_cols):
    """
    Build a directed graph where each caret is a node.
    There is an edge A -> B if there exists a path of tokens (orthogonal moves)
    from any of the source positions relative to A:
        - left cell of A: (rA, cA-1)
        - right cell of A: (rA, cA+1)
        - the caret cell A itself (previous caret)
    to the cell just before B: (rB, cB-1).
    A path may walk over token cells and caret cells.
    Only downward connections (rB > rA) are considered.
    """
    tokens = set(token_set)
    carets = list(caret_coords)
    caret_set = set(caret_coords)
    graph = {c: set() for c in carets}

    def in_bounds(p):
        r, c = p
        return 0 <= r < n_rows and 0 <= c < n_cols

    # 4-neighbor moves
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for A in carets:
        rA, cA = A
        # possible starting positions (must be either a token or a caret)
        candidate_sources = [(rA, cA - 1), (rA, cA + 1), (rA, cA)]
        valid_sources = [s for s in candidate_sources if in_bounds(s) and (s in tokens or s in caret_set)]
        if not valid_sources:
            continue

        for B in carets:
            if A == B:
                continue
            rB, cB = B
            # consider only downward edges (optional: remove this check to allow all directions)
            if rB <= rA:
                continue

            target = (rB, cB - 1)
            # the specification requires a token "to the cell just before the other caret",
            # so require the target to be a token position.
            if not in_bounds(target) or target not in tokens:
                continue

            # BFS from all valid_sources searching for target
            q = deque()
            visited = set()
            for s in valid_sources:
                q.append(s)
                visited.add(s)

            found = False
            while q and not found:
                cur = q.popleft()
                if cur == target:
                    found = True
                    break
                for dr, dc in neighbors:
                    nb = (cur[0] + dr, cur[1] + dc)
                    if not in_bounds(nb) or nb in visited:
                        continue
                    # can walk over tokens and carets
                    if nb in tokens or nb in caret_set:
                        visited.add(nb)
                        q.append(nb)

            if found:
                graph[A].add(B)

    return graph

# build and display the graph for the current grid
caret_graph = build_caret_graph(token_set, caret_coords, n_rows, n_cols)

print("\nCaret graph adjacency (A -> [B,...]):")
for src, nbrs in caret_graph.items():
    print(f"{src} -> {sorted(nbrs)}")

    