def build_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            node, neighbors = line.split(':')
            node = node.strip()
            neighbors = [n.strip() for n in neighbors.split(' ') if n.strip()]
            graph[node] = neighbors
    return graph

# Read the file and build the graph
graph = build_graph('data.txt')

print(graph)

path_count = 0


def count_paths(graph, current_node, target_node, visited=None,  ):
    global path_count
    print('Current Node : ', current_node)
    if visited is None:
        visited = set()
    if current_node == target_node:
        print('Target reached! +1 path found.')
        path_count += 1
        return
    visited.add(current_node)
    print(visited)
    for neighbor in graph.get(current_node, []):
        print('Neighbors : ', neighbor)
        if neighbor not in visited:
            count_paths(graph, neighbor, target_node, visited, )
    visited.remove(current_node)
    return 


# Start from 'you'
start_node = 'you'
# Count the number of paths from 'you' to 'out'
target_node = 'out'
path_count = 0
num_paths = count_paths(graph, start_node, target_node, visited=None)
print(f"Number of paths from '{start_node}' to '{target_node}': {path_count}")