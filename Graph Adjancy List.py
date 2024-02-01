class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            #The line self.adj_list[u].append((v, weight)) is appending
            # a tuple (v, weight) to the list associated with the key u in the adj_list dictionary.
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid vertex")
            return False

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            #self.adj_list[u]: Accesses the list associated with the vertex u in the adjacency list dictionary.
            # This is a list comprehension that iterates through each tuple (vertex, weight) in the current adjacency list of vertex u.
            # It creates a new list that includes only those tuples where the vertex is not equal to v.
            #Assigns the newly created list to the adjacency list of vertex u, effectively updating the adjacency list by removing the edge that connects to vertex v.
           self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list[u] if vertex !=v ]
           self.adj_list[v]=[(vertex,weight) for vertex, weight in self.adj_list[v] if vertex !=u]
        else:
            print("Invalid vertices")

    def has_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex ==v for vertex,weight in self.adj_list[u] )
        else:
            print("Invalid vertices")
            return False

    def print_adj_list(self):
        for (vertex,n) in self.adj_list.items():
            print("V",vertex,":",n)

    def BFS(self,s):
        from Queue_using_list import Queue
        Q = Queue()
        Q.enqueue(s)
        visited = [False]*self.vertex_count
        visited[s] = True
        bfs_traversal_output = []
        while not Q.is_empty():
            n = Q.get_front()
            Q.dequeue() #dequeing first entered element
            bfs_traversal_output.append(n)
            for (u,v) in self.adj_list[n]:
                if not visited[u]:
                 Q.enqueue(u)
                 visited[u] =True

        print("The result of a BFS is: ",bfs_traversal_output)


    def DFS(self,s):
        from stack_using_list import stack
        S = stack()
        S.push(s)
        visited = [False]*self.vertex_count
        visited[s] = True
        dfs_traversal_output = []
        while not S.is_empty():
            n = S.peek()
            m = S.pop()
            dfs_traversal_output.append(n)
            for (u,v) in self.adj_list[n]:
                if not visited[u]:
                    S.push(u)
                    visited[u]=True
        print("The result of DFS is ",dfs_traversal_output)



g = Graph(5)
g.add_edge(0,1)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.print_adj_list()
print("Has_edge = ",g.has_edge(1,3))

g.BFS(0) #passing source node as argument
g.DFS(0)


