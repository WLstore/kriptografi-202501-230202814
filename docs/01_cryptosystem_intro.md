# 01 Cryptosystem Intro

## Tujuan Pembelajaran
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1. Menjelaskan konsep dasar sistem kriptografi (cryptosystem) dan komponennya.
2. Membedakan kriptografi simetris dan asimetris pada tingkat konsep.
3. Mengimplementasikan fungsi enkripsi dan dekripsi sederhana.
4. Menyajikan bukti eksekusi, pengujian, dan penjelasan hasil dalam laporan singkat.

## Capaian Kegiatan
Pada akhir sesi ini mahasiswa menghasilkan:
- Program `caesar_cipher.py` yang dapat melakukan enkripsi dan dekripsi dengan pergeseran alfabet.
- Tangkapan layar hasil eksekusi program.
- Berkas `laporan.md` berisi penjelasan singkat (maksimal 2 halaman).

---

## Persiapan Lingkungan
1. Pastikan Python 3.11 atau lebih baru terpasang.
2. Siapkan struktur folder berikut pada repositori Anda:
   ```
   praktikum/week2-cryptosystem/
     \- src/
   ```
3. Buka terminal pada direktori repositori.

---

## Panduan Langkah demi Langkah

### Langkah 1 — Membuat Berkas Program
Buat berkas berikut di `praktikum/week2-cryptosystem/src/caesar_cipher.py` lalu salin kode di bawah ini.

```python
"""
Caesar Cipher Sederhana
- Hanya menggeser huruf A-Z atau a-z.
- Karakter non-alfabet (spasi, angka, tanda baca) tidak diubah.
"""

def encrypt(plaintext, key):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            # normalisasi ke 0-25, geser, lalu kembalikan ke kode ASCII awal
            ciphertext.append(chr((ord(char) - shift + key) % 26 + shift))
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def decrypt(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            plaintext.append(chr((ord(char) - shift - key) % 26 + shift))
        else:
            plaintext.append(char)
    return "".join(plaintext)

def main():
    message = "Kriptografi Modern"
    key = 3

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext :", message)
    print("Ciphertext:", encrypted)
    print("Decrypted :", decrypted)

if __name__ == "__main__":
    main()
```

Simpan berkas setelah menyalin kode.

### Langkah 2 — Menjalankan Program
Jalankan perintah berikut dari akar repositori (sesuaikan path jika diperlukan).

**Windows (PowerShell):**
```powershell
python .\praktikum\week2-cryptosystem\src\caesar_cipher.py
```

**Linux/macOS (bash):**
```bash
python3 praktikum/week2-cryptosystem/src/caesar_cipher.py
```

### Ekspektasi Keluaran
Contoh keluaran yang diharapkan (bergantung pada pesan dan kunci):

```
Plaintext : Kriptografi Modern
Ciphertext: Nulswrjudil Prghuq
Decrypted : Kriptografi Modern
```

Apabila hasil dekripsi tidak sama dengan plaintext, periksa kembali logika pergeseran dan penggunaan kode ASCII dasar (65 untuk huruf besar, 97 untuk huruf kecil).

### Langkah 3 — Uji Coba Mandiri
Tambahkan blok pengujian sederhana di akhir berkas (sebelum pemanggilan `main()` atau menggunakan assert terpisah) untuk memverifikasi beberapa kasus.

Contoh uji cepat (opsional, boleh ditempatkan di fungsi `main()`):
```python
# Uji invariansi: decrypt(encrypt(m, k), k) == m
test_message = "Abc Z!"
for k in (1, 5, 13, 25):
    assert decrypt(encrypt(test_message, k), k) == test_message
```

Jika tidak ada assertion error, berarti fungsi dasar berjalan sesuai harapan.

---

## Diskusi Konsep
1. Mengapa Caesar Cipher tidak aman untuk penggunaan modern?
2. Sebutkan perbedaan utama kriptografi simetris dan asimetris dari sisi kunci dan performa.
3. Berikan satu contoh skenario di dunia nyata yang cocok untuk kriptografi simetris, dan satu contoh untuk asimetris.

---

## Tugas yang Dikumpulkan
1. Berkas `caesar_cipher.py` yang berjalan dengan baik.
2. Tangkapan layar hasil eksekusi program (terminal).
3. Berkas `laporan.md` yang berisi:
   - Deskripsi singkat fungsi `encrypt` dan `decrypt`.
   - Penjelasan hasil uji coba (minimal 2 skenario kunci berbeda).
   - Jawaban singkat untuk tiga pertanyaan pada bagian Diskusi Konsep.

Simpan semua berkas pada:
```
praktikum/week2-cryptosystem/
  |- src/caesar_cipher.py
  |- screenshots/    (tangkapan layar)
  |- laporan.md
```

---

## Catatan Lanjutan (Opsional)
Bagi mahasiswa yang ingin melanjutkan eksplorasi:
- Modifikasi program agar dapat menerima `plaintext` dan `key` dari argumen baris perintah.
- Tambahkan validasi input (misalnya, memastikan `key` berupa bilangan bulat).
- Implementasikan varian ROT13 (key = 13) dan jelaskan sifat khususnya.