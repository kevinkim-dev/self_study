T = int(input())

for t in range(1, T+1):
    max_sum = float('-inf')
    a, b = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    if a > b:
        dif = a - b
        short = b
        for i in range(dif+1):
            _sum = 0
            for j in range(short):
                _sum += list_a[j+i] * list_b[j]
            if _sum > max_sum:
                max_sum = _sum
    else:
        dif = b - a
        short = a
        for i in range(dif+1):
            _sum = 0
            for j in range(short):
                _sum += list_a[j] * list_b[j+i]
            if _sum > max_sum:
                max_sum = _sum
    print("#%d %d" % (t, max_sum))