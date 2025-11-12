# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi) 
Nama: Lukman Wahyu Permadi
NIM: 230202814
Kelas: 5IKRA  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami dan mengimplementasikan algoritma kriptografi klasik, yaitu Caesar Cipher, Vigenère Cipher, dan Transposisi Cipher. Setelah praktikum ini mahasiswa diharapkan mampu:

Mengimplementasikan enkripsi dan dekripsi dengan Caesar Cipher.

Mengimplementasikan Vigenère Cipher dengan kunci berbeda.

Menggunakan metode Transposisi untuk menyusun ulang karakter pesan.

Menjelaskan kelemahan cipher klasik terhadap analisis frekuensi dan serangan brute force.

## 2. Dasar Teori
Cipher klasik adalah teknik penyandian sederhana yang digunakan sebelum munculnya kriptografi modern. Terdapat dua jenis utama: cipher substitusi dan cipher transposisi.

1. Caesar Cipher
Caesar Cipher merupakan algoritma substitusi monoalfabetik, di mana setiap huruf digeser sejauh n posisi dalam alfabet. Misalnya dengan pergeseran 3, huruf A menjadi D, B menjadi E, dan seterusnya. Kelemahannya adalah jumlah kemungkinan kunci yang sangat kecil (hanya 25), sehingga mudah dipecahkan melalui analisis frekuensi atau brute force.

2. Vigenère Cipher
Vigenère Cipher merupakan pengembangan dari Caesar Cipher dengan menggunakan kunci berupa kata. Setiap huruf kunci menentukan pergeseran huruf berbeda, sehingga cipher ini termasuk polyalphabetic substitution. Meskipun lebih kuat daripada Caesar, Vigenère masih dapat dipecahkan dengan metode Kasiski examination atau frequency attack jika ciphertext cukup panjang.

3. Transposisi Cipher
Berbeda dari substitusi, Transposisi Cipher tidak mengganti huruf, tetapi menukar posisi huruf dalam plaintext berdasarkan pola tertentu. Keamanannya terletak pada panjang kunci dan kompleksitas permutasi yang digunakan.

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
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

## 6. Hasil dan Pembahasan
Caesar Cipher berhasil melakukan pergeseran huruf sesuai nilai kunci. Hasil dekripsi identik dengan plaintext, menunjukkan algoritma bekerja benar.

Vigenère Cipher menyesuaikan pergeseran berdasarkan huruf kunci, menghasilkan ciphertext berbeda untuk huruf yang sama, menunjukkan sifat polyalphabetic.

Transposisi Cipher hanya mengubah urutan huruf tanpa mengubah karakter, sehingga hasil dekripsi dapat mengembalikan teks asli.

Ketiga algoritma bekerja sesuai teori, namun tingkat keamanannya rendah karena masih bisa dianalisis dengan metode statistik dan frekuensi huruf. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](hasil5/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)


---

## 7. Jawaban Pertanyaan
Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
Caesar Cipher mudah dipecahkan dengan brute force karena hanya memiliki 25 kemungkinan kunci.
Vigenère Cipher meskipun lebih kuat, tetap rentan terhadap frequency analysis dan Kasiski examination jika panjang ciphertext cukup besar.

Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
Karena distribusi huruf pada bahasa alami (seperti bahasa Inggris atau Indonesia) tidak seragam. Huruf tertentu seperti "E" atau "A" muncul lebih sering, sehingga pola tersebut bisa digunakan untuk menebak substitusi huruf.(Jawab pertanyaan diskusi yang diberikan pada modul.  


## 8. Kesimpulan
Dari praktikum ini dapat disimpulkan bahwa algoritma cipher klasik seperti Caesar, Vigenère, dan Transposisi merupakan dasar penting dalam kriptografi, namun tidak lagi aman digunakan karena mudah dipecahkan melalui analisis statistik atau brute force.
Meskipun demikian, pemahaman cipher klasik membantu memahami prinsip dasar penyandian dalam algoritma modern.

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

Katz, J., & Lindell, Y. (2021). Introduction to Modern Cryptography. CRC Press.

Singh, S. (1999). The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography.

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 3775c2dcf997c09a3644f1cac01c8e29ba48d5f5 (HEAD -> main, origin/main, origin/HEAD)
Author: WLstore <lukmanwahyupermadi@gmail.com>
Date:   Wed Nov 12 08:52:52 2025 +0700

    week5-cipher-klasik