#########################
#  SWEA number 11789
#  by 김승현                
#########################

# Q. bit연산 - 연습문제1

for t in range(1, int(input())+1):
    string = input()
    nums = []
    for i in range(len(string)//7):
        bi_num = string[i*7:i*7+7]
        num = 0
        for i in range(len(bi_num)):
            if bi_num[-i-1] == '1':
                num += 2 ** i
        nums.append(str(num))
    nums = ', '.join(nums)
    print("#%d %s" %(t, nums))