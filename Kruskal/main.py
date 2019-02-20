def kruskal(graph):
    assert type(graph)==dict

    nodes = graph.keys()
    visited = set()
    path = []
    next = None

    while len(visited) < len(nodes):
        distance = float('inf')
        for s in nodes:
            for d in nodes:
                if s in visited and d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d

        path.append((pre, next))
        visited.add(pre)
        visited.add(next)

    return path


if __name__ == '__main__':        
    graph_dict = {  "1":{"1": 0, "2": 2, "3": 1, "4": 4, "5": 3},
                    "2":{"1": 1, "2": 0, "3": 4, "4": 2, "5": 2},
                    "3":{"1": 2, "2": 1, "3": 0, "4": 1, "5": 4},
                    "4":{"1": 3, "2": 5, "3": 2, "4": 0, "5": 1},
                    "5":{"1": 3, "2": 5, "3": 2, "4": 4, "5": 0},
    }

    path = kruskal(graph_dict)
    print path
