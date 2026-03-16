t=int(input())
for _ in range(t):
  n,a,b = map(int, input().split())
  p=n.bit_length()-1
  r=(p*a)+((p-1)*b)
  print(r)

OR

rounds = 0
temp_n = n
while temp_n > 1:
    temp_n //= 2
    rounds += 1
