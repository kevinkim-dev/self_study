#########################
#  SWEA number 1491
#  by 김승현                
#########################

# Q. 원재의 벽 꾸미기

for t in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    x = int(N ** 0.5)
    min_score = float('inf')
    for r in range(1, x+1):
        c = N // r
        score = A*abs(r-c) + B*(N - r*c)
        score2 = B*(N - r*r)
        min_score = min(score, score2, min_score)
    print("#%d %d" %(t, min_score))