#########################
#  SWEA number 11791
#  by 김승현                
#########################

# Q. 연습문제 3

passwords = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

for t in range(1, int(input())+1):
    string = input()
    bi_num = ''
    for s in string:
        bi_num += bin(int(s, 16))[2:].zfill(4)
    i = 0
    while True:
        i += 1
        if bi_num[-i] == '1':
            break
    bi_num = bi_num[:-i+1]
    bi_num = bi_num[len(bi_num)%6:]
    nums = []
    for i in range(len(bi_num)//6):
        password = bi_num[i*6:i*6+6]
        nums.append(str(passwords.index(password)))
    nums = ', '.join(nums)
    print("#%d %s" %(t, nums))