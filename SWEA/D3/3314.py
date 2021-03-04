#########################
#  SWEA number 3314
#  by 김승현                
#########################

# Q. 보충학습과 평균

for t in range(1, int(input())+1):
    score_list = list(map(int, input().split()))
    score_sum = 0
    for score in score_list:
        if score >= 40:
            score_sum += score
        else:
            score_sum += 40
    avg = score_sum//len(score_list)
    print("#%d %d" %(t, avg))