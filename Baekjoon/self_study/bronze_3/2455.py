###########################
#  BaekJoon 2455번
#  by 김승현                
###########################

# Q. 지능형 기차

train = 0
train_list = []
for _ in range(4):
    a, b = map(int, input().split())
    train_list.append(train -a + b)
    train = train_list[-1]
print(max(train_list))