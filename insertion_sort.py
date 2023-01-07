def insertion_sort(sequence):
    n=len(sequence)
    for i in range(1,n,1):
        k=sequence[i];
        j=i;
        while k<sequence[j-1]:
            sequence[j]=sequence[j-1]
            j=j-1
        if (j<0):
            j=0;
            sequence[j]=k
    return sequence
