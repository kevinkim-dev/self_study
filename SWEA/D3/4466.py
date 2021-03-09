#########################
#  SWEA number 4466
#  by 김승현                
#########################

# Q. 최대 성적표 만들기

for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)
    print("#%d %d" %(t, sum(scores[0: K])))