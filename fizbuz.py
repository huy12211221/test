a= int(input("Nhập giá trị đầu="))
b= int(input("Nhập giá trị cuối="))
if a<b:
    for i in range (a,b):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
else:
    print("Giá trị đầu phải nhỏ hơn giá trị cuối")