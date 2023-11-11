a=float(input("Nhap so tuoi nguoi: "))
if a>=0:
    if a<=2:
        x=a*10.5
    if a>2:
        x=(2*10.5)+4*(a-2) 
    print("So tuoi cho tuong ung:",x)
else:
    print("Khong hop le")