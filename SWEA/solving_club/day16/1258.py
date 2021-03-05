#########################
#  SWEA number 1258
#  by 김승현                
#########################

# Q. 행렬찾기
        
for t in range(1, int(input())+1):
    N = int(input())
    danger = [0]*(N+1)
    danger_size = []
    for r in range(N):
        row = ''.join(list(input().split())).split('0')
        for bottle in row:
            if bottle:
                danger[len(bottle)] += 1
    for i in range(N+1):
        if danger[i]:
            danger_size.append([i, danger[i], i*danger[i]])
    danger_size = sorted(sorted(danger_size, key=lambda x: x[1]), key=lambda x: x[2])
    print("#%d %d %s" %(t, len(danger_size), ' '.join(' '.join(map(str, dan[1::-1])) for dan in danger_size)))
                

