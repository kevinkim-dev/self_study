#########################
#  SWEA number 10505
#  by 김승현                
#########################

# Q. 소득 불균형

for t in range(1, int(input())+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    avg = sum(num_list)/n
    cnt = 0
    for num in num_list:
        if num <= avg:
            cnt += 1
    print("#%d %d" %(t, cnt))