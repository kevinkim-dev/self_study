###########################
#  BaekJoon 1032번
#  by 김승현                
###########################

# Q. 명령 프롬포트

length = int(input())
arr = [0]*length
for i in range(length):
    arr[i] = input()

ans = arr[0]
word_len = len(ans)
for i in range(word_len):
    flag = 1
    for j in range(1, length):
        if ans[i] == arr[j][i]:
            pass
        else:
            flag = 0
            ans += '?'
            break
    if flag == 1:
        ans += ans[i]
print(ans[word_len:])