# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik:  Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)  
Nama: Lukman Wahyu Permadi  
NIM: 230202814
Kelas:5IKRB 

---

## 1. Tujuan
Konsep Dasar1. Entropi Kunci (Key Entropy)Entropi mengukur ketidakpastian atau keacakan suatu kunci. Secara sederhana, semakin tinggi entropi, semakin kuat kunci tersebut terhadap serangan brute force.Untuk kunci dengan panjang $L$ bit, jumlah total kemungkinan kunci adalah $N = 2^L$. Entropi $H$ (dalam bit) dihitung sebagai:$$H = \log_2(N) = L$$Jika suatu kunci diambil dari $n$ karakter berbeda (dengan probabilitas yang sama, $p=1/n$) dan panjangnya $m$ karakter, entropi dihitung sebagai:$$H = m \times \log_2(n)$$Contoh Sederhana: Kunci password yang terdiri dari 8 karakter, di mana setiap karakter adalah huruf kecil (26 kemungkinan).$n = 26$$m = 8$$H = 8 \times \log_2(26) \approx 8 \times 4.7$ bit $\approx 37.6$ bit.Jika menggunakan huruf besar, huruf kecil, angka, dan simbol (sekitar 95 karakter), maka $H \approx 8 \times \log_2(95) \approx 8 \times 6.57$ bit $\approx 52.6$ bit.

2. Teorema Euler dan Aritmatika ModularTeorema ini sering digunakan dalam kriptografi kunci publik (seperti RSA) untuk operasi modular, terutama dalam perhitungan invers modular.Teorema Euler: Jika $\gcd(a, n) = 1$, maka:$$a^{\phi(n)} \equiv 1 \pmod{n}$$Di mana $\phi(n)$ adalah fungsi totient Euler, yang menghitung jumlah bilangan bulat positif kurang dari $n$ yang koprima (relatif prima) terhadap $n$.Invers Modular: Invers dari $a$ modulo $n$ (dilambangkan $a^{-1} \pmod{n}$) adalah bilangan $x$ sedemikian ranga $ax \equiv 1 \pmod{n}$. Jika $\gcd(a, n) = 1$, invers ini ada dan dapat dihitung menggunakan Algoritma Euclidean Diperluas atau dengan menggunakan Teorema Euler: $a^{-1} \equiv a^{\phi(n) - 1} \pmod{n}$.

3. Jarak Unicity (Unicity Distance, $L_U$)Unicity distance adalah panjang minimum ciphertext (teks tersandi) yang diperlukan agar kunci yang benar secara statistik menjadi unik, mengesampingkan kunci-kunci lain. Jika panjang ciphertext lebih pendek dari $L_U$, kemungkinan ada lebih dari satu kunci yang akan menghasilkan plaintext yang tampak masuk akal.Rumus Unicity Distance:$$L_U = \frac{H}{D}$$Di mana:$H$ = Entropi kunci (dalam bit).$D$ = Redundansi plaintext (dalam bit/karakter). Redundansi adalah kelebihan informasi dalam bahasa yang memungkinkan suatu pesan tetap dapat dipahami meskipun sebagian hilang.Untuk bahasa Inggris, redundansi $D$ biasanya berkisar antara $\approx 1.5$ hingga $2.0$ bit/karakter. Untuk bahasa Indonesia, nilainya serupa, atau sekitar $\approx 1.8$ bit/karakter.
5. Entropi Kunci ($H$)Entropi mengukur ketidakpastian (keacakan) suatu kunci. Ini adalah logaritma biner dari jumlah total kunci yang mungkin ($N$).$$H = \log_2(N)$$Kunci KuatKunci LemahNilai $H$ Tinggi ($H \ge 128$ bit disarankan).Nilai $H$ Rendah ($H < 80$ bit).Kunci dipilih dari key space yang sangat besar.Kunci pendek atau memiliki banyak karakter yang terbatas.Implikasi: Memerlukan lebih banyak waktu dan daya komputasi yang tidak praktis untuk serangan brute force.Implikasi: Mudah dipecahkan dalam hitungan detik hingga jam oleh cracker modern
6.Serangan brute force adalah upaya sistematis untuk mencoba setiap kemungkinan kunci yang ada. Potensinya dievaluasi dengan menghitung waktu yang dibutuhkan untuk mencoba semua kunci.1. Skenario Kriptosistem Sederhana (Contoh: Vigenère Cipher)Asumsikan Vigenère Cipher menggunakan kunci 5 karakter, hanya terdiri dari 26 huruf kecil.Jumlah Kunci Mungkin ($N$): $26^5 \approx 11.88$ juta.Entropi Kunci ($H$): $H = 5 \times \log_2(26) \approx 23.5$ bit.2. Perhitungan Waktu SeranganAsumsikan kecepatan cracker modern ($R$) mampu menguji $10^9$ kunci per detik (1 miliar/detik).$$\text{Waktu Serangan } (T) = \frac{\text{Jumlah Kunci } (N)}{\text{Kecepatan Uji } (R)}$$$$T = \frac{11,880,000}{1,000,000,000} \text{ detik} \approx 0.01188 \text{ detik}$$

