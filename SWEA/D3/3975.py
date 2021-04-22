#########################
#  SWEA number 3975
#  by 김승현                
#########################

# Q. 승률 비교하기

who = []
T = int(input())
for t in range(T):
    a, b, c, d = map(int, input().split())
    alice, bob = a / b, c / d
    if alice > bob:
        who.append('ALICE')
    elif alice == bob:
        who.append('DRAW')
    else:
        who.append('BOB')
for t in range(T):
    print("#%d %s" %(t+1, who[t]))

