###########################
#  BaekJoon 9046번
#  by 김승현                
###########################

# Q. 복호화

for _ in range(int(input())):
    string = input()
    chars = [0]*26
    for s in string:
        if s == ' ':
            continue
        chars[ord(s)-97] += 1
    e = max(chars)
    ans = []
    for i in range(26):
        if chars[i] == e:
            ans.append(i)
    if len(ans) == 1:
        print(chr(ans[0]+97))
    else:
        print('?')
