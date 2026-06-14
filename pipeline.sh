# !/bin/bash (shell script)

# Membuat folder logs
mkdir -p logs

# Path log file
LOG_FILE='./logs/pipeline.log'

# Membuat function untuk menyimpan proses yang di jalankan oleh script
log(){
    echo "$(date '+%Y-%m-%d %H:%M:%S') -$1" | tee -a $LOG_FILE
}

# Membuat Header Pipeline
echo "====================================" | tee -a $LOG_FILE
log "Starting pipeline"


# Untuk menjalnakn file ekstrak.py
log "Running File ekstrak.py....."
python ekstrak.py

if  [ $? -eq 0 ]; then
    log "Extract Completed"
else
    log "Extract Failed"
    exit 1
fi

# Untuk menjalankan file transform.py
log "Running File transform.py....."
python transform.py

if [ $? -eq 0 ]; then
    log "Transform Completed"
else
    log "Transform Failed"
    exit 1
fi

# Untuk menjalankan file load.py
log "Running File load.py....."
python load.py

if [ $? -eq 0 ]; then
    log "Report Completed"
else
    log "Load Failed"
    exit 1
fi

# Untuk menjalankan file validasi_data.py
log "Running File validasi_data.py....."
python validasi_data.py

if [ $? -eq 0 ];then
    log "Data Quality Check Completed"
else
    log "Data Quality Check Failed"
    exit 1
fi

# Pipeline Selesai
log "Pipeline Completed Successfully"
echo "====================================" | tee -a $LOG_FILE