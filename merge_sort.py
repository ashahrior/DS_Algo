def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = mergeSort(arr[:mid])
        R = mergeSort(arr[mid:])
		
        arr = []
		
        while len(L)>0 and len(R)>0:
            if L[0]<R[0]:
                arr.append(L[0])
                L.pop(0)
            else:
                arr.append(R[0])
                R.pop(0)
        if len(L)>0:
            arr.extend(L)
        if len(R)>0:
            arr.extend(R)
    return arr

a = [12, 11, 13, 5, 6, 7]
print(*a,end= ' -> ')
print(*(mergeSort(a)))
