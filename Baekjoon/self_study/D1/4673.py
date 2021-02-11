###########################
#  BaekJoon 4673번
#  by 김승현                
###########################

# Q. 셀프 넘버

def num_sum(x):
    _sum = 0
    while x > 0:
        _sum += x % 10 
        x //= 10
    return _sum


num_list = []
for i in range(1, 10001):
    num_list.append(i)

for n in range(1, 10001):
    created = n + num_sum(n)
    if created in num_list:
        num_list.remove(created)

for num in num_list:
    print(num)
