###########################
#  BaekJoon 10214번
#  by 김승현                
###########################

# Q. Baseball 

answer = []

for _ in range(int(input())):
    y, k = 0, 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        answer.append('Yonsei')
    elif y == k:
        answer.append('Draw')
    else:
        answer.append('Korea')

for ans in answer:
    print(ans)