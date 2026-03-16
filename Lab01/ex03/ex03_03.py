def listtotuple(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
Tuple = listtotuple(numbers)
print("List:", numbers)
print("Tuple:",Tuple)
