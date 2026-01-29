'''

lis_a = [1,2,3,4,5,6,7,8,9,10]
lis_b = [11,12,13,14,15,16,17,18,19,20]

lis_c = lis_a + lis_b

print(sorted(lis_c))


'''

lis_a = [1, 3, 5, 7,9,10]
lis_b = [2, 4, 6, 8,9]

i = j = 0
lis_c = []

while i < len(lis_a) and j < len(lis_b):
    if lis_a[i] < lis_b[j]:
        lis_c.append(lis_a[i])
        i += 1
    else:
        lis_c.append(lis_b[j])
        j += 1

while i < len(lis_a):
    lis_c.append(lis_a[i])
    i += 1

while j < len(lis_b):
    lis_c.append(lis_b[j])
    j += 1

print(lis_c)
