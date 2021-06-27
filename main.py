import json

class Graph:
    def __init__(self, vCount) -> None:
        self.data = [[] for _ in range(vCount)]
        self.v = vCount

    def addUndirectedEdge(self, v1, v2):
        self.addDirectedEdge(v1, v2)
        self.addDirectedEdge(v2, v1)

    def addDirectedEdge(self, source, target):
        self.data[source].append(target)

    def adj(self, v):
        return self.data[v]

    def __str__(self) -> str:
        return str(self.data)

class Route:
    def __init__(self) -> None:
        self._route = []

    def add(self, v):
        self._route.append(str(v))

    def __str__(self) -> str:
        return " -> ".join(self._route) if len(self._route) > 0 else "EMPTY"


def BFS(graph: Graph, start, dfs_i = False):
    route = Route()
    queueOrStack = [start]
    result = [{'color': 'white', 'distFromStart': -1, 'cameFrom': None}
              for _ in range(graph.v)]
    result[start]['color'] = 'gray'
    result[start]['distFromStart'] = 0
    while len(queueOrStack) > 0:
        currNode = queueOrStack.pop(-1 if dfs_i else 0)
        route.add(currNode)
        print(f"In node {currNode} -> {result[currNode]}")
        for adjNode in graph.adj(currNode):
            if result[adjNode]['color'] == 'white':
                queueOrStack.append(adjNode)
                result[adjNode]['color'] = 'gray'
                result[adjNode]['distFromStart'] = result[currNode]['distFromStart'] + 1
                result[adjNode]['cameFrom'] = currNode
                print(
                    f"Added node {adjNode} for processing -> {result[adjNode]}")
        result[currNode]['color'] = 'black'
        print(f"Finished work in node {currNode} -> {result[currNode]}")
    return [{i: r} for i, r in enumerate(result)], route


def DFS_r(graph: Graph, start):
    route = Route()
    t = 0
    res = [{'color': 'white', 'distFromStart': -1, 'cameFrom': None}
           for _ in range(graph.v)]
    _DFS_r(graph, start, t, res, route)
    return [{i: r} for i, r in enumerate(res)], route


def _DFS_r(graph: Graph, v, time, result, route: Route):
    route.add(v)
    result[v]['distFromStart'] = time
    result[v]['color'] = 'gray'
    print(f"In node {v} -> {result[v]}")
    for adjNode in graph.adj(v):
        if result[adjNode]['color'] == 'white':
            result[adjNode]['cameFrom'] = v
            _DFS_r(graph, adjNode, time + 1, result, route)
    result[v]['color'] = 'black'
    result[v]['f'] = time
    print(f"Finished work in node {v} -> {result[v]}")


if __name__ == '__main__':
    graph = Graph(5)
    graph.addDirectedEdge(0, 1)
    graph.addDirectedEdge(0, 2)
    graph.addDirectedEdge(1, 3)
    graph.addDirectedEdge(2, 4)
    graph.addDirectedEdge(2, 1)
    graph.addDirectedEdge(0, 3)

    print(">>>>>>>>>>>>> BFS")
    resBFS, routeBFS = BFS(graph, 0)
    print(json.dumps(resBFS, indent=2))
    print(">>>>>>>>>>>>> BFS")
    
    print(">>>>>>>>>>>>> DFS (recursive)")
    resDFS_r, routeDFS_r = DFS_r(graph, 0)
    print(json.dumps(resDFS_r, indent=2))
    print(">>>>>>>>>>>>> DFS (recursive)")

    print(">>>>>>>>>>>>> DFS (iterative)")
    resDFS_i, routeDFS_i = BFS(graph, 0, True)
    print(json.dumps(resDFS_i, indent=2))
    print(">>>>>>>>>>>>> DFS (iterative)")

    print("\nROUTES:\n")
    print(f"ROUTE BFS  : {routeBFS}")
    print(f"ROUTE DFS R: {routeDFS_r}")
    print(f"ROUTE DFS I: {routeDFS_i}")
