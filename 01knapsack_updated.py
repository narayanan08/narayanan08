items=[(1,(5,6)),(2,(10,5)),(3,(15,4)),(4,(20,3)),(5,(25,2))]# (weight,(profit/unit,units))
items=items[::-1]
# total_capacity=0
allowed=True
max_cost=float("-inf")
answer=None
def knapsack(items,types,total_capacity,cost=0,contents=[],i=0):
    global max_cost,answer,allowed
    if total_capacity<=0:
        # print("contents=",contents)
        # print("cost=",cost)
        if cost>max_cost:
            max_cost=cost
            answer=contents[:]
        return 
    
    if i==types:
        # print("contents=",contents)
        # print("cost=",cost)
        if cost>max_cost:
            max_cost=cost
            answer=contents[:]
            # print("cost=",cost)
            # print("contents=",contents)
        return 
    else:
        pair=items[i]
        temp=0
        for units in range(pair[1][1],0,-1):
            if total_capacity-units*pair[0]>=0:
                contribution=units*pair[1][0]
                cost+=contribution
                total_capacity-=units*pair[0]
                temp=units
                contents.append((pair[0],(contribution,units)))
                break
        else:
            allowed=False
        i+=1
        knapsack(items,types,total_capacity,cost,contents,i=i)
        # print(i)
        if len(contents)!=0 and allowed:
            e=contents.pop()
            cost-=e[1][0]
            total_capacity+=e[0]*e[1][1]
        knapsack(items,types,total_capacity,cost,contents,i=i)
        allowed=True

for total_cap in range(1,51):
    print("total_capacity=",total_cap)#int(input("Enter a capacity between 1 and 50(both inclusive): "))
    knapsack(items,len(items),total_cap)
    print("cost=",max_cost)
    print("answer=",answer)

        
