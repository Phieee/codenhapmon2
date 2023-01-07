def binary_search(x,sequence):
    n=len(sequence)
    left=0
    right=n-1
    mid=int((left+right)/2)
    while (left<right) and (x!=sequence[mid]):
        if x<sequence[mid]:
            right=mid-1
        else:
            left=mid+1
        mid=int((left+right)/2)
    if x==sequence[mid]:
        return mid
    else:
        return -1
