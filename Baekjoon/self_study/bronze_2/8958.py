###########################
#  BaekJoon 8958번
#  by 김승현                
###########################

# Q. OX퀴즈

for _ in range(int(input())):
    ox = input()
    idx = 0
    score = 0
    con_count = 1
    while idx < len(ox):
        if ox[idx] == 'O':
            score += con_count
            con_count += 1
        else:
            con_count = 1
        idx += 1
    print(score)