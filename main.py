import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

plt.ion() #digunakan untuk mengaktifkan mode interaktif matplotlib

class Barang:
    def __init__(item, nama, harga):
        item.nama = nama
        item.harga = harga

def bacaBarang():
        try:
            jumlah = int(input("Masukkan jumlah barang : "))
            if jumlah <= 0:
                print("jumlah barang tidak boleh 0!")
                return [],0
        except ValueError:
            print("Inputan tidak valid. Masukkan harus berupa angka ")
            return[],0
        
        barang = [None] * jumlah
        for i in range(jumlah):
            print(f"\nBarang #{i + 1}")
            nama = input("Nama: ").strip()
            if not nama:
                print("Inputan nama tidak valid. Gunakan 'NN' sebagai default")
                nama = "NN"
            try:
                harga = float(input("Harga: "))
                if harga <= 0:
                    raise ValueError
            except ValueError:
                print("Inputan harga tidak valid. Gunakan 0 sebagai default.")
                harga = 0.0
            
            barang[i] = Barang(nama, harga)

        return barang, jumlah
    
    
def algoritmaMergeSortRekursif(barang, kiri, kanan):
        if kiri >= kanan:
            return
        
        tengah = (kiri + kanan) // 2
        algoritmaMergeSortRekursif(barang, kiri, tengah)
        algoritmaMergeSortRekursif(barang, tengah + 1, kanan)
        gabung(barang, kiri, tengah, kanan)

def gabung(barang, kiri, tengah, kanan):
        n1 = tengah - kiri + 1
        n2 = kanan - tengah

        kiri_array = [None] * n1
        kanan_array = [None] * n2

        for i in range(n1):
            kiri_array[i] = barang[kiri + i]
        for j in range(n2):
            kanan_array[j] = barang[tengah + 1 + j]
        
        i = j = 0
        k = kiri

        while i < n1 and j < n2:
            if kiri_array[i].harga <= kanan_array[j].harga:
                barang[k] = kiri_array[i]
                i += 1
            else: 
                barang[k] = kanan_array[j]
                j += 1
            k += 1
        
        while i < n1:
            barang[k] = kiri_array[i]
            i += 1
            k += 1

        while j < n2:
            barang[k] = kanan_array[j]
            j += 1
            k += 1
        

'''def algoritmaBubbleSortIteratif(barang, jumlah):
        for i in range(jumlah - 1):
            swapped = False
            for j in range(jumlah - i - 1):
                if barang[j].harga > barang[j+1].harga:
                    barang[j]. barang[j+1] = barang[j+1]. barang[j]
                    swapped = True
            if not swapped:
                break
'''
def algoritmaBubbleSortIteratif(barang, jumlah):
     for i in range(jumlah):
          for j in range(jumlah - i):
               if barang[j].harga > barang[j+1].harga:
                    barang[j], barang[j+1] = barang[j+1], barang[j]

def tampilkan_barang(barang, jumlah, judul):
        if jumlah == 0:
             print("\nTidak ada barang untuk ditampilkan.")
             return
        

        print(f"\n{judul}")
        print("-" * len(judul))
        for i in range(jumlah):
            print(f"{i + 1}. {barang[i].nama} - Harga: {barang[i].harga:.2f}")

def perbarui_grafik(n_nilai, waktu_bubble, waktu_merge):
        plt.figure(figsize=(8,6))
        plt.clf()
        plt.plot(n_nilai, waktu_bubble, label='Bubble Sort Iteratif', color='blue', marker='o', linestyle='-')
        plt.plot(n_nilai, waktu_merge, label='Merge Sort Rekursif', color='green', marker='o', linestyle='--')
        plt.title('Perbandingan Waktu Eksekusi : Bubble Sort vs Merge Sort', fontsize=14)
        plt.xlabel('Jumlah Barang (n)', fontsize=12)
        plt.ylabel('Waktu Eksekusi (detik)', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.draw() #perbarui grafik setelah diinputkan jumlah baru
        plt.pause(0.01) #memberikan jeda untuk menampilkan grafik


    #fungsi menampilkan waktu tabel eksekusi 

def tampilkanTabel(waktu_bubble, waktu_merge, n_nilai):
        tabel = PrettyTable()
        tabel.field_names = ["Jumlah Barang", "Bubble Sort(s)", "Merge Sort (s)"]
        for i in range(len(n_nilai)):
            tabel.add_row([n_nilai[i], f"{waktu_bubble[i]:.6f}", f"{waktu_merge[i]:.6f}"])
        print(tabel)

    ##program utama
def main():
        n_nilai = [] #menyimpan barnag yang diuji
        waktu_bubble = [] #menyimpan waktu eksekusi bubble sort
        waktu_merge = [] #menyimpan waktu merge

        while True:
            #membaca data dari pengguna
            barang, jumlah = bacaBarang()

            if jumlah == 0:
                break # akan keluar jika tidak ada barang yang dimasukkan
            
            n_nilai.append(jumlah)

            #melakukan sortir menggunakan merge sort(rekursif)
            barang_bubble = [None] * jumlah
            for i in range(jumlah):
                 barang_bubble[i] = barang[i]
            mulai_bubble = time.time()
            algoritmaBubbleSortIteratif(barang_bubble, jumlah - 1)
            durasi_bubble = time.time() - mulai_bubble
            waktu_bubble.append(durasi_bubble)

            barang_merge = barang[:]
            mulai_merge = time.time()
            algoritmaMergeSortRekursif(barang_merge, 0, jumlah - 1)
            durasi_merge = time.time() - mulai_merge
            waktu_merge.append(durasi_merge)

            #tampilkan hasil 
            tampilkan_barang(barang_bubble, jumlah, "Daftar Barang Setelah diurutkan dengan Algoritma Bubble Sort (Iteratif)")
            print(f"Waktu eksekusi Bubble Sort : {durasi_bubble:.6f} detik")

            tampilkan_barang(barang_merge, jumlah, "Daftar Barang Setelah diurutkan dengan Algoritma Merge Sort (Rekursif)")
            print(f"Wkatu eksekusi Merge Sort : {durasi_merge:.6f} detik")

            #menampilkan tabel waktu eksekusi 
            tampilkanTabel(waktu_bubble, waktu_merge, n_nilai)

            #memperbarui grafik perbandingan waktu eksekusi
            perbarui_grafik(n_nilai, waktu_bubble, waktu_merge)

        print("Program selesai. Terimakasih!")
        plt.ioff()
        plt.show()

main()