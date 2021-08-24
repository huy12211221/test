A = input("Nhập chuỗi: ")
n=len(A)
d=n//2
for b in range (1,d+1):
    e=0
    f=n//b#số lần lặp để xét chuỗi con
    g=0
    for i in range (0,f):
        if g==0:
            z=b
        if A[:b]==A[z:z+b]:
            e=e+1
            g+=1
        else:
            if A[z:z+b]!="":
                e=0
                break
            else:
                break
        z+=b
    if e==f-1:
        print("Chuỗi lặp đi lặp lại bởi chuỗi",A[:b],"và lặp lại",n/b,"lần")
        break
if e==0:
    print("Không phải chuỗi lặp")