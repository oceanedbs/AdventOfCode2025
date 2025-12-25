from pathlib import Path
import re
import itertools as it

# /home/dubois/Documents/AdventOfCode2025/day8/day8.py

data_file = Path(__file__).with_name("data.txt")

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

box1_in_connections = -1
box2_in_connections = -1
list_connections = []
i=0
# while i < 1000 :
#     connection_to_add = list_distances[i]
#     print(connection_to_add)
#     if len(list_connections) == 0 :
#         list_connections.append(list(connection_to_add[:2]))
#         print("Added, directly")
#     else : 
#         for idx, conn in enumerate(list_connections) :
#             print(" List of existing connections : ", list(conn))
#             print(" Checking connection to add : ", connection_to_add)
#             if connection_to_add[0] in conn:
#                 box1_in_connections = idx   
#             if connection_to_add[1] in conn:
#                 box2_in_connections = idx
#         # box1_in_connections = any(connection_to_add[0] in conn[:2] for conn in list_connections)
#         # box2_in_connections = any(connection_to_add[1] in conn[:2] for conn in list_connections)
#         print(box1_in_connections, box2_in_connections)
#         if box1_in_connections==box2_in_connections and box1_in_connections != -1 :
#             print("Both boxes already in connections, skipping")
#         elif box1_in_connections != -1 and box2_in_connections != -1 and box1_in_connections != box2_in_connections :
#             print("Merging connections at index", box1_in_connections, "and", box2_in_connections)
#             list_connections[box1_in_connections].extend(list_connections[box2_in_connections])
#             del list_connections[box2_in_connections]
#             print("After merging + deletion:", list_connections)
#         elif box1_in_connections != -1 :
#             print("Found box1 in list_connections at index", box1_in_connections)
#             list_connections[box1_in_connections].append(connection_to_add[1])
#             print(list_connections)
#         elif box2_in_connections != -1 :
#             print("Found box2 in list_connections at index", box2_in_connections)
#             list_connections[box2_in_connections].append(connection_to_add[0])
#             print(list_connections)
#         elif box1_in_connections == -1 and box2_in_connections == -1 :
#             list_connections.append(list(connection_to_add[:2]))
#             print("Added, new connection")
#             print(list_connections)
        
        
#         box1_in_connections = -1
#         box2_in_connections = -1

#     i +=1
    
# print("End")
# print(list_connections)
# list_connections.sort(key=len, reverse=True)
# print(list_connections)

# total = 1
# for conn in list_connections[:3] :
#     print("Length of connection :", len(conn))
#     total *= len(conn)

# print("Total :", total)


##### PART 2 #####

# Run until there is only one connection

box1_in_connections = -1
box2_in_connections = -1
# add first connection
list_connections = []
list_connections.append(list(list_distances[0][:2]))
i=1
last_connection_added = list_distances[0]
while len(list_connections[0])< len(list_boxes) :
    connection_to_add = list_distances[i]
    print(connection_to_add)
    print("Current connections :", list_connections)
    for idx, conn in enumerate(list_connections) :
        if connection_to_add[0] in conn:
            box1_in_connections = idx   
        if connection_to_add[1] in conn:
            box2_in_connections = idx
    # box1_in_connections = any(connection_to_add[0] in conn[:2] for conn in list_connections)
    # box2_in_connections = any(connection_to_add[1] in conn[:2] for conn in list_connections)
    print(box1_in_connections, box2_in_connections)
    if box1_in_connections==box2_in_connections and box1_in_connections != -1 :
        print("Both boxes already in connections, skipping")
    elif box1_in_connections != -1 and box2_in_connections != -1 and box1_in_connections != box2_in_connections :
        print("Merging connections at index", box1_in_connections, "and", box2_in_connections)
        list_connections[box1_in_connections].extend(list_connections[box2_in_connections])
        del list_connections[box2_in_connections]
        print("After merging + deletion:", list_connections)
        last_connection_added = connection_to_add
    elif box1_in_connections != -1 :
        print("Found box1 in list_connections at index", box1_in_connections)
        list_connections[box1_in_connections].append(connection_to_add[1])
        print(list_connections)
        last_connection_added = connection_to_add
    elif box2_in_connections != -1 :
        print("Found box2 in list_connections at index", box2_in_connections)
        list_connections[box2_in_connections].append(connection_to_add[0])
        print(list_connections)
        last_connection_added = connection_to_add
    elif box1_in_connections == -1 and box2_in_connections == -1 :
        list_connections.append(list(connection_to_add[:2]))
        print("Added, new connection")
        print(list_connections)
        last_connection_added = connection_to_add
    
        
    box1_in_connections = -1
    box2_in_connections = -1

    i +=1
print(last_connection_added)
print(list_boxes[last_connection_added[0]-1])
print(list_boxes[last_connection_added[1]-1])
result = list_boxes[last_connection_added[0]-1][1] * list_boxes[last_connection_added[1]-1][1]
print("Result :", result)