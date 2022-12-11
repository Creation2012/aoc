l = {}

with open("input.txt") as f:
    for line in f:
        x = line.strip()
        l[x] = l.get(x,0) + 1

[print(i,l[i]) for i in l if l[i] > 1]

#czvcf -> nwqgchw
#pdbdwmc -> nwqgchw
