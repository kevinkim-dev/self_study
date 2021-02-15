###########################
#  BaekJoon 10179번
#  by 김승현                
###########################

# Q. 쿠폰

t = int(input())

for i in range(t):
    print('$' + '%0.2f' %float(round((float(input())*0.8), 2)))