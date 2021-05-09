# undirected graph using adjacency matrix

from collections import deque

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return 
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False

    def __dfsHelper(self, sv, visited):
        print(sv, end=" ")
        visited[sv] = True
        for i in range(self.nVertices):
            if (self.adjMatrix[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self, sv, visited):
        queue = deque()
        queue.append(sv)
        visited[sv] = True
        while queue:
            currentVertex = queue.popleft()
            for i in range(self.nVertices):
                if self.adjMatrix[currentVertex][i] > 0 and visited[i] is False:
                    queue.append(i)
                    visited[i] = True
            print(currentVertex, end=" ")

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)

    def hasPath(self, v1, v2):
        if v1 == v2 and self.adjMatrix[v1][v2] != 1:
            return "Both vertices are same and there is no self loop"
        if v1 == v2 and self.adjMatrix[v1][v2] == 1:
            return "Both vertices are same and there is a self loop"
        queue = deque()
        visited = [False for i in range(self.nVertices)]
        queue.append(v1)
        visited[v1] = True
        while queue:
            currentVertex = queue.popleft()
            if currentVertex == v2:
                return True
            for i in range(self.nVertices):
                if self.adjMatrix[currentVertex][i] == 1 and visited[i] is False:
                    queue.append(i)
                    visited[i] = True
        return False

    def __printAllPathsHelper(self, v1, v2, visited, path):
        path.append(v1)
        visited[v1] = True
        if v1 == v2:
            print(path)
        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                self.__printAllPathsHelper(i, v2, visited, path)
        path.pop()
        visited[v1] = False

    def printAllPaths(self, v1, v2):
        if v1 == v2 and self.adjMatrix[v1][v2] == 1:
            print("v1 and v2 are same and there is a self loop")
            return
        elif v1 == v2 and self.adjMatrix[v1][v2] == 0:
            print("v1 and v2 are same and there is no self loop")
            return
        path = []
        visited = [False for i in range(self.nVertices)]
        self.__printAllPathsHelper(v1, v2, visited, path)

    def __str__(self):
        return str(self.adjMatrix)

graph = Graph(6)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(3, 5)
graph.addEdge(2, 4)
graph.addEdge(4, 5)

graph.dfs()

print("\n")

graph.bfs()

print("\n")

print(graph.hasPath(2, 2))

print("\n")

graph.addEdge(2, 2)
print(graph.hasPath(2,2))

print("\n")

graph.printAllPaths(0,5)
