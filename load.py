import pandas as pd
import os

# Membuat folder untuk loading data
os.makedirs('./data/mart',exist_ok=True)

# Path file hasil Transformasi
input_file_mart_path = './data/transformed/yellow_tripdata_2026-01.parquet'

# Membuat output path data mart nya
output_file_mart_path = os.path.join(
    './data/mart',
    'yellow_tripdata_2026-01.csv'
)

# Membaca file hasil transformasi
df_taxi_mart = pd.read_parquet(input_file_mart_path)

# print('Data Taxi Transformed Berhasil Di Baca')
# print(df_taxi_mart.shape)

# Load file ke dalam data/mart dalam bentuk csv
df_taxi_mart.to_csv(output_file_mart_path,index=False)

# Notifikasi Saat data berhasil Di Load 
# print(f'File Berhasil Di Load ke : {output_file_mart_path}')
