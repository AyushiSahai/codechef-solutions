try:
    n=int(input())
except:
    exit()
score_p1=0
score_p2=0
winner=0
max_lead=0

for _ in range(n):
    p1,p2=map(int,input().split())
    score_p1+=p1
    score_p2+=p2 
    curr_diff=score_p1 - score_p2
    if abs(curr_diff)>max_lead:
        max_lead=abs(curr_diff)
        if curr_diff > 0:
            winner=1 
        else:
            winner=2 
print(winner,max_lead)            
