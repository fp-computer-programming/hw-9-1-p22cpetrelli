#author CJP 01/13/2022
def find_thing(lst,y):
    index = -1
    for i, v in enumerate(lst):
        if v == y:
            index = i
            break
    return index

print(find_thing([1,2,3,7,5,3,7,8,7],3))