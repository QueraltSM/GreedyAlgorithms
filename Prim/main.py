def prim(graph, root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)

    visited = [root]
    path = []
    next = None
    cost = 0

    while nodes:
        distance = float('inf')
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        cost += distance
        visited.append(next)
        nodes.remove(next)

    print "Path = ",path
    print "Minimum cost = ",cost


if __name__ == '__main__':
    graph_dict = {  "1":{"1": 0, "2": 8, "3": 4, "4": 2, "5": 9},
                    "2":{"1": 8, "2": 0, "3": 6, "4": 6, "5": 5},
                    "3":{"1": 4, "2": 6, "3": 0, "4": 4, "5": 1},
                    "4":{"1": 2, "2": 6, "3": 4, "4": 0, "5": 3},
                    "5":{"1": 9, "2": 5, "3": 1, "4": 3, "5": 0},
    }

    prim(graph_dict, '1')
