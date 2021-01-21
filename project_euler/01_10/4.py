###########################
#  project_euler number 4 
#  by 김승현                
###########################

# Q. 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수


# 대칭수인지 체크하는 법
def DIY_palindrom(x):   
    check_num = str(x)
    while check_num:
        if check_num[0] == check_num[len(check_num)-1]:
            check_num = check_num[1:-1]
        else:
            return False
    return True
    
max_num = 0

#모든 3자리수의 곱을 check
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        new_num = num1 * num2
        if DIY_palindrom(new_num) and new_num > max_num:
            max_num = new_num

print(max_num)

