
#----------------------------------------
# WITHOUT DUPLICATES -> DEFAULT OVERWRITE
#----------------------------------------

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}

dict3 = {}

for key in dict1.keys():
    dict3[key] = dict1[key]

for key in dict2.keys():
    dict3[key] = dict2[key]

print(dict3)


#----------------------------------------
# WITH DUPLICATES -> COMBINING
#----------------------------------------


dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "e": 5, "b": 6}

dict3 = {}

for key in dict1.keys():
    dict3[key] = dict1[key]

for key in dict2.keys():
    if key in dict3:
        dict3[key] = [dict3[key],dict2[key]]
    else:
        dict3[key] = dict2[key]

print(dict3)
