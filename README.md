# Praktikum Kriptografi – TinyCoin (20251)

Repositori ini merupakan template praktikum untuk mata kuliah Kriptografi semester gasal 2025/2026, dengan studi kasus TinyCoin – mulai dari cipher klasik, kriptografi modern, tanda tangan digital, hingga implementasi cryptocurrency dan Web3.

Mahasiswa diharapkan dapat membangun pemahaman menyeluruh tentang kriptografi, dimulai dari konsep dasar hingga aplikasi modern dalam bentuk prototipe blockchain (TinyChain) dan token ERC-20 (TinyCoin).

---

## Instruksi Praktikum
1. Lakukan fork repositori ini ke akun GitHub masing-masing.
2. Ubah nama hasil fork dengan format:
   ```
   kripto-202501-<nim>
   ```
   Contoh: `kripto-202501-2310112345`
3. Clone repositori tersebut ke komputer lokal dengan perintah:
   ```bash
   git clone https://github.com/<username>/kripto-20251-<nim>.git
   ```
4. Tambahkan remote upstream untuk sinkronisasi dengan repositori dosen:
   ```bash
   git remote add upstream https://github.com/mhbahara/kriptografi-202501.git
   ```
5. Lakukan sinkronisasi secara berkala dengan perintah:
   ```bash
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```
6. Kerjakan tugas mingguan sesuai instruksi pada folder [docs/](docs/).
7. Simpan kode program pada folder [praktikum/](praktikum/) dengan struktur yang rapi.
8. Setiap minggu lakukan commit dan push dengan format pesan yang sesuai, misalnya:
   - `week1-intro-cia`
   - `week3-modmath-gcd`
   - `week6-aes-rsa`
   - `week13-tinychain-pow`
   - `week15-tinycoin-erc20`
9. Setiap tugas wajib dilengkapi dengan:
   - Kode program
   - Tangkapan layar hasil eksekusi
   - Commit log sesuai instruksi
   - Laporan singkat dalam format Markdown atau PDF

---

## Struktur Folder
```
kriptografi-202501/
 ├─ README.md                       # Panduan umum repositori
 ├─ docs/                           # Panduan praktikum mingguan (Markdown)
 │   ├─ 00_pendahuluan.md
 │   ├─ 01_cryptosystem_intro.md
 │   ├─ 02_modular_math.md
 │   ├─ 03_entropy_unicity.md
 │   ├─ 04_cipher_klasik.md
 │   ├─ 05_cipher_modern.md
 │   ├─ 06_diffie_hellman.md
 │   ├─ 07_signature_pki.md
 │   ├─ 08_secret_sharing.md
 │   ├─ 09_aplikasi_tls.md
 │   ├─ 10_blockchain_intro.md
 │   ├─ 11_tinychain_pow.md
 │   ├─ 12_analisis_serangan.md
 │   ├─ 13_tinycoin_erc20.md
 │   ├─ 14_proyek_tim.md
 │   └─ 15_uas_demo.md
 ├─ praktikum/                      # Folder tugas mingguan
 │   ├─ week1-intro-cia/
 │   ├─ week2-cryptosystem/
 │   ├─ week3-modmath-gcd/
 │   ├─ week4-entropy-unicity/
 │   ├─ week5-cipher-klasik/
 │   ├─ week6-cipher-modern/
 │   ├─ week7-diffie-hellman/
 │   ├─ week8-uts/
 │   ├─ week9-digital-signature/
 │   ├─ week10-pki/
 │   ├─ week11-secret-sharing/
 │   ├─ week12-aplikasi-tls/
 │   ├─ week13-tinychain/
 │   ├─ week14-analisis-serangan/
 │   ├─ week15-tinycoin-erc20/
 │   └─ week16-uas/
 ├─ blockchain/                     # Proyek DIY Blockchain (TinyChain)
 ├─ contracts/                      # Proyek Smart Contract (TinyCoin ERC-20)
 ├─ frontend/                       # DApp sederhana (opsional)
 └─ report/                         # Laporan akhir tim
```

---

## Sistem Penilaian
Praktikum ini mencakup 60–70% dari total penilaian mata kuliah yang terdiri atas tugas, praktikum, dan partisipasi.  
- Penilaian Proyek (TinyChain dan TinyCoin): 35%  
- Tugas individu (kuis, laporan mingguan, commit): 25%  
- Penilaian partisipasi: 5%  
- Ujian Tengah Semester (UTS): 15%  
- Ujian Akhir Semester (UAS): 20%  

---

## Referensi Utama
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*  
- Stallings, W. *Cryptography and Network Security*  
- Narayanan, A. et al. *Bitcoin and Cryptocurrency Technologies*  
- Antonopoulos, A. M. *Mastering Bitcoin*  
- Ethereum & Solidity Documentation (OpenZeppelin, Hardhat, Foundry)  

---

## Lisensi
Repositori ini menggunakan lisensi MIT. Pemanfaatan dan modifikasi diperkenankan dengan tetap mencantumkan atribusi yang sesuai.
