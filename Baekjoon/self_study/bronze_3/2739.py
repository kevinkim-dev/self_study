###########################
#  BaekJoon 2739번
#  by 김승현                
###########################

# Q. 구구단

n = int(input())

for i in range(1, 10):
    print("%d * %d = %d" %(n, i, n*i))