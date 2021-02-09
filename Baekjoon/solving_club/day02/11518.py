def sum_con(numbers, length, i):
    result = 0
    for n in range(i, i+length):
        result += numbers[n]
    return result


T = int(input())

for t in range(1, T+1):
    num_num, length = map(int, input().split())
    numbers = list(map(int, input().split()))
    max_sum = sum_con(numbers, length, 0)
    min_sum = sum_con(numbers, length, 0)
    for i in range(1, num_num-length+1):
        _sum = sum_con(numbers, length, i)
        if _sum > max_sum:
            max_sum = _sum
            continue
        if _sum < min_sum:
            min_sum = _sum
    ans = max_sum - min_sum
    print("#%d %d" % (t, ans))
        