#########################
#  SWEA number 2005
#  by 김승현                
#########################

# Q. 파스칼의 삼각형

for t in range(1, int(input())+1):
    print("#%d" %t)
    size = int(input())
    array = [0]*size
    for i in range(size):
        array[i] = [0]*(i+1)
        for j in range(i+1):
            if j == 0 or j == i:
                array[i][j] = 1
            else:
                array[i][j] = array[i-1][j-1] + array[i-1][j]
        print(*array[i])