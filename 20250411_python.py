# def makeFishShapeBun(taste) :
#     print(f"{taste}맛 붕어빵 완성!!!")
#     print("맛있게 드세요")

# makeFishShapeBun("팥")
# makeFishShapeBun("슈크림")

# x = 10

# def example():
#     x = 20
#     print(x)  # 20

# example()
# print(x)  # 10

# def for10(string):
#     for i in range(10):
#         print(string)

# for10("HelloWorld")

def sortList(returnType, func, *args) :  # !!함수 재사용성 극대화!!
    return returnType(func(args))

def quick_sort(arr) :
    # 출처 : https://www.daleseo.com/sort-quick/
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print(sortList(tuple, sorted, 1,6,3,4,327490851980709851))
print(sortList(tuple, quick_sort, 25,32662,24,21,1,33,234,2,6,524,4,2,42))  # sorted 안씀!

