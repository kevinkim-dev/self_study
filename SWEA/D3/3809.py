#########################
#  SWEA number 3809
#  by 김승현                
#########################

# Q. 화섭이의 정수 나열

for t in range(1, int(input())+1):
    N = int(input())
    num_list = []
    while N != len(num_list):
        num_list.extend(list(map(int, input().rstrip().split())))
    all_num = set()
    for n in range(1, N+1):
        for i in range(N-n+1):
            all_num.add(int(''.join(map(str, num_list[i:i+n]))))
        if len(all_num) != 10**n:
            break
    all_num = sorted(list(all_num))
    for i in range(len(all_num)):
        if i != all_num[i]:
            print("#%d %d" %(t, i))
            break