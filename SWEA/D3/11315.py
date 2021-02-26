#########################
#  SWEA number 11315
#  by 김승현                
#########################

# Q. 오목 판정

for t in range(1, int(input())+1):
    n = int(input())
    box = [input() for _ in range(n)]
    
    flag = 'NO'
    for array in box, zip(*box):
        for arr in array:
            temp = ''
            for char in arr:
                temp += char
            temp_array = temp.split('.')
            for element in temp_array:
                if len(element) >= 5:
                    flag = 'YES'
                    break
    cross = ''
    rev_cross = ''
    for i in range(n-4):
        for j in range(i, n):
            cross += box[j-i][j]
            rev_cross += box[n-j-1+i][j]
        cross_array = cross.split('.')
        rev_cross_array = rev_cross.split('.')
        for arr in cross_array, rev_cross_array:
            for element in arr:
                if len(element) >= 5:
                    flag = 'YES'
                    break
    for i in range(1, n-4):
        for j in range(n-i):
            cross += box[j+i][j]
            rev_cross += box[n-j-1-i][j]
        cross_array = cross.split('.')
        rev_cross_array = rev_cross.split('.')
        for arr in cross_array, rev_cross_array:
            for element in arr:
                if len(element) >= 5:
                    flag = 'YES'
                    break
    print("#%d %s" %(t, flag))