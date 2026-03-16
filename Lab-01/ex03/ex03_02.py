def Dao(chuoi):
    return chuoi[::-1]
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

dao = Dao(numbers)
print("Sau khi đảo: ",dao)
