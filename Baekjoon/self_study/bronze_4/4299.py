###########################
#  BaekJoon 4299번
#  by 김승현                
###########################

# Q. AFC 윔블던

s, d = map(int, input().split())

win = (s + d)/2
lose = (s - d)/2

if (s+d)%2 == 1 or s < d:
    print('-1')
else:
    print(int(win), int(lose))