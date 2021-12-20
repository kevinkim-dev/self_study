#########################
#  SWEA number 7490
#  by 김승현                
#########################

# Q. 0 만들기

def make_zero(num, N):
    todo = []
    for _ in range(N-1):
        todo.append(num%3)
        num //= 3
    num_list = list(range(N, 1, -1))
    cal = '1'
    for do in todo:
        if not do:
            cal += f'+{num_list.pop()}'
        elif do == 1:
            cal += f'-{num_list.pop()}'
        else:
            cal += str(num_list.pop())
    num_str = list(map(str, list(range(1, N+1))))
    if not eval(cal):
        new_cal = '1'
        for c in cal:
            if c == '1':
                continue
            if new_cal[-1] in num_str and c in num_str:
                new_cal += ' '
            new_cal += c
        return new_cal
    return False

T = int(input())

for _ in range(T):
    N = int(input())
    ans = []
    # 모든 경우의 수
    for i in range(3**(N-1)):
        is_zero = make_zero(i, N)
        if is_zero:
            ans.append(is_zero)
    # ascii순서로 sort
    ans.sort()
    for a in ans:
        print(a)
    print()