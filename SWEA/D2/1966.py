#########################
#  SWEA number 1966
#  by 김승현                
#########################

# Q. 숫자를 정렬하자

T = int(input())

for t in range(1, T+1):
    list_len = int(input())
    num_list = list(map(int, input().split()))
    for i in range(list_len-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    for idx in range(list_len):
        num_list[idx] = str(num_list[idx])
    ans = " ".join(num_list)
    print("#{0} {1}".format(t, ans))
