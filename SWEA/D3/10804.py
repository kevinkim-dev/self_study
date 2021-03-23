#########################
#  SWEA number 10804
#  by 김승현                
#########################

# Q. 문자열의 거울상

char = ['b', 'p', 'd', 'q']

for t in range(1, int(input())+1):
    string = input()
    new_string = ''
    for i in range(len(string)-1, -1, -1):
        new_string += char[(char.index(string[i])+2) % 4]
    print("#%d %s" %(t, new_string))