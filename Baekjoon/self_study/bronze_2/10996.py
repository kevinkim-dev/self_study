###########################
#  BaekJoon 10996번
#  by 김승현                
###########################

# Q. 별 찍기 - 21

n = int(input())

string = '* '*n

for i in range(n*2):
    s = string[i%2:n+i%2]
    if s:
        print(s)
