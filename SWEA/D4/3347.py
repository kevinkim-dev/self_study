#########################
#  SWEA number 3347
#  by 김승현                
#########################

# Q. 올림픽 종목 투표 

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = list(map(int, input().split())), list(map(int, input().split()))
    vote = [0]*N
    for b in B:
        for i in range(N):
            if A[i] > b:
                continue
            vote[i] += 1
            break
    print("#%d %d" %(t, vote.index(max(vote))+1))