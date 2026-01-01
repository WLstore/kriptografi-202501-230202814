# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: week10-pki 
Nama:Lukman Wahyu Permadi
NIM: 230202814
Kelas: 5IKRB

---

## 1. Tujuan
Membuat sertifikat digital sederhana menggunakan pustaka Python.

Menjelaskan peran Certificate Authority (CA) dalam ekosistem PKI.

Mengevaluasi fungsi PKI dalam menjamin keamanan komunikasi seperti HTTPS dan TLS.

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sebuah kerangka kerja yang terdiri dari perangkat keras, perangkat lunak, orang, proses, dan kebijakan yang diperlukan untuk membuat, mengelola, mendistribusikan, menggunakan, menyimpan, dan mencabut sertifikat digital. Komponen kunci dalam PKI adalah sertifikat digital yang mengikat kunci publik dengan identitas entitas (seperti individu atau organisasi).

Certificate Authority (CA) bertindak sebagai pihak ketiga terpercaya yang memvalidasi identitas pemegang sertifikat dan menandatangani sertifikat tersebut secara digital. Dalam proses komunikasi aman (seperti HTTPS), PKI memastikan bahwa pengguna berkomunikasi dengan server yang asli dan bukan penyamar, serta menyediakan mekanisme enkripsi untuk melindungi data selama transmisi.

## 3. Alat dan Bahan
Python 3.11 atau lebih baru.

Visual Studio Code sebagai Code Editor.

Library Python: cryptography.

Git untuk manajemen versi dan repositori.

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
Membuat struktur folder praktikum di praktikum/week10-pki/ yang terdiri dari folder src, screenshots, dan file laporan.md.

Menginstal pustaka yang diperlukan dengan perintah pip install cryptography.

Membuat file skrip Python bernama pki_cert.py di dalam folder src/.

Menuliskan kode program untuk menghasilkan pasangan kunci RSA, membuat identitas subjek, dan melakukan self-signing pada sertifikat.

Menjalankan program menggunakan perintah python src/pki_cert.py.

Memverifikasi kemunculan file cert.pem di direktori kerja.

Mendokumentasikan hasil percobaan dan menjawab pertanyaan diskusi.

## 5. Source Code
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# 1. Generate key pair (Private & Public Key)
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 2. Buat subject & issuer (Self-signed: Issuer sama dengan Subject)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Jawa Tengah"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Kebumen"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"lukman-example.com"),
])

# 3. Membangun Sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# 4. Simpan sertifikat ke dalam file .pem
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

# 5. Simpan private key (Opsional, untuk referensi)
with open("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

print("Sertifikat digital (cert.pem) dan Private Key (key.pem) berhasil dibuat.")

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)



---

## 7. Jawaban Pertanyaan
Apa fungsi utama Certificate Authority (CA)? Fungsi utama CA adalah sebagai otoritas pihak ketiga yang terpercaya untuk memvalidasi identitas sebuah entitas dan menerbitkan sertifikat digital yang mengikat identitas tersebut dengan kunci publiknya. CA menjamin bahwa kunci publik tersebut benar-benar milik entitas yang tertera di sertifikat.

Mengapa self-signed certificate tidak cukup untuk sistem produksi? Karena self-signed certificate tidak memiliki rantai kepercayaan (chain of trust) ke root CA yang diakui secara global. Browser atau sistem lain akan menampilkan peringatan keamanan "Not Secure" atau "Connection not private" karena tidak ada pihak independen yang menjamin keaslian identitas server tersebut.

Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS? PKI mencegah Man-in-the-Middle (MITM) melalui proses otentikasi. Saat klien terhubung ke server, server mengirimkan sertifikat digitalnya. Klien memverifikasi tanda tangan digital pada sertifikat tersebut menggunakan kunci publik CA yang sudah tertanam di sistem operasi/browser. Jika penyerang mencoba mencegat dan memberikan sertifikat palsu, verifikasi tanda tangan akan gagal, dan komunikasi akan dihentikan sebelum data sensitif dikirim.
---

## 8. Kesimpulan
Praktikum ini berhasil mensimulasikan pembuatan sertifikat digital sederhana menggunakan Python. Dapat disimpulkan bahwa meskipun kita dapat membuat sertifikat sendiri, peran CA sangat krusial dalam dunia nyata untuk membangun kepercayaan (trust) antar entitas di jaringan publik agar terhindar dari pemalsuan identitas.
## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice.

Pustaka Dokumentasi: Cryptography.io Documentation (Python Cryptography Authority).

## 10. Commit Log
Author: Lukman Wahyu Permadi lukmanwahyupermadi@gmail.com
Date:   2026-01-01

    week10-pki: implementasi pembuatan sertifikat digital dan laporan PK