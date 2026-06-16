# ETL PIPELINE TAXI

# Deskripsi Project
Project ini merupakan Capstone Project Module 1 dari Bootcamp Data Engineer Purwadhika.

Project ini bertujuan untuk membangun pipeline ETL (Extract, Transform, Load) secara otomatis menggunakan Python, Shell Script, Docker, dan Docker Compose. Pipeline ini memproses data taxi mulai dari tahap pengambilan data, transformasi data, penyimpanan hasil akhir, hingga pengecekan kualitas data.

# Workflow Pipeline
Pipeline berjalan otomatis dengan urutan:

Extract → Transform → Load → Data Quality Check

# Struktur Folder

Berikut gambaran struktur folder project:

capstone1_etl_pipeline_taxi/
│
├── data/
│   ├── raw/              # Folder untuk menyimpan hasil ekstrak data mentah
│   ├── transformed/      # Folder untuk menyimpan hasil transformasi data, dalam bentuk parquet
│   ├── mart/             # Folder untuk menyimpan hasil dari load data, dalam bentuk csv
│   ├── mart_cleaned/     # Folder hasil cek quality data, data tidak valid disimpan karantina_data.csv, data valid disimpan ke file valid_data.csv 
│   └── logs/             # Untuk menyimpan history activity 
│
├── docker-compose.yml    # Untuk membuat Containerization
├── Dockerfile            # Untuk Build image Docker
├── ekstrak.py            # Proses Extract data mentah
├── transform.py          # Proses Transform data
├── load.py               # Proses Load data dan menyimopan dalam bentuk csv
├── validasi_data.py      # Proses Cek Data quality
├── pipeline.sh           # Script untuk menjalankan ETL pipeline
├── requirements.txt      # Untuk menyimpan library yang dibutuhkan
└── README.md             # Dokumentasi project

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