#########################
#  SWEA number 1984
#  by 김승현                
#########################

# Q. 중간 평균값 구하기

for t in range(1, int(input())+1):
    num_list = list(map(int, input().split()))
    num_list.sort()
    print("#%d %d" %(t, round(sum(num_list[1:-1])/8)))