
import math
t=int(input())
for _ in range(t):
    n=int(input())
    is_prime = True
    if n<=1:
        is_prime=False
    elif n == 2:
        is_prime = True
    elif n%2 == 0:
        is_prime = False
    else:
        limit = int(math.sqrt(n))
        for i in range(3, limit+1,2):
            if n%i ==0:
                is_prime= False
                break

    if is_prime:
        print("Yes")
    else:
        print("No")
        
        
