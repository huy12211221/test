a = int(input("Nhập giá trị="))
x=0#biến để lấy phần dư
d=0 #d là output
while a>0:
    x=a%10
    d=d*10+x
    a=a//10
print(d)