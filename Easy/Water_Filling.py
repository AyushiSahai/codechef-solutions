t=int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    if a==0 and b==0 or b==0 and c==0 or c==0 and a==0 or a==0 and b==0 and c==0:
        print("water filling time")
    else:
        print("not now")
