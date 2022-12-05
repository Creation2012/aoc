f = open("input.txt")

valid = 0

for x in f:
    control = False
    counter = 0
    temp = x.strip().split()
    zakres = temp[0]
    litera = temp[1]
    haslo = temp[2]

    z_min = int(zakres.split('-')[0])
    z_max = int(zakres.split('-')[1])
    litera = litera.replace(":","")

    if haslo[z_min-1] == litera and haslo[z_max-1] == litera:
        control = False
    elif haslo[z_min-1] != litera and haslo[z_max-1] != litera:
        control = False
    else:
        control = True

    if control == True:
        print(x)
        valid = valid + 1

print(valid)


