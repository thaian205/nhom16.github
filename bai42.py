N= {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}
a = float(input("Nhập tần số (tính bằng Hz): "))

for i, key in N.items():
    if abs(a - key) <= 1:
        print(f"Tần số tương ứng với nốt nhạc {i}.")
        break
else:
    print("Tần số nằm ngoài phạm vi của các nốt đã biết")