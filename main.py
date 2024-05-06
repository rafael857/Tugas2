def cetak_kuadrat_ganjil(n):
    for i in range(n):
        if i == 0 or i % 2 != 0:
            print(i ** 2, end=" ")

n = int(input("Masukkan nilai n: "))
print("Nilai kuadrat bilangan ganjil untuk n =", n, "adalah:")
cetak_kuadrat_ganjil(n)


#artinya jika bilangan negatif yang di masukan maka tidak akan running, dimulai dari i= 0 
#i< dari n maksimal dari i selalu n-1
