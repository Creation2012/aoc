pwd = list()
val = 0
parent = 0
with open("input.txt") as f:
    for line in f:
        var = line.strip().split(' ')
        if var[0] == '$':
            if var[1] == 'cd':
                print(pwd,val, parent)
                if var[2] == '..':
                    pwd.pop()
                    parent = 0
                else:
                    parent += val 
                    pwd.append(var[2])
                val = 0
            elif var[1] == 'ls':
                pass
        elif var[0] == 'dir':
            pass # directory process
        else:
            val = val + int(var[0])