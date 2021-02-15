###########################
#  BaekJoon 1550번
#  by 김승현                
###########################

# Q. 16진수

string = input()
length = len(string)
num = 0

for i in range(length):
    if ord(string[i]) >= 65 and ord(string[i]) <= 90:
        num += (ord(string[i])-55)*(16 ** (length-1-i))
    else:
        num += int(string[i])*(16 **(length-1-i))

print(num)