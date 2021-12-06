###########################
#  BaekJoon 4949번
#  by 김승현                
###########################

# Q. 균형잡힌 세상

def check_bracket(string):
    stack = []
    for s in string:
        if s in ('(', '['):
            stack.append(s)
        elif s in (')', ']'):
            if not stack:
                return 'no'
            bracket = stack.pop()
            if s == bracket_dict[bracket]:
                continue
            return 'no'
    if not stack:
        return 'yes'
    else:
        return 'no'


bracket_dict = { '(': ')', '[': ']'}

while True:
    string = input()
    if string == ".":
        break
    print(check_bracket(string))