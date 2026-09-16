import numpy as np
import pandas as pd

harga = np.array([5000, 7000, 3000, 12000, 4500])
print('Rata-rata harga:', np.mean(harga))
print('Harga tertinggi:', np.max(harga))
print('Harga setelah diskon 10%:', harga * 0.9)
print(' ')

data_kantin = {
    'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Teh Hangat', None],
    'harga': [12000, 4000, 10000, 4000, 8000],
    'terjual': [23, 40, None, 35, 18]
}
df = pd.DataFrame(data_kantin)
print(df)
print('')

df = pd.read_csv('data_kantin.csv')
print('5 baris pertama')
print(df.head())        #5 baris pertama
print(' ')

print('info dataframe')
print(df.info())        #info; typedata, jumlah non-null tiap kolom
print(' ')

print('statistik')
print(df.describe())   #statistik deskriptif kolom numerik
print('')

print('jumlah baris dan kolom')
print(df.shape)       #jumlah baris dan kolom
print(' ')

print('jumlah data kosong tiap kolom')
print(df.isnull().sum()) #jumlah data kosong tiap kolom
print(' ')

df['terjual'] = df['terjual'].fillna(0) #mengisi data kosong kolom terjual dengan 0 [.fillna(0)]
df = df.dropna(subset=['menu']) #menghapus baris jika kolom menu kosong [.dropna(subset=['menu'])]
print(' ')

print('jumlah baris duplikat')
print(df.duplicated().sum()) #jumlah baris duplikat
print(' ')
df = df.drop_duplicates()

df['harga'] = df['harga'].astype(int) # memastikan tipe data harga adalah int -------------------------------------------
print(df.dtypes) #menampilkan tipe data tiap kolom
print(' ')

laris = df[df['terjual'] > 20] # filtering
urut = df.sort_values(by='terjual', ascending=False) # sorting
df['total_pendapatan'] = df['harga'] * df['terjual'] # kolom turunan
ringkasan = df.groupby('menu')['total_pendapatan'].sum() # agregasi
print(ringkasan)





## Soal
#Tugas Analisis 1: Bandingkan hasil harga * 0.9 di atas dengan jika harga berupa list Python
#                  biasa (bukan array). Apa yang terjadi bila kamu mencoba [5000,7000,3000] * 0.9? Jelaskan
#                  mengapa berbeda.

#Tugas Analisis 2: Amati tabel yang dihasilkan. Kolom mana yang terlihat memiliki data kosong
#                  (None)? Menurutmu apa risikonya jika data ini langsung dianalisis tanpa dibersihkan?

#Tugas Analisis 3: Dari hasil df.info(), kolom mana yang jumlah non-null-nya lebih sedikit dari
#                  jumlah baris total? Apa artinya?

#Tugas Analisis 4: Mengapa pada contoh di atas kolom terjual diisi (fillna) sedangkan baris
#                  dengan menu kosong justru dihapus (dropna)? Diskusikan alasan logisnya.

#Tugas Analisis 5: Setelah drop_duplicates(), berapa jumlah baris dataset sekarang dibanding
#                  sebelumnya? Mengapa penting memastikan tipe data (dtypes) sudah benar sebelum data
#                  dianalisis lebih lanjut?

#Tugas Analisis 6: Dari hasil groupby di atas, menu apa yang menghasilkan total_pendapatan
#                  tertinggi? Bagaimana informasi ini bisa membantu pengambilan keputusan di kantin sekolah?

## Jawaban
#Analisis 1: Jika dalam penulisan kita langsung ganti dengan [5000,7000,3000] * 0.9, akan terjadi error karena list Python tidak mendukung operasi perkalian dengan float.
#            berikut error outputnya;
#                 print('Harga setelah diskon 10%:', [5000, 7000, 3000] * 0.9)
#                                       ~~~~~~~~~~~~~~~~~~~^~~~~
#                 TypeError: can't multiply sequence by non-int of type 'float'

#Analisis 2: Kolong yang memiliki data (None) adalah kolom 'menu' (baris ke-4) dan kolom 'terjual' (baris ke -3). 
#            Resiko jika data ini dianalisis tanpa dibersihkan dapat menyebabkan error atau hasil analisis yang tidak akurat.

#Analisis 3: Kolom yang memiliki jumlah non-null yang lebih sedikit dari jumlah baris total adalah kolom 'menu' (107 non-null) dan kolom 'terjual' (104 non-null).
#            Arti dari non-null adalah kolom tersebut memiliki data yang hilang (missing value) dalam file data csv-nya

#Analisis 4: kolom 'terjual' diisi dengan 0 karena data kosong pada kolom tersebut dianggap seperti tidak ada yang dibeli/tidak ada penjualan.
#            Sedangkan baris dengan menu kosong dihapus karena menu adalah informasi penting untuk analisis, 
#            jika tidak ada menu maka data tersebut tidak berguna dan dapat mengganggu analisis.

#Analisis 5: Setelah drop_duplicates(), jumlah baris dataset sekarang berkurang dibanding sebelumnya karena baris yang duplikat dihapus.
#            Penting memastikan tipe data (dtypes) sudah benar sebelum data dianalisis lebih lanjut karena tipe data yang salah dapat menyebabkan error atau hasil analisis yang tidak akurat.
#            Misalnya, jika kolom harga masih berupa float atau string, maka perhitungan harga total atau diskon tidak akan berjalan dengan benar.    

#Analisis 6: Dari hasil groupby di atas, menu yang menghasilkan total_pendapatan tertinggi adalah 'Nasi Goreng' dengan total pendapatan
#            sebesar 3924000, pengetahuan ini bisa membantu pengambilan keputusan di kantin sekolah untuk fokus pada menu yang paling laris.
#            


