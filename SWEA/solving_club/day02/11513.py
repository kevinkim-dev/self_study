T = int(input())

for t in range(1, T+1):
    length = int(input())
    num_list = list(map(int, input().split()))
    max_num = 0
    min_num = 1000001
    for num in num_list:
        if num > max_num:
            max_num = num
            continue
        if num < min_num:
            min_num = num
    print("#%d %d" % (t, max_num-min_num))
