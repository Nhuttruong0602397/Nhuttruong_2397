def dem(lst):
    c = {}
    for i in lst :
        if i in c:
            c[i]+=1
        else:
            c[i] =1
    return c
instr = input("nhập danh sách cách nhau bằng khỏng trắng")
word = instr.split()
S = dem(word)
print("Số lần xuất hiện của các phần tử:",S)