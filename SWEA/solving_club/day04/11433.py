T = int(input())

d_row = [1, 0, -1, 0]
d_col = [0, 1, 0, -1]

for t in range(1, T+1):
    array = [0]*5
    all_sum = 0
    for n in range(5):
        array[n] = list(map(int, input().split()))
    for i in range(5):
        for j in range(5):
            _sum = 0
            for d in range(4):
                if i + d_row[d] >= 0 and i + d_row[d] <= 4 and j + d_col[d] >= 0 and j + d_col[d] <= 4:
                    _sum += abs(array[i][j] - array[i+d_row[d]][j+d_col[d]])
            all_sum += _sum
    print("#%d %d" %(t, all_sum))


            
            