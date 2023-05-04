from DisjointSet import DisjointSet
class Vertex:
    
    def __init__(self,element):
        self.element=element

    def getelement(self):
        return self.element
    
    def __hash__(self):
        return hash(id(self))
    
class Edge:
    
    def __init__(self,u,v,weight=None):
        self.origin=u
        self.destination=v
        self.weight=weight
    
    def endpoints(self):
        return (self.origin,self.destination)
    
    def opposite(self,vertex):
        return self.destination if vertex is self.origin else self.origin
    
    def element(self):
        return self.weight

class Graph:
    
    def __init__(self,directed=False):
        self.__outgoing={} 
        self.__incoming={} if directed else self.__outgoing
    
    def is_directed(self):
        return self.__incoming is not self.__outgoing
    
    def vertex_count(self):
        return len(self.__outgoing.keys())
    
    def getVertices(self):
        return self.__outgoing.keys()
    
    def edge_count(self):
        total=sum(len(self.__outgoing[v]) for v in self.__outgoing)
        return total if self.is_directed else total//2
    
    def getEdges(self):
        result={}
        for secondary_map in self.__outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self,u,v):
        return self.__outgoing[u].get(v)
    
    def degree(self,source,directed=False):
        total=self.__incoming if directed else self.__outgoing
        return len(total[source])
    
    def incident_edges(self,vertex,directed=False):
        d=self.__incoming if directed else self.__outgoing
        edges={}
        for source in d:
            if vertex in d[source]:
                edges.update(d[source].get(vertex))
        return edges
    
    def insert_vertex(self,vertex):
        vertex=Vertex(vertex)
        self.__outgoing[vertex]={}
        if self.is_directed():
            self.__incoming[vertex]={}
        return vertex
    
    def insert_edge(self,u,v,w=None,directed=False):
        edge=Edge(u,v,w)
        self.__outgoing[u][v]=edge
        if self.is_directed():
            self.__incoming[v][u]=edge  
        else:
            self.__outgoing[v][u]=edge
        return edge
    
    def show_graph(self):
        return self.__outgoing

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i][0] <= R[j][0]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


n,m=6,8#tuple(map(int,input().split()))
G=Graph()
l=[(2 ,6 ,2),
(2,4 ,1),
(4, 10 ,7),
(4, 8 ,3),
(6 ,7, 5),
(6, 10 ,4),
(8 ,10 ,2),
(8, 7 ,3)]




# d_edges={}
# ll=[]
# for i in range(m):
#     a,b,w=l[i]#tuple(map(int,input().split())) 
#     a=G.insert_vertex(a)
#     b=G.insert_vertex(b)
#     ll.append((w,DisjointSet(a),DisjointSet(b)))
#     e=G.insert_edge(a,b,w)
#     d_edges[e]=(a,b)
    

# keys=[e.weight for e in d_edges.keys()]
# print()
# print(keys)
# print()
# mergeSort(ll,0,len(l)-1)
# d={}
# def find_MST(ll,cost=0,i=0,G=None):
#     if i==n:
#         d[cost]=G
#     else:
#         s=ll[i]
#         cost+=s[0]
#         p1=s[1].find(s[1].get_ultimate_parent()) 