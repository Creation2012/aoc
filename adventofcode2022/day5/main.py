file = "input.txt"
output = open(file,'r')

N = 9 

stacks = [[]*N for i in range(N)]

col = 0
row = 0

while 1:
    char = output.read(1)
    if not char or char == '1':
        break
   
    col = col + 1
    if char != ' ' and char != '\n' and char != '[' and char != ']':
        ns = col // 4 + 1
        idx_col = ns - 1
        stacks[idx_col].append(char)

    if char == '\n':
        row = row + 1
        col = 0

output.close()

with open(file) as f:
    actions = f.readlines()[N+1:]
    
for i in range(N):
    stacks[i].reverse()

actions = list(map(lambda x:x.strip(), actions))

for line in actions:
    xs = line.split(' ')
    action = {xs[0]:xs[1],
         xs[2]:xs[3],
         xs[4]:xs[5]}

    # PART 1
    #for i in range(int(action['move'])):
        #popped = stacks[int(action['from'])-1].pop()
        #stacks[int(action['to'])-1].append(popped)
    
    # PART 2
    mv = int(action['move'])
    fr = int(action['from'])-1
    stacklen = len(stacks[fr])
    popped = stacks[fr][stacklen-mv:]
    stacks[fr] = stacks[fr][0:stacklen-mv]
    to = int(action['to'])-1
    stacks[to].extend(popped)

    #[print(i) for i in stacks]
    #print("================")
    
[print(i.pop(),end='') for i in stacks]