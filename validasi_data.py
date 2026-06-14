import pandas as pd
import os 


# Path file dari data mart
data_mart_path = './data/mart/yellow_tripdata_2026-01.csv'

# Path untuk output dari data mart_cleaned
output_path = './data/mart_cleaned'

# Membuat folder untuk penyimanan valdiasi_data
os.makedirs(output_path, exist_ok=True)

valid_file = os.path.join(output_path,'valid_data.csv')
karantina_file = os.path.join(output_path,'karantina_data.csv')

# Load data dari data mart
df_taxi_mart = pd.read_csv(data_mart_path,low_memory=False)

# Membersihkan Data di kolom store_and_fwd_flag
df_taxi_mart['store_and_fwd_flag']=(
    df_taxi_mart['store_and_fwd_flag'].astype('string').str.strip().fillna('Unknown')
)

# Notifikasi File data_mart berhasil di baca
# print(f'Data berhasil terbaca : {df_taxi_mart.shape}')

# Mengecek Tipe data semua kolom Before
# print("======== TIPE DATA SEMUA KOLOM BEFORE ========")
# print(df_taxi_mart.dtypes)

# Mengkonversi kolom yang memiliki value datetime menjadi tipe data datetime
df_taxi_mart['tpep_pickup_datetime']=pd.to_datetime(df_taxi_mart['tpep_pickup_datetime'],errors='coerce')
df_taxi_mart['tpep_dropoff_datetime']=pd.to_datetime(df_taxi_mart['tpep_dropoff_datetime'],errors='coerce')
df_taxi_mart['pickup_date']=pd.to_datetime(df_taxi_mart['pickup_date'],errors='coerce')

# Mengecek Tipe data semua kolom After
# print("======== TIPE DATA SEMUA KOLOM After ========")
# print(df_taxi_mart.dtypes)

# Membuat error type untu validasi data
df_taxi_mart['error_type'] = None

# Membuat validai durasi yang invalid
df_taxi_mart.loc[
    df_taxi_mart['tpep_dropoff_datetime'] <= df_taxi_mart['tpep_pickup_datetime'],
    'error_type'
] = 'duration invalid'

# Membuat validasi distance invalid
df_taxi_mart.loc[
    df_taxi_mart['trip_distance'] <= 0,
    'error_type'
] = df_taxi_mart['error_type'].fillna('distance invalid')

# Memisahkan Data valid dan data invalid
df_valid = df_taxi_mart[df_taxi_mart['error_type'].isna()].copy()
df_invalid = df_taxi_mart[df_taxi_mart['error_type'].notna()].copy()

# Menyimpan File
df_valid.to_csv(valid_file,index=False)
df_invalid.to_csv(karantina_file,index=False)

# Membuat informasi jumlah data valid dan invalid
# print('======== Total Data Valid Dan Invalid ========')
# print(f'Total Data        : {len(df_taxi_mart)}')
# print(f'Total Data Valid  : {len(df_valid)}')
# print(f'Tota Data Invalid : {len(df_invalid)}')

# Menghitung jumlah error disance invalid dan duration invalid
# print('======== Jumlah Error/Invalid ========')
# print(df_invalid['error_type'].value_counts())