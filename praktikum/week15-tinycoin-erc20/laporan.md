# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik: week15-tinycoin-erc20
Nama: Lukman Wahyu Permadi
NIM: 230202814
Kelas: 5IKRA 

---

## 1. Tujuan

Mengembangkan proyek sederhana berbasis algoritma kriptografi (smart contract).

Mendokumentasikan proses implementasi proyek ke dalam repository Git.

Menyusun laporan teknis hasil proyek akhir terkait standar token ERC20.

---

## 2. Dasar Teori
ERC20 adalah standar teknis yang digunakan untuk smart contract di blockchain Ethereum dalam mengimplementasikan token. Standar ini menetapkan sekumpulan aturan yang memungkinkan token untuk dibagikan, ditukar dengan token lain, atau ditransfer ke dompet kripto. Penggunaan interface standar seperti ERC20 memastikan interoperabilitas antara berbagai aplikasi terdesentralisasi (dApps) dan bursa (exchanges).

Dalam konteks kriptografi, keamanan smart contract sangat bergantung pada integritas kode Solidity. Sejak versi 0.8.0, Solidity telah menyertakan pemeriksaan bawaan untuk overflow dan underflow aritmetika, yang sebelumnya merupakan celah keamanan fatal. Penggunaan library OpenZeppelin semakin memperkuat keamanan karena menyediakan implementasi standar yang telah diaudit secara luas oleh komunitas global.
---

## 3. Alat dan Bahan
Remix IDE (Web-based) untuk penulisan dan deployment smart contract.

Solidity 0.8.x (Bahasa pemrograman smart contract).

OpenZeppelin Contracts Library (Standar industri untuk ERC20).

MetaMask (Wallet untuk interaksi dengan testnet).

Ethereum Testnet (Sepolia/Goerli) atau Remix VM.

Git untuk version control.

---

## 4. Langkah Percobaan
Membuat struktur folder praktikum/week15-tinycoin-erc20/ beserta sub-folder contracts/ dan screenshots/.

Membuka Remix IDE dan membuat file baru bernama TinyCoin.sol di dalam folder contracts/.

Menuliskan kode smart contract dengan mengimpor library ERC20 dari OpenZeppelin.

Melakukan kompilasi (compile) menggunakan compiler Solidity versi 0.8.x.

Melakukan deployment kontrak melalui tab "Deploy & Run Transactions" di Remix IDE.

Melakukan pengujian fungsi totalSupply, balanceOf, dan mencoba melakukan transfer token ke alamat address lain.

Mendokumentasikan hasil transaksi dan menyimpan laporan dalam file laporan.md.
---

## 5. Source Code
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Mengimpor standar ERC20 dari OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    /**
     * @dev Constructor yang memberikan supply awal kepada pembuat kontrak.
     * @param initialSupply Jumlah token awal (dalam satuan wei).
     */
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        // Mencetak (minting) token ke alamat pengirim (deployer)
        _mint(msg.sender, initialSupply);
    }
}

---

## 6. Hasil dan Pembahasan
(Deployment: Kontrak berhasil di-deploy pada jaringan [Sebutkan Jaringan, misal: Remix VM (London)]. Alamat kontrak dihasilkan secara otomatis.

Pengujian Fungsi:

balanceOf: Alamat deployer menunjukkan saldo yang sesuai dengan initialSupply yang dimasukkan saat deployment.

transfer: Fungsi transfer berhasil memindahkan sejumlah token TNC ke address tujuan tanpa error.

Analisis Keamanan: Penggunaan Solidity 0.8.x secara otomatis menangani risiko integer overflow. Risiko Reentrancy pada fungsi transfer standar ERC20 OpenZeppelin juga minimal karena state update dilakukan sebelum pengiriman (Checks-Effects-Interactions pattern).

Hasil eksekusi program TinyCoin:

![Hasil Eksekusi](hasil/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
Apa fungsi utama ERC20 dalam ekosistem blockchain? Fungsi utamanya adalah menyediakan standar interface yang seragam. Hal ini memungkinkan developer dompet, bursa, dan dApps lain untuk berinteraksi dengan token baru secara instan tanpa perlu memodifikasi kode mereka secara khusus untuk setiap token.

Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20? Mekanisme transfer bekerja dengan memanipulasi state variable (biasanya sebuah mapping dari address ke uint256). Saat fungsi transfer(recipient, amount) dipanggil, kontrak akan mengecek apakah saldo pengirim cukup, lalu mengurangi saldo pengirim dan menambah saldo penerima dalam database blockchain kontrak tersebut.

Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya? Risiko utama meliputi Reentrancy attack, Integer Overflow/Underflow, dan Access Control issues. Mitigasinya adalah dengan menggunakan versi compiler terbaru (0.8+), menggunakan library yang teruji seperti OpenZeppelin, serta melakukan audit keamanan dan pengujian menyeluruh pada testnet sebelum dipindahkan ke mainnet.
---

## 8. Kesimpulan
Percobaan ini berhasil mengimplementasikan token ERC20 bernama TinyCoin menggunakan Solidity dan library OpenZeppelin. Melalui praktikum ini, dipahami bahwa standar ERC20 mempermudah penciptaan aset digital yang dapat saling beroperasi dalam ekosistem Ethereum dengan keamanan yang terjaga melalui audit library dan fitur compiler terbaru.
---

## 9. Daftar Pustaka
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson.

OpenZeppelin Docs. ERC20 Token Standard. https://docs.openzeppelin.com/contracts/4.x/erc20

Solidity Documentation. Version 0.8.0 Release Notes.

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
