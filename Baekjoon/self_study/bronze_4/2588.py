###########################
#  BaekJoon 2588번
#  by 김승현                
###########################

# Q. 곱셈

a = int(input())
b = int(input())

c = a * (b % 10)
print(c)
b //= 10
d = a * (b % 10)
print(d)
b //= 10
e = a * (b % 10)
print(e)
print(e*100 + d*10 + c)
