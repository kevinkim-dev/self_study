#########################
#  SWEA number 1204
#  by 김승현                
#########################

# Q. 최빈수 구하기

for _ in range(1, int(input())+1):
    t = int(input())
    score_count = [0]*101
    score_list = list(map(int, input().split()))
    for score in score_list:
        score_count[score] += 1
    max_count = 0
    max_index = 0
    for idx in range(101):
        if score_count[idx] >= max_count:
            max_count = score_count[idx]
            max_index = idx
    print("#%d %d" %(t, max_index))