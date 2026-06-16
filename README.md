# ETL PIPELINE TAXI

# Deskripsi Project
Project ini merupakan Capstone Project Module 1 dari Bootcamp Data Engineer Purwadhika.

Project ini bertujuan untuk membangun pipeline ETL (Extract, Transform, Load) menggunakan Python, Shell Script, Docker, dan Docker Compose. Pipeline ini memproses data taxi mulai dari tahap pengambilan data, transformasi data, penyimpanan hasil akhir, hingga pengecekan kualitas data.

# Workflow Pipeline
Pipeline berjalan otomatis dengan urutan:
```text
Extract → Transform → Load → Data Quality Check
```
# Struktur Folder

Berikut gambaran struktur folder project:

```text
capstone1_etl_pipeline_taxi/
│
├── data/
│   ├── mart/                                   # Folder untuk menyimpan hasil load data (csv)
│   │   └── yellow_tripdata_2026-01.csv         # File hasil load data dari hasil transformasi dalam format csv
│   │
│   ├── mart_cleaned/                           # Folder hasil cek quality data
│   │   ├── karantina_data.csv                  # Data tidak valid disimpan dalam file karantina_data.csv
│   │   └── valid_data.csv                      # Data valid disimpan dalam file valid_data.csv
│   │
│   ├── raw/                                    # Folder untuk menyimpan hasil ekstrak data mentah
│   │   ├── taxi_zone_lookup.csv                # File hasil ekstrak data mentah taxi_zone_lookup.csv 
│   │   └── yellow_tripdata_2026-01.parquet     # File hasil ekstrak data mentah yellow_tripdata_2026-01.parquet
│   │
│   ├── transformed/                            # Folder untuk menyimpan hasil transformasi data (parquet)
│   │   └── yellow_tripdata_2026-01.parquet     # File hasil transformasi data dalam format (parquet)
│   │
│   └── logs/                                   # Folder untuk menyimpan history aktivitas pipeline
│       └── pipeline.log                        # File history aktivitas pipeline
│
├── docker-compose.yml                          # Membuat Containerization
├── Dockerfile                                  # Membuat image Docker
│
├── ekstrak.py                                  # Proses Extract data mentah
├── transform.py                                # Proses Transform data
├── load.py                                     # Proses Load data
├── validasi_data.py                            # Data Quality Check
│
├── pipeline.sh                                 # Script menjalankan ETL pipeline secara otomatis
├── requirements.txt                            # List library yang dibutuhkan
└── README.md                                   # Dokumentasi project

```

# Tech Stack
- Python 3.10
- Pandas
- Docker
- Docker Compose
- Bash Script


# Cara Menjalankan Program
1. Buka Visual Studio Code, lalu buka terminal di Visual Studio Code nya

2. Clone Repository
    
    ```bash
    git clone https://github.com/jonathansionk/capstone1_etl_pipeline_taxi.git
    cd capstone1_etl_pipeline_taxi

3. Pastikan Docker Aktif
    Buka Docker Desktop
    Pastikan status Running

4. Jalankan Pipeline

    Pastikan terminal berada di folder project yang terdapat file docker-compose.yml.
    Kemudian jalankan:
    ```bash
    docker compose up --build

5. Pipeline Berjalan Otomatis

    Pipeline akan berjalan dengan urutan:

    Extract → Transform → Load → Data Validation