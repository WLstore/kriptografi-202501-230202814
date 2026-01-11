# Laporan Praktikum Kriptografi
Minggu ke-: 14
Topik: week14-analisis-serangan
Nama: Lukman Wahyu Permadi  
NIM: 230202824
Kelas: 5IKRA  

---

## 1. Tujuan
Mengidentifikasi jenis serangan pada sistem informasi nyata.

Mengevaluasi kelemahan algoritma kriptografi yang digunakan.

Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.
---

## 2. Dasar Teori
Kriptografi bertujuan untuk menjaga kerahasiaan (confidentiality), integritas (integrity), dan ketersediaan (availability). Namun, seiring meningkatnya kekuatan komputasi, algoritma lama seperti MD5 atau DES kini dianggap tidak aman karena rentan terhadap serangan brute force dan collision. Serangan kriptografi sering kali mengeksploitasi tiga aspek utama: kelemahan matematis algoritma, kesalahan implementasi (seperti hardcoded keys), atau kesalahan konfigurasi (seperti protokol TLS versi lama).

Salah satu serangan paling umum pada sistem autentikasi adalah Dictionary Attack dan Brute Force. Penyerang mencoba menebak nilai hash dari kata sandi dengan mencocokkan nilai hash yang bocor dengan daftar kata sandi populer yang telah di-hash sebelumnya. Untuk memitigasi ini, penggunaan fungsi hashing modern yang memiliki mekanisme cost factor dan salting seperti Argon2 atau Bcrypt sangat direkomendasikan.

---

## 3. Alat dan Bahan
Python 3.x (untuk simulasi pengecekan hash atau brute force sederhana)

Terminal / Command Prompt

Git dan akun GitHub

Wordlist (misalnya: rockyou.txt versi ringkas) atau alat bantu seperti hashcat (opsional)

---

## 4. Langkah Percobaan
Identifikasi Kasus: Memilih kasus kebocoran data yang menggunakan hash MD5 tanpa salt (misalnya simulasi serangan pada database lama).

Eksperimen: Membuat skrip Python sederhana untuk melakukan perbandingan hash (dictionary attack) terhadap sebuah string MD5.

Analisis: Mencatat waktu yang dibutuhkan dan kemudahan dalam memecahkan hash tersebut dibandingkan dengan standar keamanan saat ini.

Rekomendasi: Menyusun skema perbaikan menggunakan algoritma yang lebih kuat (SHA-256 atau Argon2).

Dokumentasi: Mengambil screenshot hasil percobaan dan melakukan commit ke repositori Git.
---

## 5. Source Code
import hashlib

def dictionary_attack(target_hash, dictionary_file):
    try:
        with open(dictionary_file, 'r', encoding='utf-8') as f:
            for word in f:
                word = word.strip()
                # Mencoba hashing kata dari kamus menggunakan MD5
                hashed_word = hashlib.md5(word.encode()).hexdigest()
                
                if hashed_word == target_hash:
                    return f"Password ditemukan: {word}"
        return "Password tidak ditemukan dalam kamus."
    except FileNotFoundError:
        return "File kamus tidak ditemukan."

# Contoh target: hash dari kata 'rahasia123'
target = "7f7390740a02a4669f9478f7e3465355" 
print(f"Mencari password untuk hash: {target}")
print(dictionary_attack(target, 'password_list.txt'))

---

## 6. Hasil dan Pembahasan
(Identifikasi Serangan: Serangan yang dianalisis adalah Dictionary Attack terhadap algoritma MD5. Vektor serangan berasal dari akses ilegal ke database yang menyimpan password dalam bentuk hash lemah tanpa salt.

Evaluasi Kelemahan: MD5 memiliki ruang kunci yang relatif kecil untuk standar saat ini dan sangat rentan terhadap collision attack. Tanpa salt, penyerang dapat menggunakan Rainbow Tables untuk memecahkan hash secara instan.

Hasil Eksekusi: Program berhasil menemukan kata sandi asli dalam waktu kurang dari 1 detik karena efisiensi komputasi MD5 yang terlalu tinggi (memudahkan brute force).

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
Mengapa banyak sistem lama masih rentan? Karena adanya faktor legacy system (sistem warisan) yang sulit diperbarui tanpa merusak kompatibilitas, kurangnya kesadaran pengembang saat membangun sistem, atau biaya migrasi infrastruktur yang dianggap mahal.

Apa bedanya kelemahan algoritma dengan kelemahan implementasi? Kelemahan algoritma terletak pada desain matematisnya (misal: MD5 yang rentan kolisi). Kelemahan implementasi terjadi ketika algoritma aman digunakan secara salah (misal: menyimpan kunci enkripsi AES di dalam kode program/hardcoded).

Bagaimana organisasi memastikan sistem tetap aman? Dengan rutin melakukan audit keamanan, menerapkan kebijakan pembaruan algoritma secara berkala (kripto-agility), menggunakan standar terbaru dari NIST, dan melakukan penetrasi tes secara rutin.
---

## 8. Kesimpulan
Berdasarkan analisis, penggunaan algoritma hashing lama seperti MD5 sangat berbahaya karena mudah dipatahkan dengan serangan dictionary attack. Rekomendasi utama untuk sistem nyata adalah bermigrasi ke algoritma Argon2 atau SHA-256 dengan tambahan salt yang unik untuk setiap pengguna guna memperlambat upaya serangan brute force.
---

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

NIST Special Publication 800-132. Recommendation for Password-Based Key Derivation.
---

## 10. Commit Log

commit abc12345
Author: lukmanwahyupermadi@gmail.com <email>
Date:   2026-01-11
week14-analisis-serangan
```
