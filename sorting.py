
'''
low = Starting index,  high = Ending index 
quickSort(arr, low, high)
{
    if (low < high)
    {
        temp is partitioning index, arr[temp] is not at bright place
        temp = partition(arr, low, high);

        quickSort(arr, low, temp - 1); --- Before temp
        quickSort(arr, temp + 1, high); --- After temp
    }
}

'''



def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] 
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return i+1

def quick(arr,low,high):
   if low < high:
      temp = partition(arr,low,high)
      quick(arr, low, temp-1)
      quick(arr, temp+1, high)

arr = [3,10,4,7,1,9,45,87]
n = len(arr)
quick(arr,0,n-1)
print(arr)
