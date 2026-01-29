def max_elem(lis):
    num = lis[0]  
    for i in lis:
        if i > num:
            num = i
    return num

lis = [1,2,4,5,6,8,5,5,8,9,13,3]
print("Max element of list is:", max_elem(lis))
