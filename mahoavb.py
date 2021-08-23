a= input("Nhập lock để mã hóa văn bản, nhập unlock để giải mã văn bản: ")
def pro(sb,se):
    k=int(input("Nhập key: "))
    b=k
    for i in range (0,k):
        k=k-1
        sb+=Q[k]
    print(sb,end='')
    e=len(Q)
    for i in range (b,e):
        e=e-1
        se+=Q[e]
    print(se)
#main
if a=="lock":
    Q=input("Nhập văn bản cần mã hóa: ")
    pro('','')
elif a=="unlock":
    Q=input("Nhập văn bản cần giả mã: ")
    pro('','')
