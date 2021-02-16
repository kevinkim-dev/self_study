#########################
#  SWEA number 1961
#  by 김승현                
#########################

# Q. 숫자 배열 회전

# 90도: 첫 col, 마지막 row부터
# 180도: 마지막 row , 마지막 col부터
# 270도: 마지막 col , 첫번째 row부터
# rotate 에는 0, 1, 2 index에 각각 90, 180, 270도 회전한 row가 들어감

for t in range(1, int(input())+1):
    print("#%d" %t)
    size = int(input())
    square = [0]*size
    for i in range(size):
        square[i] = list(map(str, input().split()))
    for a in range(1, size+1):
        rotate = ['']*3
        for b in range(1, size+1):
            rotate[0] += str(square[size-b][a-1])
            rotate[1] += str(square[size-a][size-b])
            rotate[2] += str(square[b-1][size-a])
        print(rotate[0], rotate[1], rotate[2])
