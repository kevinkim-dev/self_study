###########################
#  BaekJoon 1475번
#  by 김승현                
###########################

# Q. 방 번호

N = int(input())

num_list = [0]*10

while N:
    num = N%10
    if num == 6:
        num_list[9] += 1
    else:
        num_list[N%10] += 1
    N //= 10

print(max(max(num_list[:9]), num_list[9]//2 + bool(num_list[9]%2)))
