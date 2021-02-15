###########################
#  BaekJoon 10162번
#  by 김승현                
###########################

# Q. 전자레인지

time = int(input())

a = time // 300
time %= 300
b = time // 60
time %= 60
c = time // 10
time %= 10

if time == 0:
    print(a, b, c)
else:
    print('-1')