#author CJP 01/12/2022

def even_number(lst):
    for i, v in enumerate(lst): 
            if lst[i] % 2 == 0:
                print(v)
                
even_number([3,6,8,10])
