def giai_thua(n):
    if n==1:
        return 1
    else:
        return n*giai_thua(n-1)
n=int(input("Nhap so n can tinh giai thua="))
print(n,"!=",giai_thua(n))
