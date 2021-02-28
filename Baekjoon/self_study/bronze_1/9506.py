###########################
#  BaekJoon 9506번
#  by 김승현                
###########################

# Q. 약수들의 합

def check_div(x):
    for i in range(2, x):
        if x % i == 0:
            div_list.append(i)
    if sum(div_list) == x:
        return True
    else:
        return False

n = int(input())

while n != -1:
    div_list = [1]
    if check_div(n):
        for i in range(len(div_list)):
            div_list[i] = str(div_list[i])
        ans = ' + '.join(div_list)
        print("%d = %s" %(n, ans))
    else:
        print("%d is NOT perfect." %n)
    n = int(input())