#Membuat list berisi 10
list_nama = ['adhi', 'afik', 'agus', 'rafi', 'alip', 'nisa', 'ara', 'athan', 'ayu', 'bagus']

#Menampilkan isi list indeks nomor 4,6,7
print("list_nama[3]: ",list_nama[4])
print("list_nama[5]: ",list_nama[6])
print("list_nama[6]: ",list_nama[7])

#Mengganti nama di list 3,5,9
list_nama[3] = 'uddin'
list_nama[5] = 'attar'
list_nama[9] = 'danendra'
print(list_nama)

#Menambah 2 nama teman
list_nama.append('raka')
list_nama.append('memed')
print(list_nama)

#Menampilkan semua teman dalam perulangan
for nama in list_nama:
    print(nama)

#Menampilkan panjang list
print("Panjang list_nama adalah: ",len(list_nama))