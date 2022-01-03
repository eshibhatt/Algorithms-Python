def linearSearch(arr,val):
    for i in range(0,len(arr)-1):
        if arr[i]==val:
            return i

arr=[1,4,73,2,3,5]
print(linearSearch(arr,2))