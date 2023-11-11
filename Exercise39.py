n = {"Búa khoan": 130,
     "Máy cắt cỏ dùng gas": 106,
     "Đồng hồ báo thức": 70,
     "Căn phòng im ắng": 40}

db = int(input("Nhập mức decibel: "))

if db == n["Búa khoan"]:
    print("Búa khoan")
elif db == n["Máy cắt cỏ dùng gas"]:
    print("Máy cắt cỏ dùng gas")
elif db == n["Đồng hồ báo thức"]:
    print("Đồng hồ báo thức")
elif db == n["Căn phòng im ắng"]:
    print("Căn phòng im ắng")
elif 40< db < 70 :
        print("Âm thanh nằm giữa Căn phòng im ắng và đồng hồ báo thức")
elif 70< db < 106 :
    print('Âm thanh nằm giữa đồng hồ báo thức và máy cắt cỏ dùng gas')   
elif 106 < db < 130 :
    print('Âm thanh nằm giữa Búa khoan và máy cắt cỏ dùng gas')
else:
    print('Nằm ngoài âm thanh trong bảng')