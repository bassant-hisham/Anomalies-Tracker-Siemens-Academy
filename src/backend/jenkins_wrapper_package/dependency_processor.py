from collections import defaultdict, deque

from src.common.exception import CircularDependencyException
def topological_sort_in_batches(graph:dict, batch_size:int):
    """
    topological sort on a directed acyclic graph in batches, where each batch contains a specified number of nodes that can be run in parallel.
    
    :param graph: dictionary that represents the dependencies between nodes.
    Each key in the dictionary represents a node, and the corresponding value is a list of nodes that
    the key node depends on.
    :param batch_size: maximum number of nodes that can be processed in each batch. 
    :return: list of lists. Each inner list represents a batch of nodes that can be processed in parallel,
    according to the topological sorting order.
    """

    def invert_dependency(graph_dict):
        inverted_graph = {node: [] for node in graph_dict.keys()}

        for node, dependencies in graph_dict.items():
            for dependency in dependencies:
                inverted_graph[dependency].append(node)

        return inverted_graph
    
    graph = invert_dependency(graph)

    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque()
    result = []

    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        batch = []
        for _ in range(min(len(queue), batch_size)):
            node = queue.popleft()
            batch.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        result.append(batch)
    flattened_array = [element for row in result for element in row]
    if len(flattened_array) != len(graph):
        raise CircularDependencyException 

    return result

graph = {
    "1": ["2"],
    "2": [1],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": []
}
# [['5','6','7'],['2','3','4'],['1']]


All_Jobs_Status = {
    "1": "True",
    "2": "True",
    "3": "",
    "4": "",
    "5": "FAILURE",
    "6": "",
    "7": ""
}

# graph = {
#     'Ethernet-1-1': ['Ethernet-1-2'],
#     'Ethernet-1-2': ['Ethernet-1-3'],
#     'Ethernet-1-3': [],
# }

# result = topological_sort_in_batches(graph, batch_size=10)
# print("Batched Topological Sort:", result)



# def is_dependency_failed(job):
#     for dependency in graph[job]:
#         if dependency in All_Jobs_Status and All_Jobs_Status[dependency] == "FAILURE":
#             return False
#     return True


#print(is_dependency_failed("6"))


