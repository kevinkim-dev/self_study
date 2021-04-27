#########################
#  SWEA number 6190
#  by 김승현                
#########################

# Q. 정곤이의 단조 증가하는 수

def check_increase(num):
    while num >= 10:
        if num % 10 < (num // 10) % 10:
            return False
        num //= 10
    return True

for t in range(1, int(input())+1):
    N = int(input())
    num_list = sorted(list(map(int, input().split())), reverse=True)
    max_increase = -1
    for i in range(N-1):
        if num_list[i]*num_list[i+1] <= max_increase:
            break
        for j in range(i+1, N):
            num = num_list[i]*num_list[j]
            if check_increase(num):
                max_increase = max(max_increase, num)
    print("#%d %d" %(t, max_increase))
    
