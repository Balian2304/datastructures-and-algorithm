class Graph():
    def __init__(self,nodes):
        self.nodes = nodes
        self.list = []
        for i in range(nodes):
            self.list.append([])
    def createedge(self,v1,v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)
    def bfs(self,sourcenode):
        self.visited = [False] * self.nodes
        result = []
        queue = []
        queue.append(sourcenode)
        self.visited[sourcenode] = True
        while len(queue) > 0:
            s = queue.pop(0)
            result.append(s)
            for node in self.list[sourcenode]:
                if self.visited[node] == False:
                    queue.append(node)
                    self.visited[node] = True
        return result

graph1 = Graph(4)
graph1.createedge(0,1)
graph1.createedge(1,2)
graph1.createedge(1,3)
graph1.createedge(0,2)
graphresult = graph1.bfs(0)
print(graphresult)




