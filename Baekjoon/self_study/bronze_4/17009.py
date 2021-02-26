###########################
#  BaekJoon 17009번
#  by 김승현                
###########################

# Q. Winning Score

A_score = 0
B_score = 0

for n in range(3, 0, -1):
    A_score += int(input())*n
for n in range(3, 0, -1):
    B_score += int(input())*n
print('A') if A_score > B_score  else print('B') if B_score > A_score else print('T')