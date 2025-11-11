# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik:  Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: Lukman Wahyu Permadi  
NIM: 230202814
Kelas:5IKRB 

---

## 1. Tujuan
🔑 Konsep Dasar1. Entropi Kunci (Key Entropy)Entropi mengukur ketidakpastian atau keacakan suatu kunci. Secara sederhana, semakin tinggi entropi, semakin kuat kunci tersebut terhadap serangan brute force.Untuk kunci dengan panjang $L$ bit, jumlah total kemungkinan kunci adalah $N = 2^L$. Entropi $H$ (dalam bit) dihitung sebagai:$$H = \log_2(N) = L$$Jika suatu kunci diambil dari $n$ karakter berbeda (dengan probabilitas yang sama, $p=1/n$) dan panjangnya $m$ karakter, entropi dihitung sebagai:$$H = m \times \log_2(n)$$Contoh Sederhana: Kunci password yang terdiri dari 8 karakter, di mana setiap karakter adalah huruf kecil (26 kemungkinan).$n = 26$$m = 8$$H = 8 \times \log_2(26) \approx 8 \times 4.7$ bit $\approx 37.6$ bit.Jika menggunakan huruf besar, huruf kecil, angka, dan simbol (sekitar 95 karakter), maka $H \approx 8 \times \log_2(95) \approx 8 \times 6.57$ bit $\approx 52.6$ bit.
2. Teorema Euler dan Aritmatika ModularTeorema ini sering digunakan dalam kriptografi kunci publik (seperti RSA) untuk operasi modular, terutama dalam perhitungan invers modular.Teorema Euler: Jika $\gcd(a, n) = 1$, maka:$$a^{\phi(n)} \equiv 1 \pmod{n}$$Di mana $\phi(n)$ adalah fungsi totient Euler, yang menghitung jumlah bilangan bulat positif kurang dari $n$ yang koprima (relatif prima) terhadap $n$.Invers Modular: Invers dari $a$ modulo $n$ (dilambangkan $a^{-1} \pmod{n}$) adalah bilangan $x$ sedemikian ranga $ax \equiv 1 \pmod{n}$. Jika $\gcd(a, n) = 1$, invers ini ada dan dapat dihitung menggunakan Algoritma Euclidean Diperluas atau dengan menggunakan Teorema Euler: $a^{-1} \equiv a^{\phi(n) - 1} \pmod{n}$.
3. Jarak Unicity (Unicity Distance, $L_U$)Unicity distance adalah panjang minimum ciphertext (teks tersandi) yang diperlukan agar kunci yang benar secara statistik menjadi unik, mengesampingkan kunci-kunci lain. Jika panjang ciphertext lebih pendek dari $L_U$, kemungkinan ada lebih dari satu kunci yang akan menghasilkan plaintext yang tampak masuk akal.Rumus Unicity Distance:$$L_U = \frac{H}{D}$$Di mana:$H$ = Entropi kunci (dalam bit).$D$ = Redundansi plaintext (dalam bit/karakter). Redundansi adalah kelebihan informasi dalam bahasa yang memungkinkan suatu pesan tetap dapat dipahami meskipun sebagian hilang.Untuk bahasa Inggris, redundansi $D$ biasanya berkisar antara $\approx 1.5$ hingga $2.0$ bit/karakter. Untuk bahasa Indonesia, nilainya serupa, atau sekitar $\approx 1.8$ bit/karakter.
5. Entropi Kunci ($H$)Entropi mengukur ketidakpastian (keacakan) suatu kunci. Ini adalah logaritma biner dari jumlah total kunci yang mungkin ($N$).$$H = \log_2(N)$$Kunci KuatKunci LemahNilai $H$ Tinggi ($H \ge 128$ bit disarankan).Nilai $H$ Rendah ($H < 80$ bit).Kunci dipilih dari key space yang sangat besar.Kunci pendek atau memiliki banyak karakter yang terbatas.Implikasi: Memerlukan lebih banyak waktu dan daya komputasi yang tidak praktis untuk serangan brute force.Implikasi: Mudah dipecahkan dalam hitungan detik hingga jam oleh cracker modern
6.Serangan brute force adalah upaya sistematis untuk mencoba setiap kemungkinan kunci yang ada. Potensinya dievaluasi dengan menghitung waktu yang dibutuhkan untuk mencoba semua kunci.1. Skenario Kriptosistem Sederhana (Contoh: Vigenère Cipher)Asumsikan Vigenère Cipher menggunakan kunci 5 karakter, hanya terdiri dari 26 huruf kecil.Jumlah Kunci Mungkin ($N$): $26^5 \approx 11.88$ juta.Entropi Kunci ($H$): $H = 5 \times \log_2(26) \approx 23.5$ bit.2. Perhitungan Waktu SeranganAsumsikan kecepatan cracker modern ($R$) mampu menguji $10^9$ kunci per detik (1 miliar/detik).$$\text{Waktu Serangan } (T) = \frac{\text{Jumlah Kunci } (N)}{\text{Kecepatan Uji } (R)}$$$$T = \frac{11,880,000}{1,000,000,000} \text{ detik} \approx 0.01188 \text{ detik}$$

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
