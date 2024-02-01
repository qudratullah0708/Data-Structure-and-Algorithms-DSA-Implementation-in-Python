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

    def DFS(self, s):
        #Using recursive approch instead of a stack for backtracking in DFS
        visited = [False] * self.vertex_count
        dfs_traversal_output = []

        def dfs_util(node):
            visited[node] = True
            dfs_traversal_output.append(node)

            for u in range(self.vertex_count):
                if self.adj_matrix[node][u] != 0 and not visited[u]:
                    dfs_util(u)

        for i in range(self.vertex_count):
            if not visited[i]:
                dfs_util(i)

        print("Result of DFS is:", dfs_traversal_output)


g = Graph(5)
g.add_edge(0,1)
g.add_edge(3,4)
g.add_edge(4,2)
g.add_edge(2,0)
g.add_edge(2,3)
result = g.has_edge(2,3)
print("The given vertices has_edge = ",(result))
g.print_graph()
g.DFS(0)