## Lembar Perencanaan Proyek Kelompok (Project Charter)
#Numpy = Komputasi Numerik (import numpy as np)
#Pandas = Memanipulasi Data (import pandas as pd)
#Matplotlib & Seaborn = Visualisasi Data (import matplotlib.pyplot as plt, import seaborn as sns)

#Alur kerja EDA
# 1. Data loading (memuat data dari file CSV ke dalam dataframe)
# 2. Data inspection (mengenali struktur data: jumlah baris, kolom, tipe data, dan nilai kosong)
# 3. Data cleaning (membersihkan data: mengisi nilai kosong, menghapus duplikat, dan mengubah tipe data)
# 4. Data manipulation (memfilter, mengurutkan, membuat kolom turunan, dan agregasi)


## Nama Anggota Kelompok
# Nama: 'Albi'
# Nama: 'Habibi'

## Dataset yang dipilih:
# [] Data Penjualan Kantik/Toko
# [x] Data Nilai Akademik Siswa
# [] Data Sensor IoT Sederhana
# [] Dataset lain..

## Pertanyaan analisis awal
# 1. Siapa nama murid yang memiliki nilai tertinggi dalam mata pelajaran Matematika?
# 2. Siapa nama-nama murid yang memiliki nilai yang kosong/null?
# 3. Apa nilai rata-rata  dari mata pelajaran Pemrogaman Web?

## Dugaan Masalah Kualitas Data
# [x] Missing value dalam kolom (guru_pengampu)
# [] Duplikat data
# [x] Tipe data tidak sesuai pada kolom... (tanggal_ujian, nilai)


## Rencana Teknik Pembersihan 
# 1. dikarenakan adanya missing value pada kolom guru_pengampu, maka akan dilakukan pengisian nilai kosong dengan metode fillna() dengan mengisi nilai kosong dengan string "guru tidak diketahui"
# 2. dikarenakan adanya tipe data yang tidak sesuai pada kolom tanggal_ujian, maka akan dilakukan konversi tipe data menjadi datetime dengan metode pd.to_datetime()
# 3. dan juga dikarenakan adanya tipe data yang tidak sesuai pada kolom nilai, maka akan dilakukan konversi tipe data menjadi integer dengan metode astype(int)

## Rencana Manipulasi Data
# Filter: 
# Sort: 
# Kolom turunan:
# Groupby/agregat: 

## Jadwal Kerja 
# P3 (Loading & Inspection) : 09/09/2026 
# P4 (Cleaning) : 09/09/2026
# P5 (Manipulation) : 16/09/2026
# P6 (Uji/Presentasi) :

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_df = pd.read_csv('dataset_nilai_akademik_siswa.csv')
df = raw_df.copy()
df.info() #menampilkan info dataframe; tipe data, jumlah non-null tiap kolom
#^dengan melakukan tahap tersebut, kita mengetahui tipe data masing masih kolom, outputnya untuk sekarang seperti ini;
# #   Column          Non-Null Count  Dtype
# ---  ------          --------------  -----
# 0   id_siswa        79 non-null     str  
# 1   nama            79 non-null     str  
# 2   kelas           79 non-null     str  
# 3   mata_pelajaran  79 non-null     str  
# 4   jenis_ujian     79 non-null     str  
# 5   tanggal_ujian   79 non-null     str  
# 6   nilai           75 non-null     str  
# 7   guru_pengampu   75 non-null     str  
# dtypes: str(8)

print(''), print('')
print(df.isnull().sum()) #dari syntax ini, kita dapat mengetahui bahwa ada 2 jenis kolom yang memiliki masing masing 4 nilai kosong/null.
print(''), print('')
print(df.duplicated().sum()) #untuk cek berapa data yang duplicate
print(''), print('')
print(df.dtypes) #untuk cek tipe dari semua kolom



df = df.drop_duplicates() #untuk menghapus data yang duplicate

# Standardisasi semua nilai dalam kolom jenis_ujian agar seragam dan uppercase
# Contoh: uts -> UTS, uh -> UH, uas -> UAS
df['jenis_ujian'] = df['jenis_ujian'].astype(str).str.strip().str.upper()

# Membersihkan kolom nilai
df["nilai"] = df["nilai"].str.replace(" poin", "", regex=False)
df["nilai"] = df["nilai"].str.replace(",", ".", regex=False)

# Mengubah string menjadi angka
df["nilai"] = pd.to_numeric(df["nilai"], errors="coerce")

# Mengecek nilai yang tidak masuk akal
df[df["nilai"] > 100]

# Mengubah nilai di atas 100 menjadi kosong
df.loc[df["nilai"] > 100, "nilai"] = pd.NA
df = df.dropna() #untuk menghapus data yang kosong

# Mengecek hasil akhir
df["nilai"].dtype
df["nilai"].isna().sum()

print(''), print('')
print(df.head()) #dari tahap pengecekan data 5 teratas, kini nilai sudah diganti dari typedata STR menjadi float.



print(''), print('')
# indonesian month names 
bulan_map = {
    'Januari': 'January', 'Februari': 'February', 'Maret': 'March',
    'April': 'April', 'Mei': 'May', 'Juni': 'June',
    'Juli': 'July', 'Agustus': 'August', 'September': 'September',
    'Oktober': 'October', 'November': 'November', 'Desember': 'December'
}

for id_month, en_month in bulan_map.items():
    df['tanggal_ujian'] = df['tanggal_ujian'].str.replace(id_month, en_month, regex=False)

# 2. Convert to a unified datetime object
df['tanggal_ujian'] = pd.to_datetime(df['tanggal_ujian'], dayfirst=True, format='mixed')

# 3. Format into a consistent string standard (YYYY-MM-DD)
df['tanggal_ujian'] = df['tanggal_ujian'].dt.strftime('%Y-%m-%d')

print(''), print('')
print(df.head()) #dari tahap ini, kita telah mengubah tanggal ujian menjadi format yang konsisten, yaitu YYYY-MM-DD.

print(''), print('')

# Jawaban pertanyaan analisis menggunakan data yang sudah dibersihkan
print('=== Jawaban Pertanyaan Analisis ===')

# 1. Siapa nama murid yang memiliki nilai tertinggi dalam mata pelajaran Matematika?
print('1. Nama murid dengan nilai tertinggi di Matematika:')
math_top = df[df['mata_pelajaran'] == 'Matematika'].sort_values('nilai', ascending=False).head(1)
print(math_top[['nama', 'mata_pelajaran', 'nilai']].to_string(index=False))

print('')

# 2. Siapa nama-nama murid yang memiliki nilai yang kosong/null?
print('2. Nama murid dengan nilai kosong/null sebelum cleaning:')
raw_null_values = raw_df[raw_df['nilai'].isna()][['nama', 'mata_pelajaran', 'nilai', 'guru_pengampu']]
if raw_null_values.empty:
    print('Tidak ada data dengan nilai kosong pada dataset raw.')
else:
    print(raw_null_values.to_string(index=False))

print('')

# 3. Apa nilai rata-rata dari mata pelajaran Pemrogaman Web?
print('3. Rata-rata nilai Pemrogaman Web:')
web_mean = df[df['mata_pelajaran'] == 'Pemrograman Web']['nilai'].mean()
print(round(web_mean, 2))

print(''), print('')
print(df.head())