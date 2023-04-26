class node:
    def __init__(self,key=None,value=None,left=None,right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0 for x in range(n1)]
	R = [0 for x in range(n2)]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		#print('R ',j,'',R)
		R[j] = arr[m + 1 + j]
	j = 0	 # Initial index of second subarray
	i = 0	 # Initial index of first subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i].value <= R[j].value:
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

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

def print_codes(root,code=[]):
	if root.left==root.right==None:
		print(root.key,":","".join(code))
	else:
		if root.left:
			code.append('0')
			print_codes(root.left,code)
			code.pop()
		if root.right:
			code.append('1')
			print_codes(root.right,code)
			code.pop()

def decode(root,encoded_string):
    index=0
    curr=root
    prev=root
    while index<len(encoded_string):
        #curr=prev
        while curr.left!=None or curr.right!=None:
            if encoded_string[index]=='0':
                curr=curr.left
                index+=1
            elif encoded_string[index]=='1':
                curr=curr.right
                index+=1
        print(curr.key,end="")
        curr=root
	

message='aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff'#input("Enter a message:")
characters=set(message)
char_freq={}
nodes=[]
for character in characters:
    char_freq[character]=message.count(character)
    nodes.append(node(character,message.count(character)))




n = len(nodes)
length=n
while length>=2:
    if length>2:
        mergeSort(nodes, 0, n-1)
        left=nodes.pop(0)
        right=nodes.pop(0)
        new_node=node(value=left.value+right.value,left=left,right=right)
        left.parent,right.parent=new_node,new_node
        nodes.append(new_node)
        length-=1
        n-=1
    else: 
        mergeSort(nodes, 0, n-1)
        left=nodes.pop(0)
        right=nodes.pop(0)
        new_node=node(value=left.value+right.value,left=left,right=right)
        left.parent,right.parent=new_node,new_node
        nodes.append(new_node)
        length-=1
        n-=1
    print()
    for node__ in nodes:
	    print(node__.key,":",node__.value)
    
root=nodes[0]
print_codes(root)


encoded_string=""	

decode(root,encoded_string)