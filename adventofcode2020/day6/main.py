f = open("input.txt")

# a b c x y z

sum = 0
val = []
for x in f:
    y = x.split()
    if len(y) == 0:
        for i in range(0,len(val)-1):
            val[i+1].intersection_update(val[i])
        
        val[len(val)-1].remove('\n')

        sum = sum + len(val[len(val)-1])
        print(val[len(val)-1],sum,len(val[len(val)-1]))
        val = []
        input()
    else:
        val.append(set(x))

        #print(val)

print(sum)
