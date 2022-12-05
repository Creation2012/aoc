f = open("input.txt")

valid = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
eyes = ["amb","blu","brn","gry","grn","hzl","oth"]
validation = True
tab = f.readlines()

matches = []
control = 8
count = 0

for i in range(0,len(tab)):
    if tab[i].split() != [] and validation == True:
        matches = [x for x in valid if x in tab[i]]
        for x in matches:
            if validation == True:
                for y in tab[i].split():
                    if y.find(x) == 0:
                        o = y.split(x+':')[1]
                        #print("Debug: ",validation, o, y, x)
                        if x == "byr":
                            if 1920 <= int(o) <= 2002:
                                validation = True
                            else:
                                validation = False
                        elif x == "iyr":
                            if 2010 <= int(o) <= 2020:
                                validation = True
                            else:
                                validation = False
                        elif x == "eyr":
                            if 2020 <= int(o) <= 2030:
                                validation = True
                            else:
                                validation = False
                        elif x == "hgt":
                            if "cm" in o:
                                if 150 <= int(o.replace("cm","")) <= 193:
                                    validation = True
                                else:
                                    validation = False
                            elif "in" in o:
                                if 59 <= int(o.replace("in","")) <= 76:
                                    validation = True
                                else:
                                    validation = False
                        elif x == "hcl":
                            if o[0] == '#' and len(o) == 7:
                                for z in range(1,6):
                                    if ("0" <= o[z] <= "9") or ( "a" <= o[z] <= "f"):
                                        validation = True
                                    else:
                                        validation = False
                                        break
                            else:
                                validation = False
                        elif x == "ecl":
                            if o in eyes:
                                validation = True
                            else:
                                validation = False
                        elif x == "pid":
                            if len(o) == 9:
                                validation = True
                            else:
                                validation = False
                        
                        break
                
        valid = list(set(valid)-set(matches))
        #print(i, tab[i], valid)
    else:
        if (len(valid) == 0 or (len(valid) == 1 and valid[0] == "cid")) and validation == True:
            count = count + 1
            #print(tab[i-1])

        valid = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
        validation = True

if len(valid) == 0 or (len(valid) == 1 and valid[0] == "cid"):
    count = count + 1

print(count)
