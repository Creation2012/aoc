file = "input.txt"
output = open(file, 'r')

ans = 0

def inner(range1, range2):
    global ans
    for i in range1:
        for j in range2:
            if i == j:
                ans = ans + 1
                return

for line in output:
    cont = line.strip().split(",")
    lrange1 = cont[0].split("-")
    lrange2 = cont[1].split("-")

    range1 = int(lrange1[0]),int(lrange1[1])
    range2 = int(lrange2[0]),int(lrange2[1])

    # (4, 6) (6, 6)
    # PART 1 
    #if range1[1] < range2[1]:
    #    if range1[0] >= range2[0]:
    #        ans = ans + 1
    #elif range1[1] > range2[1]:
    #    if range1[0] <= range2[0]:
    #        ans = ans + 1
    #elif range1[1] == range2[1]:
    #    if range1[0] > range1[1]:
    #        ans = ans + 1
    #    else:
    #        ans = ans + 1
            
    # PART 2 
    range1 = range(int(lrange1[0]),int(lrange1[1])+1)
    range2 = range(int(lrange2[0]),int(lrange2[1])+1)
    
    inner(range1,range2) 


print(ans)