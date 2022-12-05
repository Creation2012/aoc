file = "input.txt"
output = open(file,'r')
prior = 0

# PART 1
for line in output:
    size = int(len(line.strip())/2)
    comp1 = [*line[0:size]]
    comp2 = [*line[size:size*2]]
    filter = list(set(comp1).intersection(comp2))[0]
    prior += ord(filter)-96+26+32 if filter.isupper() else ord(filter)-96

# PART 2
three = list()
i = 1
for line in output:
    three.append([*line.strip()])

    if i != 3:
        i = i + 1
    else:
        filter = list(set(set(three[0]).intersection(three[1])).intersection(three[2]))[0]
        prior += ord(filter)-96+26+32 if filter.isupper() else ord(filter)-96
        three = list()
        i = 1

print(prior)