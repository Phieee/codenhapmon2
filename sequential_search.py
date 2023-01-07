def sequential_search(x,sequence):
    n=len(sequence)
    k=-1
    for i in range(0,n,1):
        if sequence[i]==x:
            k=i
            break
    return k
