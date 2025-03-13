def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
