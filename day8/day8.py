from pathlib import Path
import re
import itertools as it

# /home/dubois/Documents/AdventOfCode2025/day8/day8.py

data_file = Path(__file__).with_name("dataExemple.txt")

list_boxes = []
with data_file.open("r", encoding="utf-8") as f:
    for lineno, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        parts = [p for p in re.split(r"[,\s]+", line) if p]
        if len(parts) != 3:
            raise ValueError(f"{data_file}: line {lineno}: expected 3 numbers, got {len(parts)}: {line}")
        idx = len(list_boxes)+1
        list_boxes.append((idx,) + tuple(int(p) for p in parts))
        

list_distances = []
for i, j in it.combinations(list_boxes, 2):
    dist = sum((a - b) ** 2 for a, b in zip(i[1:], j[1:])) ** 0.5
    list_distances.append((i[0], j[0], dist))
    
list_distances.sort(key=lambda t: t[-1])


list_connections = []
i=0
while i < 10 :
    connection_to_add = list_distances[i]
    print(connection_to_add)
    if len(list_connections) == 0 :
        list_connections.append(list(connection_to_add))
        print("Added, directly")
    else : 
        box1_in_connections = any(connection_to_add[0] in conn[:2] for conn in list_connections)
        box2_in_connections = any(connection_to_add[1] in conn[:2] for conn in list_connections)
        print(box1_in_connections, box2_in_connections)
        if box1_in_connections :
            idx_existing = next(i for i, conn in enumerate(list_connections) if connection_to_add[0] in conn[:2])
            print("Found box1 in list_connections at index", idx_existing)
            list_connections[idx_existing].append(connection_to_add)
        elif box2_in_connections :
            idx_existing = next(i for i, conn in enumerate(list_connections) if connection_to_add[1] in conn[:2])
            print("Found box2 in list_connections at index", idx_existing)
            list_connections[idx_existing].append(connection_to_add)
        elif not box1_in_connections and not box2_in_connections :
            list_connections.append(list(connection_to_add))
            print("Added, new connection")
            

    i +=1
    
print("End")
print(list_connections)
    