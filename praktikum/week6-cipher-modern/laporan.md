# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: Cipher Modern (DES, AES, RSA)
Nama: Lukman Wahyu Permadi
NIM: 230202814
Kelas: 5IKRA  

---

## 1. Tujuan
Mengimplementasikan algoritma DES pada data blok sederhana.

Menggunakan algoritma AES 128-bit untuk proses enkripsi dan dekripsi.

Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
## 2. Dasar Teori
Program Python untuk algoritma AES, RSA, serta DES (opsional).

Screenshot hasil eksekusi program enkripsi dan dekripsi.

Laporan yang menjelaskan implementasi, teori, dan jawaban pertanyaan diskusi.

Commit Git dengan format: week6-cipher-modern.

## 3. Alat dan Bahan
Membuat folder:

praktikum/week6-cipher-modern/
├─ src/
├─ screenshots/
└─ laporan.md


Menggunakan Python 3.11+

Menginstal library PyCryptodome:

pip install pycryptodome


Referensi utama materi: Stallings (2017), Bab 3–4

## 4. Langkah Percobaan
4.1 Program DES (Opsional)
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)

4.2 Program AES-128
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())

4.3 Program RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
## 5. Source Code
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
---

## 6. Hasil dan Pembahasan
Pesan berhasil dienkripsi menggunakan public key.

Pesan berhasil didekripsi menggunakan private key, sesuai konsep asimetris.

DES (Opsional)

DES mengenkripsi blok 8 byte.

Hasil dekripsi kembali sama persis dengan plaintext.

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan
Algoritma	Jenis	Panjang Kunci	Keamanan	Keterangan
DES	Simetris	56 bit	Lemah	Mudah di-bruteforce, sudah tidak digunakan
AES	Simetris	128/192/256 bit	Sangat kuat	Standar modern, cepat & aman
RSA	Asimetris	1024–4096 bit	Sangat kuat	Digunakan untuk enkripsi kunci atau digital signature

DES & AES → memerlukan kunci yang sama untuk enkripsi dan dekripsi.
RSA → menggunakan dua kunci berbeda (publik & privat).

2. Mengapa AES lebih banyak digunakan dibanding DES di era modern?

Kunci DES hanya 56-bit, sehingga dapat dipecahkan kurang dari 24 jam dengan perangkat modern.

AES memiliki kunci 128–256 bit, sangat kuat dan cepat.

AES sudah menjadi standar internasional (NIST) dalam keamanan modern.

3. Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?

RSA disebut asimetris karena:

Enkripsi menggunakan public key

Dekripsi menggunakan private key

Proses pembangkitan kunci RSA:

Memilih dua bilangan prima besar, p dan q

Menghitung modulus:

𝑛
=
𝑝
×
𝑞
n=p×q

Menghitung totient:

𝜙
(
𝑛
)
=
(
𝑝
−
1
)
(
𝑞
−
1
)
ϕ(n)=(p−1)(q−1)

Memilih e (public exponent) yang coprime terhadap φ(n)

Menghitung d sebagai invers dari e:

𝑑
≡
𝑒
−
1
m
o
d
 
 
𝜙
(
𝑛
)
d≡e
−1
modϕ(n)

Public key → (e, n)
Private key → (d, n)

## 8. Kesimpulan
Pada praktikum Week 6 ini, mahasiswa telah memahami dan mengimplementasikan tiga algoritma kriptografi modern, yaitu DES, AES, dan RSA. Melalui proses coding dan pengujian, mahasiswa dapat melihat bagaimana data dienkripsi dan didekripsi menggunakan berbagai teknik cipher. DES digunakan sebagai contoh cipher blok generasi awal yang kini sudah dianggap kurang aman, sedangkan AES terbukti lebih kuat berkat ukuran kunci yang lebih besar dan struktur algoritma yang lebih efisien, sehingga menjadi standar modern dalam keamanan data. RSA memperkenalkan konsep kriptografi kunci publik yang memungkinkan proses enkripsi dan dekripsi dilakukan dengan pasangan kunci berbeda, serta digunakan secara luas dalam keamanan komunikasi digital.
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
Author: lukmanwahyupermadi@gmail.com
Date:   2025-11-17

    week6-cipher-modern

