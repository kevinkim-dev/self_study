###########################
#  BaekJoon 10814번
#  by 김승현                
###########################

# Q. 나이순 정렬

dic = dict()
for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    if dic.get(age):
        dic[age].append(name)
    else:
        dic[age] = [name]

for key in sorted(dic.keys()):
    for name in dic[key]:
        print('%d %s' %(key, name))