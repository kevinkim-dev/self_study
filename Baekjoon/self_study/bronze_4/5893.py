###########################
#  BaekJoon 5893번
#  by 김승현                
###########################

# Q. 17배

binary = input()
deci = 0
for i in range(len(binary)):
    deci += int(binary[len(binary)-i-1])* (2 ** i)
deci *= 17

print(format(deci, 'b'))