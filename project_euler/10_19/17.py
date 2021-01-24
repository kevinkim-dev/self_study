###########################
#  project_euler number 17
#  by 김승현                
###########################

# Q. 1부터 1000까지 영어로 썼을 때 사용된 글자의 개수는?

# 1) 100의 자리 -> 1의자리 + hundred and(10)
# 2) 10의 자리 -> 1일때와 아닐때
# 3) 1의 자리 -> 10의자리가 1일때와 아닐때

def check_one(x):
    if x in [1, 2, 6]:
        return 3
    elif x in [4, 5, 9]:
        return 4
    elif x in [3, 7, 8]:
        return 5
    else:
        return 0

def check_ten(x):
    if x in [4, 5, 6]:
        return 5
    elif x in [2, 3, 8, 9]:
        return 6
    elif x in [7]:
        return 7
    else:
        return 0

def check_special(x):
    if x in [0]:
        return 3
    elif x in [1, 2]:
        return 6
    elif x in [5, 6]:
        return 7
    elif x in [3, 4, 8, 9]:
        return 8
    elif x in [7]:
        return 9

def check_hun(x):
    if x in [1, 2, 6]:
        return 13
    elif x in [4, 5, 9]:
        return 14
    elif x in [3, 7, 8]:
        return 15
    else:
        return 0

letters = 0

for N in range(1, 1000):
    one = N % 10
    ten = (N // 10) % 10
    hun = N // 100
    letter = 0

    if ten == 1:
        letter += check_hun(hun)
        letter += check_special(one)  
    else:
        if ten == 0 and one == 0:
            letter += check_hun(hun)-3
        else:
            letter += check_one(one)
            letter += check_ten(ten)
            letter += check_hun(hun)
    
    letters += letter
    print(f"{N} needs {letter} letters to write, total {letters}")

letters += 11
print(f"1000 needs 11 letters to write, total {letters}")
print(letters)