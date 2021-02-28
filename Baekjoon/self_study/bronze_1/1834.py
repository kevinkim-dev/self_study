###########################
#  BaekJoon 1834번
#  by 김승현                
###########################

# Q. 나머지와 몫이 같은 수

num = int(input())
_sum = 0
for n in range(1, num):
    _sum += n*(1+num)
print(_sum)