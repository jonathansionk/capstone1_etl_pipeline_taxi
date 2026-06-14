# ETL PIPELINE TAXI

# Deskripsi Project
Project ini adalah Capstone 1 dari Module 1 Bootcamp Data Engineer Purwadikha
Membuat pipeline ETL (Extract, Transform, Load) yang dijalankan secara otomatis menggunakan Python, Shell Script, Docker , dan Docker Compose.

# Workflow Pipeline
Pipeline berjalan otomatis dengan urutan:

Extract → Transform → Load → Data Quality Check


# Cara Menjalankan Program

1. Clone Repository

    ```bash
    git clone https://github.com/jonathansionk/capstone1_etl_pipeline_taxi.git
    cd capstone1_etl_pipeline_taxi

2. Pastikan Docker Desktop berjalan
    
    - Buka Docker Desktop
    - Pastikan status Running

3. Jalankan Pipeline

    - Pastikan alamat di terminal sudah seusai dengan lokasi file docker-compose.yml
    - docker compose up --build

4. Pipeline akan berjalan secara otomatis 

# Tech Stack
- Python 3.10
- Pandas
- Docker
- Docker Compose
- Bash Script