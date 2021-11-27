###########################
#  BaekJoon 1110번
#  by 김승현                
###########################

# Q. 더하기 사이클

num = int(input())
count = 0
now_num = num
while True:
    count += 1
    now_num = (now_num % 10)*10 + (now_num % 10 + now_num // 10) % 10
    if now_num == num:
        break

print(count)