def quick_sort(list):
    if(len(list)<=1):
        return list
    else:
        pivot = list[0]
        lesser = [x for x in list[1: ] if x  <=pivot]
        greater = [ x for x in list[1:] if x  > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

list = [1,6,36,8,4,44,64,43]

mylist = quick_sort(list)
print(mylist)
