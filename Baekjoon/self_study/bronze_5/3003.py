###########################
#  BaekJoon 3003번
#  by 김승현                
###########################

# Q. 킹, 퀸, 룩, 비숍, 나이트, 폰

chess = [1, 1, 2, 2, 2, 8]

white = list(map(int, input().split()))

for i in range(len(chess)):
    white[i] = str(chess[i] - white[i])

ans = ' '.join(white)

print(ans)
