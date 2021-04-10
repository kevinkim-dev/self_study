#########################
#  SWEA number 1232
#  by 김승현                
#########################

# Q. 사칙연산

def calculate(idx):
    if len(tree[idx]) == 1:
        return int(tree[idx][0])
    else:
        for i in (1, 2):
            tree[idx][i] = int(tree[idx][i])
        if tree[idx][0] == '+':
            return calculate(tree[idx][1]) + calculate(tree[idx][2])
        elif tree[idx][0] == '-':
            return calculate(tree[idx][1]) - calculate(tree[idx][2])
        elif tree[idx][0] == '*':
            return calculate(tree[idx][1]) * calculate(tree[idx][2])
        else:
            return calculate(tree[idx][1]) / calculate(tree[idx][2])


for t in range(1, 11):
    N = int(input())
    tree = list(input().split()[1:] for _ in range(N))
    tree = [0] + tree
    ans = int(calculate(1))
    print("#%d %d" %(t, ans))
    