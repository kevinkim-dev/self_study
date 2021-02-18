#########################
#  SWEA number 11522
#  by 김승현                
#########################

def palindrom(pal):
    string = pal
    while string:
        if string[0] == string[-1]:
            string = string[1:-1]
        else:
            return False
    return True

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    square = [0]*N
    for n in range(N):
        square[n] = input()
        for i in range(N-M+1):
            string = square[n][i:i+M]
            if palindrom(string):
                print("#%d %s" %(t, string))
    for col in range(N):
        for row in range(N-M+1):
            string = ''
            for i in range(M):
                string += square[row+i][col]
        if palindrom(string):
            print("#%d %s" %(t, string))