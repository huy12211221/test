a= input("Nhập chuỗi: ")
c=len(a)
b=''
d=0
for i in range (0,c//2):
    if a[i]==a[c-1-i]:
        d=d+1
if d==c//2:
    print("Chuỗi đối xứng")
else:
    print("Chuỗi không đối xứng")
