import random
c=0
d=3
n = random.randint(1,10)
while True:
    if c==3:
        print("Bạn đã thua cuộc,số đúng là:",n)
        break
    a = int(input("Nhập số:"))
    if a==n:
        print("Bạn đã đoán đúng")
        break
    else:
        c=c+1
        d=d-1
        if a>n:
            print("Bạn đã đoán sai,số bạn đoán lớn hơn số đúng,bạn còn",d,"lượt đoán")
        else:
            print("Bạn đã đoán sai,số bạn đoán nhỏ hơn số đúng,bạn còn",d,"lượt đoán")

