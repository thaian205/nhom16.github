a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:  
    pass
    if (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
        print("Tam giac can")
    elif(a==b) and (b==c) and (c==a):
        print("Tam giac deu")
    else:
        print("Tam giac thuong")
else:
    print("Khong hop le")