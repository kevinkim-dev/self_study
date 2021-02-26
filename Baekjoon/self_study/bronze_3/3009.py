###########################
#  BaekJoon 3009번
#  by 김승현                
###########################

# Q. 네 번째 점

X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for xs in X:
    if X.count(xs) == 1:
        print(xs, end=' ')
for ys in Y:
    if Y.count(ys) == 1:
        print(ys)