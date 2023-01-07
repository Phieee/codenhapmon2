def sequential_search(x,sequence):
    n=len(sequence)
    k=-1
    for i in range(0,n,1):
        if sequence[i]==x:
            k=i
            break
    return k
sequence=[]
n=int(input("Nhap so phan tu="))
for i in range(0,n):
    a=int(input())
    sequence.append(a)
x=int(input("Nhap gia tri can tim x= "))
print("Vi tri can tim la:",i)
