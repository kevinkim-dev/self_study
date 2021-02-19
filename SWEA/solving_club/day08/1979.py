#########################
#  SWEA number 1979
#  by 김승현                
#########################

# Q. 어디에 단어가 들어갈 수 있을까

T = int(input())

for t in range(1, T+1):
    N, word_len = map(int, input().split())
    square = [0]*(N+2)
    word_count = 0
    for i in range(N+2):
        if i == 0 or i == N+1:
            square[i] = [0]*(N+2)
        else:
            square[i] = [0] + list(map(int, input().split())) + [0]
    # 가로로 word_len개 1이 있는지 확인
    for row in range(1, N+1):
        for col in range(1, N-word_len+2):
            if (square[row][col:col+word_len] == [1]*word_len
            and square[row][col-1] == square[row][col+word_len] == 0):
                word_count += 1
                f = 0
    # 세로로 word_len개 1이 있는지 확인
    for row in range(1, N-word_len+2):
        for col in range(1, N+1):
            flag = 1
            if square[row-1][col] == square[row+word_len][col] == 0:
                for i in range(word_len):
                    if square[row+i][col] != 1:
                        flag = 0
                        break
                if flag == 1:
                    word_count += 1
                    f = 1
    print("#%d %d" %(t, word_count))

                # flag = 1
                # print(row, col, flag)