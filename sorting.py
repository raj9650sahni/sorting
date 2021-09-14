
'''
low = Starting index,  high = Ending index 
quickSort(arr, low, high)

    if (low < high)
    
        temp is partitioning index, arr[temp] is not at bright place
        temp = partition(arr, low, high);

        quickSort(arr, low, temp - 1); --- Before temp
        quickSort(arr, temp + 1, high); --- After temp
    


'''



def qs(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


a1 = [3, -2, -1, 0, -6, 4, 1,-8]
n = len(a1)


qs(a1,0,n-1)
print(a1)
