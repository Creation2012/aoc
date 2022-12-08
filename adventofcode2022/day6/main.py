file = "input.txt"

output = open(file,'r')

# PART 1 and PART 2
v = 14 # or 14
for i in output:
    s = 0
    e = v + s #
    while e < len(i):
        ans = len(set(i[s:e]))
        if ans == v:
            print(set(i[s:e]))
            break
        s = s + 1
        e = e + 1

    print(e)