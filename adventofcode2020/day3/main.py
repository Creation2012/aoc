def slope(x,y):
    f = open("input.txt")

    row = 323 
    rs = 1
    column = 31
    cs = 1

    #step by r+1, c+3
    #on index 31 -> newline \n

    tab = f.readlines()
    tab = [x.strip() for x in tab]

    control = 0

    while rs <= 323:
        if tab[rs-1][cs-1] == '#':
            control = control + 1
            #print(rs, cs, tab[rs-1][cs-1])
       
        if cs + x > column:
            cs = cs + x - column 
        else:
            cs = cs + x

        rs = rs + y

    f.close()
    return control

print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))

#gadala baba z typem, a tym mial problem z odbytem
