# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik:  Diffie-Hellman Key Exchange
Nama: LUKMAN WAHYU PERDMADI
NIM: 230202814
Kelas: 5IKRB  

---

## 1. Tujuan
Mensimulasikan protokol Diffie–Hellman dalam proses pertukaran kunci publik untuk membentuk kunci rahasia bersama melalui jaringan yang tidak aman.

Memahami mekanisme pembentukan kunci rahasia menggunakan bilangan prima, generator, dan operasi eksponensial modular yang berkaitan dengan masalah logaritma diskrit.

Menganalisis aspek keamanan protokol Diffie–Hellman, termasuk potensi kerentanan terhadap serangan Man-in-the-Middle (MITM) serta pentingnya autentikasi dalam implementasi kriptografi modern.

---

## 2. Dasar Teori
Protokol Diffie-Hellman memungkinkan dua pihak membentuk kunci rahasia bersama melalui saluran publik tanpa mengirimkan kunci tersebut. Proses ini memanfaatkan bilangan prima, generator, dan operasi eksponensial modular. Keamanan protokol ini bergantung pada kesulitan menyelesaikan masalah logaritma diskrit.

---

## 3. Analisis Serangan MITM

Serangan MITM terjadi karena Diffie-Hellman murni tidak menyediakan mekanisme autentikasi. Penyerang dapat mencegat dan mengganti public key tanpa terdeteksi, sehingga dapat membaca atau memodifikasi komunikasi.

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
import random

# ===============================
# DIFFIE–HELLMAN KEY EXCHANGE
# ===============================

# Parameter publik (disepakati bersama)
p = 23  # bilangan prima
g = 5   # generator

# Private key (rahasia, tidak dibagikan)
a = random.randint(2, p - 2)  # private key Alice
b = random.randint(2, p - 2)  # private key Bob

# Public key
A = pow(g, a, p)  # public key Alice
B = pow(g, b, p)  # public key Bob

# Pembentukan shared secret
shared_secret_alice = pow(B, a, p)
shared_secret_bob   = pow(A, b, p)

# Output
print("=== Diffie–Hellman Key Exchange ===")
print("p (prime)        :", p)
print("g (generator)    :", g)
print("Private key Alice:", a)
print("Private key Bob  :", b)
print("Public key Alice :", A)
print("Public key Bob   :", B)
print("Kunci bersama Alice:", shared_secret_alice)
print("Kunci bersama Bob  :", shared_secret_bob)

# Validasi
if shared_secret_alice == shared_secret_bob:
    print("Status: BERHASIL (kunci sama)")
else:
    print("Status: GAGAL (kunci berbeda)")


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?

Karena kunci rahasia tidak pernah dikirimkan, melainkan dibentuk secara independen oleh kedua pihak menggunakan operasi matematika yang sulit dibalik.

2. Apa kelemahan utama protokol Diffie-Hellman murni?

Tidak memiliki autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle.

3. Bagaimana cara mencegah serangan MITM?

Dengan menambahkan autentikasi seperti sertifikat digital, tanda tangan digital, atau menggunakan protokol aman seperti TLS
## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.

Diffie, W., & Hellman, M. (1976). New Directions in Cryptography. IEEE Transactions on Information Theory, 22(6), 644–654.

Kahn Academy. (n.d.). Modular arithmetic and cryptography.
https://www.khanacademy.org/computing/computer-science/cryptography

Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.

Schneier, B. (2015). Applied Cryptography: Protocols, Algorithms, and Source Code in C (20th Anniversary ed.). Wiley.

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
