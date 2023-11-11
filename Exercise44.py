a=int(input("Nhap ngay (1-31): "))
b=int(input("Nhap thang (1-12): "))
print("Ngay",a,"thang",b)
if a==1 and b==1:
    print("New year's day")
elif a==1 and b==7:
    print("Canada day")
elif a==25 and b==12:
    print("Christmas day")
else:
    print("Ngay thang khong phai ngay le")