# Laporan Praktikum Kriptografi
Minggu ke-: 02  
Topik: [Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)]  
Nama: [Lukman Wahyu Permadi]
NIM: [230202815]  
Kelas: [5IKRb]  

## 1. Tujuan

   1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
   2  Menggambarkan proses enkripsi dan dekripsi sederhana.
   3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori

 1. Cryptosystem (Sistem Kriptografi) adalah sekumpulan algoritma dan prosedur yang digunakan untuk mengamankan data dengan cara mengubah pesan asli (plaintext) menjadi bentuk yang tidak dapat dibaca (ciphertext), serta mengembalikannya lagi ke bentuk semula dengan proses tertentu.
 
 2. Komponen Utama Cryptosystem
 
- Plaintext = Pesan asli yang dapat dibaca sebelum dienkripsi. Contoh: “Halo Dunia”.
    
- Ciphertext = Hasil dari proses enkripsi, berupa teks acak yang tidak bisa dibaca. Contoh: “Xz@12!kL”.
    
- Encryption Algorithm (Algoritma Enkripsi) = Metode atau rumus matematika yang digunakan untuk mengubah plaintext menjadi ciphertext. Contoh: AES, DES, RSA.
    
- Decryption Algorithm (Algoritma Dekripsi) = Metode untuk mengubah ciphertext kembali menjadi plaintext dengan kunci tertentu.
    
- Key (Kunci Kriptografi) = Nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi. Tanpa kunci yang benar, pesan tidak dapat dikembalikan ke bentuk
    aslinya.
- Key Management (Manajemen Kunci) = Proses pembuatan, distribusi, dan penyimpanan kunci secara aman.
   
 3. Konsep Dasar Cryptosystem
- Enkripsi (Encryption) adalah Proses mengubah plaintext menjadi ciphertext menggunakan algoritma dan kunci.
- Dekripsi (Decryption) adalah Proses mengembalikan ciphertext ke bentuk plaintext menggunakan algoritma dan kunci tertentu.
- Kunci (Key) menjadi faktor utama keamanan. Jika kunci diketahui pihak lain, maka sistem tidak lagi aman.

 4.
A. Kriptografi Simetris

   Pengertian:
   Kriptografi simetris menggunakan satu kunci yang sama untuk proses enkripsi (mengubah plaintext menjadi ciphertext) dan dekripsi (mengubah ciphertext kembali ke plaintext).Artinya, pengirim dan penerima harus memiliki kunci yang sama dan menjaganya tetap rahasia.

   Contoh algoritma:

- AES (Advanced Encryption Standard) → digunakan secara luas untuk enkripsi file, jaringan Wi-Fi (WPA2), dan data digital.

- DES (Data Encryption Standard) → algoritma lama, kini jarang digunakan karena ukuran kuncinya kecil (56-bit) dan mudah diserang brute force
   
B. Kriptografi Asimetris

Pengertian:
Kriptografi asimetris menggunakan dua kunci yang berbeda, yaitu:

- Kunci publik (public key) → digunakan untuk enkripsi

- Kunci privat (private key) → digunakan untuk dekripsi

- Kunci publik dapat disebarluaskan secara bebas, sedangkan kunci privat harus dijaga kerahasiaannya.

Contoh algoritma:

- RSA (Rivest–Shamir–Adleman) → digunakan untuk keamanan pada HTTPS, email, dan tanda tangan digital.

- ECC (Elliptic Curve Cryptography) → menawarkan keamanan tinggi dengan ukuran kunci lebih kecil dibanding RSA.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code
- Git dan akun GitHub  
- Excalidraw

---

## 4. Langkah Percobaan

1. Membuat file `simple_crypto.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python simple_crypto.py`.)

---

## 5. Source Code
# file: praktikum/week2-cryptosystem/src/simple_crypto.py

      def encrypt(plaintext, key):
          result = ""
          for char in plaintext:
              if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
       return result

      def decrypt(ciphertext, key):
          result = ""
          for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

      if __name__ == "__main__":
          message = "subhan"
          key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
---

## 6. Hasil dan Pembahasan
 
Hasil eksekusi program simple_crypto:

![Hasil Eksekusi](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
 1. Komponen utama dalam kriptosistem meliputi:

- Plaintext, yaitu pesan asli yang masih dapat dibaca sebelum dienkripsi.

- Ciphertext, yaitu hasil enkripsi berupa teks acak yang tidak dapat dibaca.

- Encryption Algorithm (Algoritma Enkripsi), yaitu metode untuk mengubah plaintext menjadi ciphertext.

- Decryption Algorithm (Algoritma Dekripsi), yaitu metode untuk mengembalikan ciphertext menjadi plaintext.

- Key (Kunci Kriptografi), yaitu nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi.

- Key Management (Manajemen Kunci), yaitu proses pembuatan, distribusi, serta penyimpanan kunci secara aman.

 2. A (Sistem Simetris)
 
  Kelebihan
- Proses enkripsi dan dekripsi lebih cepat dan efisien, terutama untuk data dalam jumlah besar.
- Algoritmanya lebih sederhana dan membutuhkan sumber daya komputasi yang lebih sedikit.

  Kelemahan
- Distribusi kunci sulit karena harus dikirim secara rahasia ke penerima.
- Jika kunci diketahui pihak lain, seluruh komunikasi menjadi tidak aman.

    B. (Sistem Asimetris)

  Kelebihan
- Distribusi kunci lebih aman karena menggunakan dua kunci (publik dan privat).
- Mendukung tanda tangan digital dan autentikasi.

  Kelemahan
- Proses lebih lambat karena perhitungan matematikanya kompleks.
- Membutuhkan sumber daya komputasi lebih besar.

 3. Distribusi kunci menjadi masalah utama dalam kriptografi simetris karena sistem ini menggunakan satu kunci yang sama untuk enkripsi dan dekripsi. Artinya, kunci tersebut harus dikirimkan kepada penerima dengan cara yang benar-benar aman.Jika kunci tersebut bocor, disadap, atau dicuri selama proses pengiriman, maka pihak yang tidak berwenang dapat dengan mudah mendekripsi semua pesan rahasia. Oleh karena itu, tantangan terbesar dari kriptografi simetris adalah menjaga kerahasiaan kunci selama proses distribusi.
## 8. Kesimpulan
  Dalam kriptosistem, proses enkripsi dan dekripsi berperan penting untuk menjaga kerahasiaan dan keamanan informasi. Enkripsi mengubah pesan asli (plaintext) menjadi bentuk acak (ciphertext) menggunakan algoritma dan kunci, sehingga pesan tidak dapat dibaca oleh pihak yang tidak berwenang. Sebaliknya, dekripsi mengembalikan ciphertext menjadi plaintext dengan menggunakan kunci yang sesuai.

  Keamanan sistem ini sepenuhnya bergantung pada kerahasiaan kunci dan kekuatan algoritma yang digunakan. Oleh karena itu, manajemen kunci menjadi aspek yang sangat penting agar data tetap aman dari penyadapan atau akses ilegal

---

## 9. Daftar Pustaka
  
- Niko P. *Enkripsi simetris vs asimetris: kapan harus menggunakan masing-masing*.  
- Suyanto. *Enkripsi Simetris dan Asimetris*.  

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week02
Author: Subhan Susilo <Subhansusilo4@gmail.com>
Date:   2025-10-10

    week2-cryptosystem: implementasi simple_crypto dan laporan )
```
