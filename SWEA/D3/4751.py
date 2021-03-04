#########################
#  SWEA number 4751
#  by 김승현                
#########################

# Q. 다솔이의 다이아몬드 장식

for t in range(1, int(input())+1):
    string = input()
    N = len(string)
    out = "." 
    mid = "." 
    inside = "#"
    for char in string:
        out += ".#.."
        mid += "#.#."
        inside += ".%s.#" %char
    print(out, mid, inside, mid, out, sep='\n')