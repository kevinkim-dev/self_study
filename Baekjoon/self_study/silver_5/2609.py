###########################
#  BaekJoon 2609번
#  by 김승현                
###########################

# Q. 최대공약수와 최소공배수

a, b = map(int, input().split())
ta, tb = a, b
while ta != tb:
    if ta > tb:
        ta = ta - tb
    else:
        tb = tb - ta
print(ta)
print(a*b//ta)
