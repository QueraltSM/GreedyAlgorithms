def prim(graph, root):
    assert type(graph)==dict

    nodes = graph.keys()
    nodes.remove(root)

    visited = [root]
    path = []
    next = None

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
        visited.append(next)
        nodes.remove(next)

    return path


if __name__ == '__main__':
    graph_dict = {  "1":{"2": 2, "3": 1},
                    "2":{"1": 2, "4":4,"5":3},
                    "3":{"1": 1, "5":1},
                    "4":{"2": 4},
                    "5":{"2": 3, "3":1},
    }

    path = prim(graph_dict, '1')
    print path