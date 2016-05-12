def dfs(graph, start, destination, path=None):
    if path is None:
        path = tuple()
    if start == destination:
        yield path
    neighbours = [connection for connection in graph if connection[0] == start and
                                                        connection[1] not in (vertex[0] for vertex in path)]
    for next in neighbours:
        yield from dfs(graph, next[1], destination, path + (next,))


def print_min_from_pathes(pathes):
    min_weight = -1
    min_path = ""
    for path in pathes:
        weight = 0
        result = path[0][0]
        for connection in path:
            result += " -> %s" % connection[1]
            weight += connection[2]
        if weight < min_weight or min_weight == -1:
            min_weight = weight
            min_path = result
    print(min_path, " = ", min_weight)


def depth_first(graph, start, end):
    pathes = list(dfs(graph, start, end))
    print("Depth first search: ", end="")
    print_min_from_pathes(pathes)


def breadth_first(graph, start, destination):
    queue = [((start, start, 0),)]
    results = []
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        neighbours = [connection for connection in graph if connection[0] == vertex[1] and
                                                            connection[1] not in [vertex[1] for vertex in path]]
        for next in neighbours:
            if next[1] == destination:
                res = list(path + (next,))
                results.append(res[1:])
            else:
                queue.append(path + (next,))
    print("Breadth first search: ", end="")
    print_min_from_pathes(results)


def degree(graph, vertex):
    return len([ver for ver in graph if ver[0] == vertex])


def nodes_list(graph):
    vertexes = set([ver[0] for ver in graph])
    for vertex in sorted(vertexes):
        print(vertex, " - ", degree(graph, vertex))

if __name__ == "__main__":
    # Variant 0 - Arc-clause form
    graph = (
        ('A', 'B', 8),
        ('A', 'C', 7),
        ('B', 'C', 9),
        ('B', 'D', 3),
        ('C', 'A', 5),
        ('C', 'D', 15),
        ('D', 'B', 10),
    )
    depth_first(graph, 'A', 'D')
    breadth_first(graph, 'A', 'D')

    nodes_list(graph)
