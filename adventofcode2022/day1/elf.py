file = "input.txt"

output = open(file,'r')

elf_calories = []
calories = 0
i = 0


for line in output:
    if line != '\n':
        calories += int(line)
    else:
        elf_calories.append(calories)
        i = i + 1
        calories = 0

top_three = 0

for i in range(0,3): 
    top_three += max(elf_calories)
    print(max(elf_calories))
    elf_calories.remove(max(elf_calories))

print(top_three)