def buscaSeq(list, item):
    pos = 0
    x = False

    while pos<len(list) and not x:
        if list[pos] == item:
            x = True
        else:
            pos += 1
    return x


list = [5,6,8,12,1,5,7]
print(buscaSeq(list, 8))
print(buscaSeq(list, 13))