import sys
sys.stdin = open("input.txt")


list_n = []
for line in sys.stdin:
    input_txt = line.split()
    list_n.append(input_txt)

print(list_n)