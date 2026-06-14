# Untuk Mengambil base image python 
FROM python:3.10

# Untuk membuat timestamp nya sesuai dengan zona WIB
ENV TZ=Asia/Jakarta

# Untuk Set folder kerja di dalam container
WORKDIR /app

# Untuk Mengcopy semua file project ke container
COPY . /app

# Untuk Install Library yang di butuhkan & Untuk menjalankan file pipeline.sh dengan bash
RUN pip install --no-cache-dir -r requirements.txt && chmod +x pipeline.sh

# Untuk Menjalankan script utama 
CMD [ "bash","pipeline.sh" ]