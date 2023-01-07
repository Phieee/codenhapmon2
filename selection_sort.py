def selection_sort(seq):
    n=len(seq)
    for i in range (0,n-1,1):
        min_index=i
        for j in range(i+1,n,1):
            if seq[j]<seq[min_index]:
                min_index=j
        seq[i],seq[min_index]=seq[min_index],seq[i]
    return seq
