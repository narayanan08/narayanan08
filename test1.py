import math
import csv

class BST:
	def __init__(self,key):
		self.key=key
		self.lchild=None
		self.rchild=None

	def insert(self,data,position):
		if self.key is None:
			self.key=data
			return
		elif self.key>data:
			if self.lchild is None:
				self.lchild= BST(data)
			else:
				self.lchild.insert(data)
		else:
			if self.rchild:
				self.rchild.insert(data)
			else:
				self.rchild= BST(data)
	
	def inorder(self):
		if self.lchild:
			self.lchild.inorder()
		print(self.key,end= ", ")
		if self.rchild:
			self.rchild.inorder()
    
f=open(r"IT-A details.txt","r")
#r=csv.reader(f)
n=next(csv.reader)
l=[]
for i in csv.reader(f):
	l.append(i)
f.close()

#print(32)
n=32
p=n
i=0
q=n
c=0
obj=BST(32)
while c<6:
    
    for j in range(2**i):
#        if j ==(2**i)-1-1:
#            break
#        print(p)
        obj.insert(p)
        p= p + 2**((math.log(q,2))+1)
    i+=1
    o = n/(2**i)
    p=o
#    i+=1
    q=o
    c+=1
obj.inorder()