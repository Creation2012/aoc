from collections import Counter
f = open("input.txt")

def binary(bot,top,c):
    control = int((top-bot)/2)
    frontRange = [bot, bot+control]
    backRange = [bot+control+1, top]
    #print(frontRange,backRange,control,c)
    if 'F' == c or 'L' == c:
        return frontRange
    elif 'B' == c or 'R' == c:
        return backRange

topValue = -1
tab = [] 
for x in f:
    mainRange = [0b0,0b1111111]
    for i in range(0,7):
        #print("DEBUG INPUT mainRange:",mainRange)
        #print(i,end='')
        mainRange = binary(mainRange[0],mainRange[1],x[i])
        if mainRange[0] == mainRange[1]:
            break
        

    max = mainRange[0]

    mainRange = [0b0,0b111]
    for i in range(7,9):
        #print(i,end='')
        mainRange = binary(mainRange[0],mainRange[1],x[i])

    ID = max * 8 + mainRange[0]

    if topValue < ID:
        topValue = ID
    tab.append(ID)

tab.sort()
print(Counter(tab))
#print(tab)
result = set(tab)
dic = {}

#print(result)
#TODO: READ ABOUT THIS
#result = [i for i in tab if not i in exclude or exclude.remove(i)]
