X = 1
cycle = 0
cycles = (20,60,100,140,180,220)
ans = 0
sprite = ['#','#','#']

pixel_w = 3
width = 40
height = 6
crt = [['.' for i in range(width)] for j in range(height)]

# PART 1
#with open("input.txt") as f:
#    for line in f:
#        t = line.strip().split(' ')
#        com = t[0]
#        if com == "noop":
#            cycle += 1
#            if cycle in cycles:
#                ans += X * cycle
#        elif com == "addx":
#            cycle += 1
#            if cycle in cycles:
#                ans += X * cycle
#            cycle += 1
#            if cycle in cycles:
#                ans += X * cycle
#            val = int(t[1])
#            X += val 
#    print(ans) 

# PART 2
with open("input.txt") as f:
    for line in f:
        t = line.strip().split(' ') 
        com = t[0]
        if com == "noop":
            cycle += 1
            if (int(cycle/width)) == height:
                break

            crt[int(cycle / width)][cycle % (width-1)] = '#' 
            ans += X * cycle
        elif com == "addx":
            cycle += 1
            if (int(cycle/width)) == height:
                break
            if cycle % width:
                ans += X * cycle
            cycle += 1
            if (int(cycle/width)) == height:
                break
            if cycle % width:
                ans += X * cycle
            val = int(t[1])
            X += val 
            print(cycle,X)
        