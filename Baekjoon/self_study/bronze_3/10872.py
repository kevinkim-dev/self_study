###########################
#  BaekJoon 10872번
#  by 김승현                
###########################

# Q. 팩토리얼

fact = 1
for i in range(1, int(input())+1):
    fact *= i

print(fact)