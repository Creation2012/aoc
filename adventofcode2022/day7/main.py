
# cd / - root directory
# cd a - directory a
# cd .. - go back
# ls - list directory

pwd = ''
dir_sizes = {} 

with open("input.txt") as f:
    for line in f:
        var = line.strip().split(' ')
        if var[0] == '$':
            if var[1] == "cd":
                #cd[var[1]] = var[2]
                if var[2] == "/":
                    #pwd += var[2]
                    pass
                elif var[2] == "..":
                    pwd += var[2]
                else:
                    pwd += var[2]+"/"
            elif var[1] == "ls":
                pass
        elif var[0] == "dir":
            pass
        else:
            dir_sizes[pwd] = dir_sizes.get(pwd,0) + int(var[0])
            #print(int(var[0]))

depth = 0
order = list()

print(dir_sizes)

for dir in dir_sizes:
    indepth = dir.count('/')
    outdepth = dir.count("..")
    depth = indepth - outdepth
    #print(depth, dir,dir_sizes[dir])
    order.append([depth,dir,dir_sizes[dir]]) 
    

for i in range(0,len(order)):
    for j in range(0,len(order)):
        if order[i][0] < order[j][0]:
            order[i][2] += order[j][2]
            print(order[i][1]," - ",order[j][1])

            
for i in order:
    print(i)