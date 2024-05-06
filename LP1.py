def bfs(graph, initial):
    visited = []
    queue = [initial]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    
    return visited

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

print(bfs(graph, 'A'))



def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)

    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)
    
    return visited

graph = {
    '0': ['1', '2', '3'],
    '1': ['0'],
    '2': ['0', '4'],
    '3': ['0'],
    '4': ['2']
}

dfs(graph, '0')
