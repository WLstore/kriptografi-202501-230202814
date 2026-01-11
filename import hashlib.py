import hashlib

def dictionary_attack():
    # KITA SAMAKAN TARGET DENGAN HASIL HASH DARI KATA 'rahasia123' DI SISTEM ANDA
    kamus = ["123456", "admin", "password", "rahasia123", "qwerty"]
    
    # Target yang sesuai dengan hasil eksekusi Anda sebelumnya
    target_hash = "7f95b733f4210c71482904eb422143f8" 
    
    print(f"[*] Mencari Hash: {target_hash}")
    print("-" * 50)

    for word in kamus:
        # .strip() sangat penting untuk membuang karakter tersembunyi
        clean_word = word.strip()
        hashed_word = hashlib.md5(clean_word.encode('utf-8')).hexdigest()
        
        print(f"[Mencoba] {clean_word.ljust(12)} -> {hashed_word}")

        if hashed_word == target_hash:
            print("-" * 50)
            return f"[+] BERHASIL: Password ditemukan -> {clean_word}"

    return "\n[-] GAGAL: Password tidak ditemukan."

if __name__ == "__main__":
    print(dictionary_attack())