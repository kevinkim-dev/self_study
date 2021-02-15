for a in range(10):
    t = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    max_sum = float('-inf')
    temp_cross_sum = 0
    temp_rev_cross_sum = 0
    for i in range(100):
        temp_row_sum = 0
        temp_col_sum = 0
        for j in range(100):
            temp_row_sum += array[i][j]
            temp_col_sum += array[j][i]
            if temp_row_sum > max_sum:
                max_sum = temp_row_sum
            if temp_col_sum > max_sum:
                max_sum = temp_col_sum
        temp_cross_sum += array[i][i]
        temp_rev_cross_sum += array[i][99-i]
    if temp_cross_sum > max_sum:
        max_sum = temp_cross_sum
    if temp_rev_cross_sum > max_sum:
        max_sum = temp_rev_cross_sum
    print("#%d %d" % (t, max_sum))