###########################
#  BaekJoon 2740번
#  by 김승현                
###########################

# Q. 행렬 곱셈

def arr_mul(arr1, arr2, i, j, N):
    _sum = 0
    for n in range(N):
        _sum += arr1[i][n] * arr2[n][j]
    return _sum

A_row, A_col = map(int, input().split())
A_arr = [0]*A_row
for i in range(A_row):
    A_arr[i] = list(map(int, input().split()))

B_row, B_col = map(int, input().split())
B_arr = [0]*B_row
for i in range(B_row):
    B_arr[i] = list(map(int, input().split()))

for i in range(A_row):
    mul_row = []
    for j in range(B_col):
        mul_row.append(arr_mul(A_arr, B_arr, i, j, A_col))
    print(*mul_row)