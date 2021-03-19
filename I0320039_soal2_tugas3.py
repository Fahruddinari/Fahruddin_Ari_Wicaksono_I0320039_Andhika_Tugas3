#Membuat program dictionary
biodata = {'nama': 'Fahruddin Ari',
           'hobi1':'ngegame',
           'hobi2':'lari',
           'hobi3':'bermain bulu tangkis',
           'sosmed1':'uddinaja_',
           'sosmed2':'uddinsukamamba',
           'sosmed3':'lambe_moba',
           'lagu1':'balonku ada 5',
           'lagu2':'topi saya bundar',
           'lagu3':'pok ame ame',
           'makanan1':'mie ayam',
           'makanan2':'bubur ayam',
           'makanan3':'sate katak'}

#Mengubah salah satu hobi dan sosial media
biodata['hobi2'] = 'futsal'
print("biodata['hobi2']: ",biodata['hobi2'])
biodata['sosmed2'] = 'arie_untunk'
print("biodata['sosmed2']: ",biodata['sosmed2'])
print("++++++++++++++++++")

#Menghapus dua makanan favorit
del biodata['makanan1']
del biodata['makanan2']
for x,y in biodata.items():
    print(x,y)
print(biodata)
print("++++++++++++++++++++")

#Menambah satu hobi
biodata['hobi4'] = 'catur'
for a,b in biodata.items():
    print(a,b)
print(biodata)
print("++++++++++++++++++++")