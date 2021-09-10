###########################
#  BaekJoon 1267번
#  by 김승현                
###########################

# Q. 핸드폰 요금

phone = int(input())
phone_list = list(map(int, input().split()))
a, b = 0, 0
for _ in range(phone):
    t = phone_list.pop()
    a += t // 30 + 1
    b += t // 60 + 1
a *= 10
b *= 15
if a < b:
    print('Y', a)
elif a > b:
    print('M', b)
else:
    print('Y M', a)