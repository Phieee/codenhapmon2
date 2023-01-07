def giai_thua(n):
    if n==1:
        return 1
    else:
        return n*giai_thua(n-1)
