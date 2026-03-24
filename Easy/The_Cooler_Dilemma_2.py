t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    n=(y - 1) // x
    if n<y:
        print(n)
    else:
        print(0)
