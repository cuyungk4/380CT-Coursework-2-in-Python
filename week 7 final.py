class graph:
      def __init__(self,v,e):
            self.v = v
            self.e = e
            self.adjlist = {}
            
      def adj_list(self):
            for a in range(len(self.v)):
                  self.adjlist.update({self.v[a]:self.e[a]})
                        
      def add_vertices(self):
            nv=raw_input("Enter a new node: ")
            self.nv=nv
            if nv in self.v:
                  print " Please enter a NEW node!!!"
                  self.add_vertices()
            else:
                  self.v.append(self.nv)
                  print self.v
            
      def add_edges(self):
            ne = raw_input ("Enter a node link with : ")
            self.ne=ne
            if ne not in self.v:
                  print " Please enter a node in the list!!!"
                  self.add_edges()
            else:
                  self.e.append([self.ne])
                  y=(self.v.index(self.ne))
                  self.e[y].append(self.nv)
                  self.adj_list()

            
      def display(self):
            for n in range (len(self.v)):
                  print "vertex: %s adjacency to %s"%(self.v[n], self.adjlist[self.v[n]])


      def DFS(self,g):
            s=str(raw_input("Enter the start node: "))
            if s not in self.v:
                  print " Please enter a node in the list!!!"
                  self.DFS(G.adjlist)
            else:
                  stack = []
                  result = []
                  stack.append(s)
                  while stack:
                        u=stack.pop()
                        if u not in result:
                              result.append(u)
                              for i in reversed (g[u]) :
                                    stack.append(i)
                  print "The path start from %s is %s."%(s,result)

            
G=graph(["a","b","c","d","e","f","g","h","i","j"],
        [["b","f","g"],
        ["a","d","g","h"],
        ["d","i","j"],
        ["b","c","h","j"],
        ["h","i"],
        ["a","i","j"],
        ["a","b","h"],
        ["b","e"],
        ["c","e","f"],
        ["d","c","f"]])
G.adj_list()
G.display()
G.add_vertices()
G.add_edges()
G.display()
G.DFS (G.adjlist)

