H = (0,0) 
T = (0,0)
nrows = 0
ncols = 0
visited = set()

with open("input.txt") as f:
    for line in f:
        l = line.strip().split(' ')
        colstart = ncols
        rowstart = nrows
        if l[0] == 'R':
            ncols += int(l[1])
        elif l[0] == 'L':
            ncols -= int(l[1])
        elif l[0] == 'U':
            nrows += int(l[1])
        elif l[0] == 'D':
            nrows -= int(l[1])
       
        #print("S: {} {}", colstart, rowstart)
        #print("C: {} {}", ncols, nrows)

        if colstart != ncols:
            # HORIZONTAL L - R 
            if colstart > ncols:
                s = -1
            else:
                s = 1
            for i in range(colstart,ncols+s,s):
                #print("Column: ",i,end=' ')
                H = (rowstart,i)
                visited.add(T)
                if H[1] - T[1] > 1:
                    T = (T[0],T[1]+1)
                    if H[0] > T[0]:
                        T = (T[0]+1,T[1])
                    elif H[0] < T[0]:
                        T = (T[0]-1,T[1])
                elif H[1] - T[1] < -1:
                    T = (T[0],T[1]-1)
                    #print("LEFT")
                    if H[0] > T[0]:
                        T = (T[0]+1,T[1])
                    elif H[0] < T[0]:
                        T = (T[0]-1,T[1])
            
        elif rowstart != nrows:
            # VERTICAL U - D
            if rowstart> nrows:
                s = -1
            else:
                s = 1
            for i in range(rowstart, nrows+s,s):
                #print("Row: ",i,end=' ')
                H = (i,colstart)
                visited.add(T)
                if H[0] - T[0] > 1:
                    T = (T[0]+1,T[1])
                    if H[1] > T[1]:
                        T = (T[0],T[1]+1)
                    elif H[1] < T[1]:
                        T = (T[0],T[1]-1)
                elif H[0] - T[0] < -1:
                    T = (T[0]-1,T[1])
                    if H[1] > T[1]:
                        T = (T[0],T[1]+1)
                    elif H[1] < T[1]:
                        T = (T[0],T[1]-1)
            
        #print()
        #print("HEAD:",H)
        #print("TAIL:",T)


        #visited.add((nrows,ncols))

print(visited)
print(len(visited))