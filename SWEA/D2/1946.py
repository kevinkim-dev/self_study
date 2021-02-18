#########################
#  SWEA number 1946
#  by 김승현                
#########################

# Q. 간단한 압축 풀기

for t in range(1, int(input())+1):
    print("#%d" %t)
    docu = ''
    for n in range(int(input())):
        a, b = input().split()
        b = int(b)
        docu += a*b
    while len(docu) > 10:
        print(docu[:10])
        docu = docu[10:]
    if docu:
        print(docu)