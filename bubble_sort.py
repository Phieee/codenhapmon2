def bubble_sort(sequence):
    n=len(sequence)
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if sequence[i]>sequence[j]:
                sequence[i],sequence[j]=sequence[j],sequence[i]
    return sequence
