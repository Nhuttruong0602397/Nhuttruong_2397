def xoa(dic,key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

Mdic={'a':1,'b':2,'c':3,'d':4}
keydel = 'b'
result = xoa(Mdic,keydel)
if result:
    print("Phần tử đã được xoá:",Mdic)
else:
    print("Không tìm thấy phần tử")