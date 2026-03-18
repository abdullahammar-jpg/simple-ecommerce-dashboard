# E-Commerce Data Analysis Dashboard ✨

## Deskripsi
Dashboard ini merupakan proyek akhir dari analisis dataset E-Commerce (Olist) di Brasil. Proyek ini mencakup proses *Data Wrangling*, *Exploratory Data Analysis (EDA)*, hingga *Geospatial Analysis* untuk memahami performa produk, kepuasan pelanggan, dan distribusi geografis pengguna.

## Struktur Proyek
- `/dashboard`: Berisi kode utama dashboard Streamlit dan dataset yang sudah dibersihkan.
- `/data`: Berisi dataset mentah (raw data).
- `Proyek_Analisis_Data.ipynb`: File Google Colab Notebook yang digunakan untuk analisis data awal.
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `url.txt`: Berisi link dashboard

## Instalasi
Untuk menjalankan dashboard ini secara lokal, pastikan Anda telah menginstal Python. Kemudian, ikuti langkah-langkah berikut (Install requirements terlebih dahulu):

1. **Clone repository ini** (jika menggunakan git) atau unduh folder proyek.
2. **Setup Environtment Anaconda** 
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt
 - **Setup Environtment Shell/Terminal**
    ```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    pipenv install
    pipenv shell
    pip install -r requirements.txt
3. **Jalankan streamlit** dengan: 
    ```bash
    streamlit run dashboard.py 
 - **Jika tidak bisa**, coba: 
    ```bash
    streamlit run "pathfile"
