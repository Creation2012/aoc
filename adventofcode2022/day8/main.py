N = 0
l = []
ans = 0
scenic_score = 0
total_ss = 0
ss_list = list()

with open("input.txt") as f:
    for i, line in enumerate(f):
        N = len(line) 
        l.append([]*int(N))
        [l[i].append(int(j)) for j in line if j != '\n']

for i in range(0,N):
    for j in range(0,N):
        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
           ans += 1 
        else:
            visible = False 
            rows = list()
            cols = list()
            for o in range(0,N):
                # LEFT TO RIGHT
                if j == o:
                    pass
                elif l[i][j] > l[i][o]:
                    visible = True
                    rows.append(True)
                else:
                    visible = False
                    rows.append(False)

                # UP TO DOWN
                if i == o:
                    pass
                elif l[i][j] > l[o][j]:
                    visible = True
                    cols.append(True)
                else:
                    visible = False
                    cols.append(False)

            scenic_score = 0
            total_ss = 0

            if (all(rows[:j]) or  all(rows[j:]) or all(cols[:i]) or all(cols[i:])):
                for e in list(reversed(rows[:j])):
                    if e == False:
                        scenic_score += 1
                        break
                    else:
                        scenic_score += 1
                    
                total_ss = scenic_score
                scenic_score = 0

                for e in rows[j:]:
                    if e == False:
                        scenic_score += 1
                        break
                    else:
                        scenic_score += 1

                total_ss = total_ss * scenic_score
                scenic_score = 0
                    
                for e in list(reversed(cols[:i])):
                    if e == False:
                        scenic_score += 1
                        break
                    else:
                        scenic_score += 1

                total_ss = total_ss * scenic_score
                scenic_score = 0

                for e in cols[i:]:
                    if e == False:
                        scenic_score += 1
                        break
                    else:
                        scenic_score += 1

                total_ss = total_ss * scenic_score
                scenic_score = 0

                ss_list.append(total_ss)

                #print(i,j,l[i][j]) 
                #print(rows[:j], rows[j:])
                #print(cols[:i], cols[i:])
                ans = ans + 1
        
# PART 1
print(ans)

# PART 2
print(max(ss_list))