f = open("test.txt")
tab = []
merg = {}
tempString = ''
part = 0
for x in f:
    row = x.split()
    row = [e for e in row if 'bag' not in e and 'contain' not in e and 'other' not in e]
    #i = 0
    #row = [e if i > 3 else i = 0 for e in row, i = i + 1]
    i = 0
    for a in row:
        if i < 2:
            tempString += ' '+ a
            i = i + 1
        elif i == 2:
            if a == 'no':
                merg[tempString] = 0
            else:
                merg[tempString] = int(a)

            print(tempString + ' ', merg[tempString])
            i = 0
            tempString = ''
