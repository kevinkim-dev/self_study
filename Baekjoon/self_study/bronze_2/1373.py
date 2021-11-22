###########################
#  BaekJoon 1373번
#  by 김승현                
###########################

# Q. 2진수 8진수

bi_num = input()


bi_num = '0'*((3 - len(bi_num)%3)%3) + bi_num

ans = ''

for i in range(len(bi_num)//3):
    tmp = bi_num[3*i: 3*i+3]
    tmp = str(int(tmp[0])*4 + int(tmp[1])*2 + int(tmp[2]))
    ans += tmp

print(ans)