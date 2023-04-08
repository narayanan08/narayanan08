initial_state=[[0,0,0],[0,0,0],[0,0,0]]
goal_state=[[0,0,0],[0,0,0],[0,0,0]]
given_depth=None
visited_states=[]

def read_inputs():
    global initial_state,goal_state,given_depth
    print("Enter initial state:")
    for i in range(3):
        for j in range(3):
            print("Enter a number from 1-9 for the point(",i,",",j,")(enter 0 for empty box):",end="")
            num=int(input())
            initial_state[i][j]=num
    print()
    print("Enter the goal state:")
    for i in range(3):
        for j in range(3):
            print("Enter a number from 1-9 for the point(",i,",",j,")(enter 0 for empty box):",end="")
            num=int(input())
            goal_state[i][j]=num
    given_depth=int(input("Assign the maximum depth:"))
    

def find(curr_state,path=[],depth=0):
    global visited_states,given_depth,goal_state
    if curr_state==goal_state:
        #path.append(curr_state)
        #print("answer-",path)
        return path
    
    if depth==given_depth:
        #print(path,"-Not the answer")
        return None
    
    else:
        #print("depth-",depth)                visited_states.append(new_state)
        #path.append(curr_state)
        (row,col)=locate_empty_box(curr_state)
        #print(row," ",col)

        if row==2 and col==0:
            new_state=move_down(curr_state,row-1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                    path.pop()
                    #print("depth-",depth)                visited_states.append(new_state)
                    pass    
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==2 and col==2:
            new_state=move_down(curr_state,row-1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==0 and col==2:
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                #print(visited_states)
                ans=find(new_state,path,depth+1)
                # print('fdsfsggfdge',ans)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
        #    print('new state-',new_state)
        #    print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==0 and col==0:
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            # print(curr_state)
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==1 and col==0:
            new_state=move_down(curr_state,row-1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==2 and col==1:
            new_state=move_down(curr_state,row-1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==1 and col==2:
            new_state=move_down(curr_state,row-1,col)
        #    print(new_state)
            #print("fgfgeggtrdfvjsd")
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==0 and col==1:
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        if row==1 and col==1:
            new_state=move_down(curr_state,row-1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_up(curr_state,row+1,col)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_right(curr_state,row,col-1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
            new_state=move_left(curr_state,row,col+1)
            # print('new state-',new_state)
            # print("visited-",visited_states)
            if new_state not in visited_states:
                path.append(new_state)
                visited_states.append(new_state)
                ans=find(new_state,path,depth+1)
                if isinstance(ans,(list)):
                    return ans
                else:
                   path.pop()
                   #print("depth-",depth)                visited_states.append(new_state)
                   pass
        
        #return path

def reconstruct_puzzle(state):
    temp=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            temp[i][j]=state[i][j]
            # print(temp)
    return temp
    
def locate_empty_box(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def move_up(state,i,j):
    temp=reconstruct_puzzle(state)
    if i in (1,2):
        temp[i-1][j]=temp[i][j]
        # print(state)
        temp[i][j]=0
        # print(state)
        return temp

def move_down(state,i,j):
    temp=reconstruct_puzzle(state)
    if i in (0,1):
        temp[i+1][j]=temp[i][j]
        # print(state)
        temp[i][j]=0
        # print(state)
        return temp

def move_left(state,i,j):
    temp=reconstruct_puzzle(state)
    if j in (1,2):
        temp[i][j-1]=temp[i][j]
        temp[i][j]=0
        return temp

def move_right(state,i,j):
    temp=reconstruct_puzzle(state)
    if j in (0,1):
        temp[i][j+1]=temp[i][j]
        temp[i][j]=0
        return temp

# print(read_initial_final_states())
# initial_state=[[1,4,3],[8,6,2],[0,5,7]]
# goal_state=[[1,3,5],[6,2,0],[7,8,4]]
#given_depth=6
#initial_state=[[1,0,2],[4,5,3],[7,8,6]]
#goal_state=[[1,2,3],[4,5,6],[7,8,0]]

read_inputs()
visited_states.append(initial_state)
l=find(initial_state,[initial_state])
if l:
    print("Path-")
    for i in range(len(l)):
        print(i,"-")
        for j in range(len(l[i])):
            print(l[i][j])
else:
    print("No path was found for this puzzle till the given depth.")