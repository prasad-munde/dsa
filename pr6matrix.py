from collections import deque

# Graph representing landmarks and their connections
landmarks_map = {
    'ICEM Main Gate': ['Avirat Open Parking'],
    'Avirat Open Parking': ['ICEM Main Gate', 'Maggie Point', 'Xerox Shop'],
    'Maggie Point': ['Avirat Open Parking', 'Xerox Shop'],
    'Xerox Shop': ['Maggie Point', 'Avirat Open Parking', 'Workshop'],
    'Workshop': ['Xerox Shop', 'Avirat Open Parking']
}

# BFS to find the shortest path between two landmarks
def bfs_shortest_path(graph, start, goal):
    # Queue for BFS (holds the current path)
    queue = deque([[start]])

    # Set of visited landmarks
    visited = set()

    while queue:
        path = queue.popleft()  # Get the current path
        landmark = path[-1]  # The last landmark in the path

        # If this landmark is the goal, return the path
        if landmark == goal:
            return path

        # If the landmark hasn't been visited
        if landmark not in visited:
            visited.add(landmark)
            # Add the neighboring landmarks to the queue with the current path
            for neighbor in graph.get(landmark, []):  # Use .get() to avoid KeyError
                if neighbor not in visited:  # Ensure we don't revisit landmarks
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    # If there's no path
    return None

# Example: Find the shortest path from ICEM Main Gate to Workshop
start_landmark = 'ICEM Main Gate'
end_landmark = 'Workshop'
shortest_path = bfs_shortest_path(landmarks_map, start_landmark, end_landmark)

if shortest_path:
    print(f"The shortest path from {start_landmark} to {end_landmark} is: {shortest_path}")
else:
    print(f"No path exists from {start_landmark} to {end_landmark}")


# DFS to find all paths between two landmarks
def dfs_all_paths(graph, start, goal, path=[]):
    path.append(start)

    # If we reached the destination, return the current path
    if start == goal:
        return [list(path)]

    # If there are no further paths, return an empty list
    if start not in graph:
        return []

    paths = []
    # Visit all the neighbors and explore further
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_paths = dfs_all_paths(graph, neighbor, goal, path)
            for p in new_paths:
                paths.append(p)

    # Backtrack: Remove the current node from the path before returning
    path.pop()
    return paths


# Example: Find all paths from ICEM Main Gate to Workshop
all_paths = dfs_all_paths(landmarks_map, 'ICEM Main Gate', 'Workshop')

print(f"All possible paths from ICEM Main Gate to Workshop are: {all_paths}")
