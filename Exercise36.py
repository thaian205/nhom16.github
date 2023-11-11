k = input("Nhập một chữ cái trong bảng chữ cái: ")

if k in ['a', 'e', 'i', 'o', 'u']:
    print("Chữ cái được nhập là một nguyên âm.")
elif k == 'y':
    print("Đôi khi y là nguyên âm, đôi khi y là phụ âm.")
else:
    print("Chữ cái được nhập là một phụ âm.")