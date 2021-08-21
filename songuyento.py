import math
n = int(input("Nhập số nguyên dương n:"))
c=math.sqrt(n)
i=1
d=0
while True:
    if n==1:
        break
    elif n%i==0:
        d=d+1
    i=i+1
    if i>c:
        break
if d==1:
    print("n là số nguyên tố")
else:
    print("n không phải là số nguyên tố")
