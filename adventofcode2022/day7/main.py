pwd = ''
dir_sizes = {} 

with open("input.txt") as f:
    for line in f:
        var = line.strip().split(' ')
        if var[0] == '$':
            if var[1] == "cd":
                if var[2] == "/":
                    pass
                elif var[2] == "..":
                    pwd += var[2]+"/"
                else:
                    pwd += var[2]+"/"
            elif var[1] == "ls":
                pass
        elif var[0] == "dir":
            pass
        else:
            dir_sizes[pwd] = dir_sizes.get(pwd,0) + int(var[0])

depth = 0
new_ds = {}
last_added = 0

for dir in dir_sizes:
    new = '/'
    for i, el in enumerate(dir.split('/')):
        print(i,el)
        if el != ".." and el != '':
            new += el + "/"
            last_added = len(new)
        elif el != '':
            if last_added > 0: 
                new = new[:len(new)-last_added]

    new_ds[new] = dir_sizes[dir]

print(new_ds)

for i, el in enumerate(new_ds):
    for j, el2 in enumerate(new_ds):
        if i != j:
            # check exact directory /name/
            if "/"+el in "/"+el2:
                print(el,el2)
                new_ds[el] += new_ds[el2] 

at_most = 0

print(new_ds)
for i in new_ds:
    if new_ds[i] <= 100000:
        print(new_ds[i])
        at_most += new_ds[i]

print(at_most)