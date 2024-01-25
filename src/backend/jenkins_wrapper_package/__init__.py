# Correcting and re-running the topological sort function
from collections import deque


def topological_sort(dependencies):
    # Create a dictionary to keep track of the in-degree of each node
    in_degree = {u: 0 for u in dependencies}
    for u in dependencies:
        for v in dependencies[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1

    # Queue for all nodes with in-degree 0
    queue = deque([u for u in in_degree if in_degree[u] == 0])

    sorted_order = []

    while queue:
        u = queue.popleft()
        sorted_order.append(u)
        for v in dependencies.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Check if there was a cycle in the graph
    if len(sorted_order) == len(in_degree):
        return sorted_order[::-1]  # Reverse the list before returning
    else:
        raise Exception("A cycle was detected in the dependencies , please check")

dependencies = {
    'Ethernet-1-1': ['Ethernet-1-2'],
    'Ethernet-1-2': ['Ethernet-1-3'],
    'Ethernet-1-3': [],
}

try:
    corrected_order = topological_sort(dependencies)
    print(corrected_order)
except Exception as e:
    print(str(e))

