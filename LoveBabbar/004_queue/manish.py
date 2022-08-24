def traverse(x,y,arr):
    
    if arr[x][y+1]==0:
        return 1+ traverse(x,y+1,arr)
    elif arr[x+1][y] == 0:
        return 1 + traverse(x+1,y,arr)
    elif arr[x+1][y] == 2 or arr[x][y+1]==2:
        return 1
    else :
        return -1



def rescue(m,n, arr):
    x1,x2,y1,y2 = 0,0,0,0
    
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                x1 = i
                y1 = j
            elif arr[i][j] == 2:
                x2 = i
                y2 = j
    
    if arr[x1][y1+1] == 0:
        return 1+traverse(x1, y1+1, arr)
    elif arr[x1+1][y1] == 0:
        return 1+traverse(x1+1, y1, arr)
    elif arr[x1][y1+1] == 2 or arr[x1+1][y1] == 2:
        return 2
    else:
        return -1

    


if __name__ == '__main__':
    m = 4
    n = 4
    
    arr = [[1,-1,-1,-1], [0,0,0,0], [0,0,-1,0], [0,0,-1,2]]
    print(rescue(m,n,arr))
    

