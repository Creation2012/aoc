file = "input.txt"
output = open(file,'r')

shape = (1,2,3)
outcome = (3,6,0)
first = ("A","B","C")
second = ("X","Y","Z")

# dict per action rock, paper, scissors
round = {"A X":3+1,
         "A Y":6+2,
         "A Z":0+3,
         "B X":0+1,
         "B Y":3+2,
         "B Z":6+3,
         "C X":6+1,
         "C Y":0+2,
         "C Z":3+3}

# dict per result lose, draw, win
result = {"A X":0+3,
          "A Y":3+1,
          "A Z":6+2,
          "B X":0+1,
          "B Y":3+2,
          "B Z":6+3,
          "C X":0+2,
          "C Y":3+3,
          "C Z":6+1}

total_score = 0

for line in output:
    total_score += result[line.strip()]
    
print(total_score)