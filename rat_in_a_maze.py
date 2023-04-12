# paths=[]
def find(maze,x,y,N,path):
    global paths
    if (x,y)==(0,0) or (x,y)==(N-1,0) or (x,y)==(N-1,N-1) or (x,y)==(0,N-1):
        # paths.append(path)
        # for i in range(len(path)):
        #     print(path[i])
        print(path)
        
    else:
        temp_pos=move_up(maze,x,y,N)
        if temp_pos and temp_pos not in path:
            path.append(temp_pos)
            r=find(maze,temp_pos[0],temp_pos[1],N,path)
            if not r:
                path.pop()
            else:
                #return path
                pass
        temp_pos=move_right(maze,x,y,N)
        if temp_pos and temp_pos not in path:
            path.append(temp_pos)
            r=find(maze,temp_pos[0],temp_pos[1],N,path)
            if not r:
                path.pop()
            else:
                #return path
                pass
        temp_pos=move_down(maze,x,y,N)
        if temp_pos and temp_pos not in path:
            path.append(temp_pos)
            r=find(maze,temp_pos[0],temp_pos[1],N,path)
            if not r:
                path.pop()
            else:
                # return path
                pass
        temp_pos=move_left(maze,x,y,N)
        if temp_pos and temp_pos not in path:
            path.append(temp_pos)
            r=find(maze,temp_pos[0],temp_pos[1],N,path)
            if not r:
                path.pop()
            else:
                #return path
                pass

def move_up(maze,i,j,N):
    i-=1
    if i!=-1:
        if maze[i][j]==0:
            return None
        else:
            return i,j
    else:
        return None

def move_left(maze,i,j,N):
    j-=1
    if j!=-1:
        if maze[i][j]==0:
            return None
        else:
            return i,j
    else:
        return None

def move_down(maze,i,j,N):
    i+=1
    if i!=N:
        if maze[i][j]==0:
            return None
        else:
            return i,j
    else:
        return None

def move_right(maze,i,j,N):
    j+=1
    if j!=N:
        if maze[i][j]==0:
            return None
        else:
            return i,j
    else:
        return None



N=int(input("Enter the side of the maze(only square maze):"))
maze=[[int(input("Enter zero or one:")) for i in range(6)]for j in range(6)]
intial_position=eval(input("Enter the initial position of the rat:"))
find(maze,intial_position[0],intial_position[1],N,[intial_position])

    
# N=6
# maze=[[1,1,0,1,1,1],
#       [0,1,0,1,1,1],
#       [1,1,0,1,0,0],
#       [1,0,1,1,0,0],
#       [1,1,1,0,0,0],
#       [0,0,0,0,0,1]]
# intial_position=(3,2)
# find(maze,intial_position[0],intial_position[1],N,[intial_position])

# for path in paths:
#     print(path)
#     print()