---

## 2. Dasar Teori
Entropi Kunci (Key Entropy)
Entropi merupakan ukuran ketidakpastian atau keacakan dari sebuah sistem kunci. Dalam kriptografi, semakin besar entropi maka semakin besar ruang kunci yang harus diuji oleh penyerang, sehingga sistem menjadi lebih aman. Rumus entropi: H(K)=log2​∣K∣
Semakin besar nilai 
∣
𝐾
∣
∣K∣, maka semakin sulit serangan brute force dilakukan.


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

import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")

## 6. Hasil dan Pembahasan
Analisis:

Entropi Caesar Cipher (4.7 bit) sangat kecil, artinya ruang kunci hanya 26 kemungkinan sehingga sangat mudah dipecahkan.

AES-128 memiliki entropi 128 bit, artinya memiliki 
2
128
2
128
 kemungkinan kunci — sangat besar dan praktis tidak dapat dipecahkan dengan brute force.

Unicity Distance Caesar Cipher (≈0.3) berarti ciphertext yang sangat pendek sudah cukup untuk menentukan kunci, menunjukkan lemahnya keamanan cipher klasik.

Waktu brute force untuk Caesar Cipher sangat kecil (hampir instan), sedangkan AES-128 butuh waktu astronomis bahkan dengan 1 juta percobaan per detik.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
Jawab pertanyaan diskusi yang diberikan pada modul.  
Apa arti dari nilai entropy dalam konteks kekuatan kunci?
Entropy menunjukkan tingkat ketidakpastian atau keacakan kunci. Semakin besar entropi, semakin besar jumlah kemungkinan kunci, sehingga sistem lebih sulit diserang brute force.

Mengapa unicity distance penting dalam menentukan keamanan suatu cipher?
Karena unicity distance menentukan berapa panjang ciphertext yang diperlukan untuk menemukan kunci unik. Cipher dengan unicity distance rendah mudah dipecahkan dengan ciphertext pendek.

Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat?
Karena brute force selalu menjamin hasil jika diberi waktu cukup. Namun, algoritma modern seperti AES memiliki ruang kunci yang sangat besar sehingga brute force tidak praktis dilakukan dalam waktu realistis.

## 8. Kesimpulan
Dari percobaan ini dapat disimpulkan bahwa:

Entropi yang tinggi menunjukkan kekuatan kunci yang lebih baik.

Unicity distance yang besar meningkatkan keamanan terhadap analisis ciphertext.

Serangan brute force masih mungkin secara teori, tetapi tidak efisien untuk algoritma modern seperti AES karena ruang kunci yang sangat besar.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Katz, J., & Lindell, Y. (2021). Introduction to Modern Cryptography. CRC Press.

Menezes, A. J., Van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 1b74725e9eccb1a45333c015626aeaa154172442 (HEAD -> main, origin/main, origin/HEAD)
Author: WLstore <lukmanwahyupermadi@gmail.com>
Date:   Wed Nov 12 08:35:51 2025 +0700

    week4-entropy-unicity

```
