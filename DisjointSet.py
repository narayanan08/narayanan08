class Node:
    
    def __init__(self,element,parent=None,children=[]):
        self.element=element
        self.parent=parent
        self.children=children

    def getelement(self):
        return self.element

class DisjointSet:
    
    def __init__(self,key):
        self.ultimate_parent=self
        self.children_sets=[]
        self.key=key
        self.rank=0
    
    def union(self,other):
        if self.ultimate_parent!=other.ultimate_parent:
            r1,r2=self.find_rank(),other.find_rank()
            print(r1,"  ",r2)
            if r1>r2:
                print("2")
                other.ultimate_parent=self
                self.children_sets.append(other)
            else:
                print("5")
                self.ultimate_parent=other
                other.children_sets.append(self)

    def find_rank(self,l=[]):
        if self.children_sets==[]:
            return 0
        else:
            for child in self.children_sets:
                ht=1+child.find_rank()
                l.append(ht)
            return max(l)

            

    def find(self,root,value):
        if root.children_sets==[]:
            return self
        else:
            for child in root.children_sets:
                if child.key.element==value:
                    child.ultimate_parent=self
                    if child not in self.children_sets:
                        self.children_sets.append(child)
                    print("Found out successfully.")
                    return self
                else:
                    p=self.find(child,value)
                    child.ultimate_parent=self
                    if child not in self.children_sets:
                        self.children_sets.append(child)
                    #self.children.append(value)
                return p
        
    def get_ultimate_parent(self):
        return self.ultimate_parent
        

if __name__=="__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(6)
    n7=Node(7)
    n8=Node(8)
    n9=Node(9)
    n10=Node(10)

    d1=DisjointSet(n1)
    d2=DisjointSet(n2)
    d3=DisjointSet(n3)
    d4=DisjointSet(n4)
    d5=DisjointSet(n5)
    d6=DisjointSet(n6)
    d7=DisjointSet(n7)
    d8=DisjointSet(n8)
    d9=DisjointSet(n9)
    d10=DisjointSet(n10)

    d2.union(d1)
    print(d1.children_sets)
    d4.union(d3)
    print(d3.children_sets)
    d6.union(d5)
    print(d5.children_sets)
    d8.union(d7)
    print(d7.children_sets)
    d10.union(d9)
    print(d9.children_sets)

    d2.union(d4)
    print(d4.children_sets)
    d6.union(d8)
    print(d8.children_sets)

    d1.union(d4)

    print(d4.children_sets)
    print(d4.find(d4.ultimate_parent,2))
    l=[child.key.element for child  in d4.children_sets]
    print(l)
