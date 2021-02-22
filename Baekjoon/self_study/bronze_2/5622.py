###########################
#  BaekJoon 5622번
#  by 김승현                
###########################

# Q. 다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

string = input()
cnt = 0

for char in string:
    for n in range(8):
        if char in dial[n]:
            cnt += n + 3
print(cnt)