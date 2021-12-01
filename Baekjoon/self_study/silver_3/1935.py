###########################
#  BaekJoon 1935번
#  by 김승현                
###########################

# Q. 후위 표기식2

N = int(input())
query = input()
stack = []
nums = dict()
for i in range(N):
    nums[chr(i+65)] = int(input())

for q in query:
    if q.isalpha():
        stack.append(nums[q])
    else:
        b, a = stack.pop(), stack.pop()
        if q == '+':
            stack.append(a+b)
        elif q == '-':
            stack.append(a-b)
        elif q == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)

ans = str(stack[0])

if '.' in ans:
    a, b = ans.split('.')
    b += '0'
    print(a + '.' + b[:2])
else:
    print(ans + '.00')
