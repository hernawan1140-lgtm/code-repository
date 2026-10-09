def sapa(nama):
    print('Halo ',nama,',selamat datang.')

def bilangan(a,b):
    s = ''
    for i in range(a,b+1,1):
        s += str(i)+' '
    print(s)

sapa(input("masukan nama :"))
bilangan(2,9)