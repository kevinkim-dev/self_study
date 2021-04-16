import sys
sys.stdin = open("input.txt", "r")


def calc(bin_code):
    numcode = []
    for i in range(8):
        numcode.append(enc[bin_code[i * 7:(i + 1) * 7]])
 
    if (sum(map(int, numcode[::2])) * 3 + sum(map(int, numcode[1::2]))) % 10:
        return 0
 
    return sum(numcode)
 

enc = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    data_set = set()
    code_set = set()
    result = 0
    for _ in range(N):
        data = input().strip('0')
        if data in data_set:
            continue
        data_set.add(data)
 
        if data:
            bin_data = bin(int(data, 16))[2:].strip('0')
            while bin_data:
                mul = 1
                while True:
                    if bin_data[-7*mul:][::mul] in enc.keys():
                        bin_code = bin_data.zfill(56 * mul)[-mul * 7 * 8:][::mul]
                        for i in range(8):
                            if bin_code[i*7:(i+1)*7] not in enc.keys():
                                break
                        else:
                            break
                    mul += 1
                if bin_code not in code_set:
                    result += calc(bin_code)
                    code_set.add(bin_code)
                bin_data = bin_data.replace(bin_data[-mul*7*8:], '0').rstrip('0')
 
    print('#%d %d' % (t, result))