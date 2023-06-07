""" 0/1 knapsack problem using branch and bound algorithm"""

OBJS=5
CAP=25
gdg={5:(1,6)}
obj_profit={5:(1,6),4:(2,5),3:(3,4),2:(4,3),1:(5,2)} 
pairs=[]
for p in obj_profit.items():
    pairs.append(p)
obj_profit=pairs
max_cost=float('-inf')
answer=[None]

def find_max_profit(obj_profit,remaining_cap=0,cost=0,contents=[],t=1,tt=0,ind=0):
    global max_cost,answer
    # print(contents)
    if obj_profit==[] or remaining_cap==0:
        # print("hrhrhr")
        # print("contents=",contents)
        # print("cost=",cost)
        # print()
        if cost>max_cost:
            answer=contents[:]
            max_cost=cost
        return

    if remaining_cap<0:
        # print("eeee")
        return
    
    # if remaining_cap==0:
    #     if cost>max_cost:
    #         answer=contents[:]
    #         max_cost=cost
            
    else:
        # print("fgegerg")
        for i in range(len(obj_profit)):
            pair=obj_profit[0]
            # print("obj_profit under for i in range-",obj_profit)
            # print("i=",i)
            # print("remaining=",obj_profit[i:])
            objs=pair[1][0]
            for j in range(objs,0,-1):
                weight=j*pair[0]
                if remaining_cap-weight>=0:
                    remaining_cap-=weight
                    cost+=j*pair[1][1]
                    contents.append([pair[0],(weight,j*pair[1][1])])
                    break
            remaining=obj_profit[i+1:]
            t+=1
            if remaining==[]:
                
                find_max_profit([],remaining_cap=remaining_cap,cost=cost,contents=contents,t=t,tt=tt)
            else:
                for k in range(len(remaining)):
                    find_max_profit(remaining[k:],remaining_cap,cost,contents,t=t,tt=tt)
            removed_pair=contents.pop()
            cost-=removed_pair[1][1]
            remaining_cap+=removed_pair[1][0]
            t-=1
            if t==1:
                obj_profit=obj_profit[:]
            # print("ytytryrty")
            # print("obj_profit=",obj_profit)
            # print("contents=",contents)
    
    

find_max_profit(obj_profit,CAP)
print("answer=",answer)
print("cost=",max_cost)
            


