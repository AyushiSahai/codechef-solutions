t=int(input())
for _ in range(t):
    n=int(input())
    count_start38=0 
    count_ltime108 = 0 
    codes=input().split()
    for code in codes:
        if code =="START38":
            count_start38+=1 
        elif code =="LTIME108":
            count_ltime108+=1
    print(count_start38,count_ltime108)
