###########################
#  BaekJoon 10886번
#  by 김승현                
###########################

# Q. 0 = not cute / 1 = cute

a = 0
b = 0
for _ in range(int(input())):
    if input() == '1':
        a += 1
    else:
        b += 1
print("Junhee is cute!") if a > b else print("Junhee is not cute!")