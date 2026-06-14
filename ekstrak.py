import requests
import os

# Membuat folder data_raw
os.makedirs('./data/raw',exist_ok=True)

# Link URL untuk mendownload Data
taxi_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-01.parquet'
zone_url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

# Mengambil nama file dari URL
taxi_file_name = taxi_url.split("/"[-1])
zone_file_name = zone_url.split("/"[-1])

# Path untuk menyimpan Data mentah
taxi_file_path = './data/raw/yellow_tripdata_2026-01.parquet'
zone_file_path= './data/raw/taxi_zone_lookup.csv'

# Function untuk mendownload file
def download_file(url, save_path):
    # print(f'Downloading from : {url}')

    with requests.get(url, stream=True) as r:
        # Untuk memastikan request sukses
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    # print(f'Download Success, Saved to : {save_path}')

# Mendownload kedua file

download_file(taxi_url,taxi_file_path)
download_file(zone_url,zone_file_path)

