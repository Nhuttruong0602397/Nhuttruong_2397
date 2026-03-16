def truycap(Tuple):
    first = Tuple[0]
    last = Tuple[1]
    return first,last
intuple = eval(input("Nhập tuple(1, 2, 3):"))
first, last = truycap(intuple)
print("Phần tử đầu:",first)
print("Phần tử cuối:",last)

