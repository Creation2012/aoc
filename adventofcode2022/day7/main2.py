# wrong answers: 1366529 
# proposition:   1366529

pwd = ''
dirs = {}
dirs['/'] = 0 
dir_files = {}
parent = ''

with open("input.txt") as f:
    for line in f:
        var = line.strip().split(' ')
        if var[0] == '$':
            if var[1] == "cd":
                if var[2] == "/":
                    pwd = "/"
                elif var[2] == "..":
                    pwd = pwd[:len(pwd[:-1])-last_added]
                else:
                    pwd += var[2]+"/"
                    last_added = len(var[2]+"/")
            elif var[1] == "ls":
                parent = pwd
        elif var[0] == "dir":
            dirs[parent] = 1
            #dir_files[pwd].append(var[1]) 
        else:
            pass
            #print(var)
            #dirs[pwd] = {var[1]: int(var[0])} 
            #dirs[pwd] = {(var[0],var[1])}
            #dirs[pwd] = dirs.get(pwd,0) + int(var[0])
            #dir_files[pwd].append(var[1]) 


print(dirs)

depth = 0
new_ds = {}
last_added = 0

#for dir in dir_sizes:
#    new = '/'
#    l = list(filter(('').__ne__,dir.split('/')))
#    #print(l)
#    for i, el in enumerate(l):
#        #print(i,el)
#        if el != ".." and el != '':
#            new += el + "/"
#            last_added = len(el)
#        elif el != '':
#            if last_added > 0: 
#                new = new[:len(new[:-1])-last_added]
#
#    new_ds[new] = dir_sizes[dir]

print(new_ds)
print()

for i, el in enumerate(new_ds):
    for j, el2 in enumerate(new_ds):
        if i != j:
            # check exact directory /name/
            if "/"+el in "/"+el2:
                #print(el,el2)
                new_ds[el] += new_ds[el2] 

at_most = 0

print(new_ds)
for i in new_ds:
    if new_ds[i] < 100000:
        print(new_ds[i])
        at_most += new_ds[i]

print(at_most)