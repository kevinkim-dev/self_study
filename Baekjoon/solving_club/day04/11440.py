T = int(input())

for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    flag = 0
    for i in range(1, 2 ** 10):
        subset_sum = 0
        for n in range(10):
            if i & (1 << n) != 0:
                subset_sum += num_list[n]
        if subset_sum == 0:
            print("#%d 1" %t)
            flag = 1
            break
    if flag == 0:
        print("#%d 0" %t)

# T = int(input())

# for t in range(1, T+1):
#     num_list = list(map(int, input().split()))
#     subset_sum = 0
#     flag = 0
#     for i in range(1, 2 ** 10):
#         subset_sum = 0
#         b = format(i, 'b').rjust(10, '0')
#         for n in range(10):
#             subset_sum += num_list[n]*int(b[n])
#         if subset_sum == 0:
#             print("#%d 1" %t)
#             flag = 1
#             break
#     if flag == 0:
#         print("#%d 0" %t)