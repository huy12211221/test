A = input("Nhập chuỗi: ")
d=len(A)//2
if len(A)%2==0:
    for b in range (1,d+1):
        e=0#số lần lặp
        for i in range (0,d):
            if A[:b]==A[b:b*2]:
                e=e+1
            else:
                break
        if e==d:
            print("Chuỗi lặp đi lặp lại bởi chuỗi",A[:b],"và lặp lại",e,"lần")
            break
    if e==0:
        print("Không phải chuỗi lặp")
else:
    print("Không phải chuỗi lặp")