###########################
#  BaekJoon 12757번
#  by 김승현                
###########################

# Q. 전설의 JBNU

import sys

input = sys.stdin.readline

def find(key):
    s, e = 0, l - 1
    while e - s > 1:
        m = (s + e)//2
        if keys[m] > key:
            e = m
        else:
            s = m
    small_key, large_key = keys[s], keys[e]
    small_key_dif, large_key_dif = abs(small_key - key), abs(large_key - key)
    if min(small_key_dif, large_key_dif) > K:
        return -1
    if small_key_dif == large_key_dif:
        if small_key == large_key:
            return small_key
        return -2
    elif small_key_dif < large_key_dif:
        return small_key
    else:
        return large_key

N, M, K = map(int, input().split())

keys, l, database = [], 0, dict()

for _ in range(N):
    k, v = map(int, input().split())
    keys.append(k)
    database[k] = v
    l += 1

keys.sort()

for _ in range(M):
    command = input()
    # 시간초과의 원인
    if command[0] == '1':
        c, k, v = map(int, command.split())
        database[k] = v
        keys.append(k)
        keys.sort()
        l += 1
    elif command[0] == '2':
        c, k, v = map(int, command.split())
        if k in keys:
            database[k] = v
        else:
            n_k = find(k)
            if n_k in (-1, -2):
                continue
            database[n_k] = v
    else:
        c, k = map(int, command.split())
        if k in keys:
            print(database[k])
        else:
            n_k = find(k)
            if n_k == -1:
                print(-1)
            elif n_k == -2:
                print('?')
            else:
                print(database[n_k])