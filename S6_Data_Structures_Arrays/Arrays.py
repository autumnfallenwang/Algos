def reverse(s):
    return s[::-1]

def mergeSortedArrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    a1 = arr1[0]
    a2 = arr2[0]
    mergeArray = []
    while a1 != None or a2 != None:
        if a1 == None:
            mergeArray.append(a2)
            arr2.pop(0)
            a2 = arr2[0] if len(arr2) > 0 else None
        elif a2 == None:
            mergeArray.append(a1)
            arr1.pop(0)
            a1 = arr1[0] if len(arr1) > 0 else None
        elif a1 < a2:
            mergeArray.append(a1)
            arr1.pop(0)
            a1 = arr1[0] if len(arr1) > 0 else None
        else:
            mergeArray.append(a2)
            arr2.pop(0)
            a2 = arr2[0] if len(arr2) > 0 else None
    return mergeArray


if __name__ == '__main__':
    # test mergeSortedArrays
    arr1 = [0, 3, 4, 31]
    arr2 = [4, 6, 30]
    print(mergeSortedArrays(arr1, arr2))