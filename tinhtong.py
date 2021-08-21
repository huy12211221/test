a = int(input("Nhập giá trị đầu="))
b = int(input("Nhập giá trị cuối="))
num=0
c=a
for i in range (a,b+1):
    num=num+c
    c=c+1
print("Tổng=",num)
