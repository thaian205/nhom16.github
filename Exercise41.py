a = input("Nhap quang am: ")
b = a[0]
c = int(a[1])
N = {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.00, "A": 440.00, "B": 493.88}
QA = N[b] / (pow(2, 4 - c))
print("Tan so quang am la", QA)