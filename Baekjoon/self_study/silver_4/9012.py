###########################
#  BaekJoon 9012번
#  by 김승현                
###########################

# Q. 괄호

def check_bracket(string):
    open_cnt = 0
    for char in string:
        if char == '(':
            open_cnt += 1
        if char == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return 'NO'
    return 'NO' if open_cnt else 'YES'

for _ in range(int(input())):
    string = input()
    open_cnt = 0
    print(check_bracket(string))