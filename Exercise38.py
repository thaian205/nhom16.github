month=int(input("Nhap mot thang bat ki: "))
if month in (1,3,5,7,8,10,12):
    print("Thang",month,"co 31 ngay")
elif month==2:
    print("Thang",month,"co 28 hoac 29 ngay")
else:
    print("Thang",month,"co 30 ngay")