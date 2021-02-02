import base64

T = int(input())
for t in range(1, T+1):
    print(f"#{t} {base64.b64decode(input()).decode('utf-8')}")
