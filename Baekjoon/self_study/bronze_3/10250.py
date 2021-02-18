###########################
#  BaekJoon 10250번
#  by 김승현                
###########################

# Q. ACM 호텔

for t in range(1, int(input())+1):
    floor, width, num = map(int, input().split())
    a = num % floor
    b = (num // floor)+1
    if a == 0:
        a = floor
        b -= 1
    a= str(a)
    b = str(b).rjust(2, '0')
    print(a+b)
