###########################
#  BaekJoon 2167번
#  by 김승현                
###########################

# Q. 2차원 배열의 합

row, col = map(int, input().split())
arr = [0]*row

for i in range(row):
    arr[i] = list(map(int, input().split()))
for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    _sum = 0
    for i in range(x1-1, x2):
        _sum += sum(arr[i][y1-1:y2])
    print(_sum)