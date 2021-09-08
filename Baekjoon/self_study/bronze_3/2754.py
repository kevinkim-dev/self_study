###########################
#  BaekJoon 2754번
#  by 김승현                
###########################

# Q. 학점계산

alpha = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, '+': 0.3, '0': 0.0, '-': -0.3}

score = input()

if score == 'F':
    print(str(0.0))
else:
    print(alpha[score[0]] + alpha[score[1]])