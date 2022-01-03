#using iteration
def binSearchI(arr,val):
    beg=0
    last=len(arr)-1
    while beg<=last:
        mid=int((beg+last)/2)
        if val==arr[mid]:
            return True
        #shifting mid acc to comparison
        elif val>arr[mid]:
            beg=mid+1
        elif val<arr[mid]:
            last=mid-1
    else:
        return False

#using recursion
def binSearchR(arr,val,beg,last):
    mid=int((beg+last)/2)
    #base cases
    if beg>last:
        return -999
    elif val==arr[mid]:
        return True
    #recursive cases 
    elif val>arr[mid]:
        beg=mid+1 #segment becomes 2nd half
        return binSearchR(arr,val,beg,last)
    elif val<arr[mid]:
        last=mid-1 #segment becomes 1st half
        return binSearchR(arr,val,beg,last)

nums= [2, 1, 5, 63, 87, 283, 4, 0]
print(binSearchI(nums,87))
print(binSearchR(nums,87,0,7))
