class Graph:
    def __init__(self,vno): #vno is no. of vertices
        self.vertex_count=vno
        self.adj_matrix = [ [0]*vno for e in range(vno)]

    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid vertex ")

    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("Invalid vetex")

    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid vertex")
            return False

    def print_graph(self):
      for row_list in self.adj_matrix:
         print(" ".join(map(str,row_list)))
         # map contains two arguments fuction and iterable
         # map fuctions converts every element in iterable in str one by one return string list
         #know join method takes list of string and join them in one string using " " object

    def BFS(self, s):
        from Queue_using_list import Queue
        Q = Queue()
        Q.enqueue(s)
        visited = [False] * self.vertex_count
        visited[s] = True
        bfs_traversal_output = []

        while not Q.is_empty():
            n = Q.get_front()
            Q.dequeue()
            bfs_traversal_output.append(n)

            for u in range(self.vertex_count):
                if self.adj_matrix[n][u] != 0 and not visited[u]:
                    Q.enqueue(u)
                    visited[u] = True
            # Handling disconnected Graph
            for i in range(self.vertex_count):
             if not  visited[i]:
                Q.enqueue(i)
                visited[i]=True


        print("Result of BFS is:", bfs_traversal_output)

    def DFS(self,s):
        from stack_using_list import stack
        S = stack()
        S.push(s)
        visited = [False]*self.vertex_count
        visited[s]=True
        dfs_result_output = []
        while not S.is_empty():
            n = S.peek()
            m = S.pop()
            dfs_result_output.append(n)
            for u in range(self.vertex_count):
                if self.adj_matrix[n][u]!=0 and not visited[u]:
                    S.push(u)
                    visited[u] = True
            # traversing disconnected node but it may disturb the sequence
            # Ensure to make second loop within while loop as well
            for i in range(self.vertex_count):
                if not visited[i]:
                 S.push(i)
                 visited[i]=True
        print("Result of DFS is :", dfs_result_output)



g = Graph(5)
g.add_edge(0,1)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,0)
g.add_edge(2,3)
result = g.has_edge(2,3)
print("The given vertices has_edge = ",(result))
g.print_graph()
g.BFS(0)
g.DFS(0)