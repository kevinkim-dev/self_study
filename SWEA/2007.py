#########################
#  SWEA number 2007
#  by 김승현                
#########################

# Q. 패턴 마디의 길이

T = int(input())

for t in range(1, T+1):
    string = input()
    for i in range(1, len(string)+1):
        flag = 1
        test = string
        length = i
        pattern = string[:i]
        while len(test) >= i:
            if pattern == test[:i]:
                test = test[i:]
            else:
                flag = 0
                break
        if flag == 1:
            print("#%d %d" %(t, length))
            break









    # flag = 1
    # while True:
    #     length += 1 
    #     for i in range(1, len(string)//length - 1):
    #         if string[:length] == string[length*(i):length*(i+1)]:
    #             continue
    #         else:
    #             flag = 0
    #             break
            

        