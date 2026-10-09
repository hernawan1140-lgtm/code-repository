def hitung_mundur(n):
    if n==0:
        return
    print(n)
    hitung_mundur(n-2)


hitung_mundur(9999999)