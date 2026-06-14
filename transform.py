import pandas as pd
import os
import re

# Membuat folder untuk hasil transformasi
os.makedirs('./data/transformed',exist_ok=True)

# Path file input Taxi
taxi_file_input = './data/raw/yellow_tripdata_2026-01.parquet'

# Path file output Taxi
taxi_file_output = './data/transformed/yellow_tripdata_2026-01.parquet'

# Path file input Zone
zone_file_input = './data/raw/taxi_zone_lookup.csv'

# Path file output Zone
zone_file_output = './data/transformed/taxi_zone_lookup.csv'

# Membaca file taxi
df_taxi = pd.read_parquet(taxi_file_input)

# Membaca file Zone
df_zone = pd.read_csv(zone_file_input)

# Melihat 5 data pertama di File Taxi
# print(df_taxi.head())

# print("======== TOTAL ROWS & COLUMN ========")
# print(df_taxi.shape)

# Melihat list dari semua nama_kolom
# print("======== COLUMN NAME BEFORE ========")
# print(df_taxi.columns)

# Function untuk rename nama kolom menjadi snake_case

def to_snake_case(column_name):
    column_name = str(column_name).strip()

    # Menganti spasi dan simbol lain nya menjadi underscore ('_')
    column_name = re.sub(r'[^a-zA-Z0-9]+', '_', column_name)

    # Memisahkan huruf kapital berurutan dengan kata berikut nya menggunakan underscore ('_') 
    column_name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', column_name)

    # Memisahkan huruf kecil yang bertemu huruf kapital
    column_name = re.sub(r'([a-z])([A-Z])', r'\1_\2',column_name)

    # Mengubah semu huruf menjadi huruf kecil
    column_name = column_name.lower()

    return column_name

# Rename semua kolom di file Zone
df_zone.columns = [to_snake_case(col) for col in df_zone.columns]

# Rename semua kolom di file Taxi
df_taxi.columns = [to_snake_case(col) for col in df_taxi.columns]
# print("======== COLUMN NAME AFTER ========")
# print(df_taxi.columns)

# Mengecek tipe data semua kolom

# print("======== TIPE DATA SEMUA KOLOM ========")
# print(df_taxi.dtypes)

# Menghitung durasi perjalanan
df_taxi['trip_duration_minutes'] = (
    df_taxi['tpep_dropoff_datetime'] - df_taxi['tpep_pickup_datetime']
).dt.total_seconds()/60

# Menampilkan Hasil trip_duration_minutes
# print("======== MENGHITUNG DURASI PERJALANAN ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'tpep_dropoff_datetime',
#     'trip_duration_minutes'  
# ]].head())

# Mengambil tgl pickUp
df_taxi['pickup_date']=(
    df_taxi['tpep_pickup_datetime'].dt.date
)

# Menampilkan Hasil pickup_date
# print("======== MENAMPILKAN HASIL PICKUP_DATE ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'pickup_date'  
# ]].head())

# Mengambil jam pickup
df_taxi['pickup_hour']=(
    # df_taxi['tpep_pickup_datetime'].dt.strftime('%H:%M') 
    df_taxi['tpep_pickup_datetime'].dt.hour
)

# Menampilkan Hasil pickup_hour
# print("======== MENAMPILKAN HASIL PICKUP_HOUR ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'pickup_hour'  
# ]].head())

# Mengambil nama hari 
df_taxi['pickup_day_name']=(
    df_taxi['tpep_pickup_datetime'].dt.day_name()
)

# Menampilkan Hasil pickup_day_name
# print("======== MENAMPILKAN HASIL PICKUP_DAY_NAME ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'pickup_day_name'  
# ]].head())

# Menandai Weekend
df_taxi['is_weekend'] = (
    df_taxi['pickup_day_name'].apply(
        lambda day : 'YES' if day in ['Saturday','Sunday'] else 'NO'
    )
)

# Menampilkan Hasil is_weekend
# print("======== MENAMPILKAN HASIL IS_WEEKEND ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'pickup_day_name',
#     'is_weekend'
# ]].head())


# Membuat Function untuk membuat kategori waktu
def get_time_period(hour):
    if 7 <= hour <= 9:
        return 'Morning Rush'
    elif 0 <= hour <= 5:
        return 'Late Night'
    elif 6 <= hour <= 10:
        return 'Morning'
    elif 11 <= hour <= 15:
        return 'Afternoon'
    elif 16 <= hour <= 19:
        return 'Evening Rush'
    elif 20 <= hour <= 23:
        return 'Night'
    else:
        return 'Unknown'

# Membuat kolom kategori waktu
df_taxi['time_period']=(
    df_taxi['pickup_hour'].apply(get_time_period)
)

# Menampilkan hasil time_period
# print("======== MENAMPILKAN HASIL TIME_PERIOD ========")
# print(df_taxi[[
#     'tpep_pickup_datetime',
#     'time_period'
# ]].tail())

# Membuat mapping payment_type
payment_mapping = {
    1: 'Credit Card',
    2: 'Cash',
    3: 'No Charge',
    4: 'Dispute',
    0: 'Unknown'
}

df_taxi['payment_name'] = df_taxi['payment_type'].map(payment_mapping)

# Menampilkan hasil payment_name
# print("======== MENAMPILKAN HASIL PAYMENT_NAME ========")
# print(df_taxi[[
#     'payment_type',
#     'payment_name'
# ]].head())

# Membuat mapping store and forward
store_forward_mapping = {
    'Y':'Store and Forward',
    'N':'Normal'
}

df_taxi['store_forward_description']=df_taxi['store_and_fwd_flag'].map(store_forward_mapping).fillna('Unknown')

# Menampilkan hasil Store and Forward
# print("======== MENAMPILKAN HASIL STORE_FORWARD_DESCRIPTION ========")
# print(df_taxi[[
#     'store_and_fwd_flag',
#     'store_forward_description'
# ]].tail())

# print(df_taxi['store_and_fwd_flag'].unique())

# Membuat Mapping pickup loaction
pickup_zone = df_zone.rename(columns={
    'location_id':'pu_location_id',
    'borough':'pickup_borough',
    'zone':'pickup_zone',
    'service_zone':'pickup_service_zone'
})

df_taxi=df_taxi.merge(
    pickup_zone,
    on='pu_location_id',
    how='left'
)

# Membuat Mapping dropoff location
dropoff_zone = df_zone.rename(columns={
    'location_id':'do_location_id',
    'borough':'dropoff_borough',
    'zone':'dropoff_zone',
    'service_zone':'dropoff_service_zone'
})

df_taxi=df_taxi.merge(
    dropoff_zone,
    on='do_location_id',
    how='left'
)

# Menampilkan Mapping lokasi
# print("======== MENAMPILKAN HASIL MAPPING LOCATION ========")
# print(df_taxi[[
#     'pu_location_id',
#         'pickup_borough',
#         'pickup_zone',
#         'pickup_service_zone',
#         'do_location_id',
#         'dropoff_borough',
#         'dropoff_zone',
#         'dropoff_service_zone'
# ]].tail())

# Menyimpan hasil transformasi
df_taxi.to_parquet(taxi_file_output,index=False)
# print(f'Data Taxi Transformed Berhasil Di Simpan ke : {taxi_file_output}')
