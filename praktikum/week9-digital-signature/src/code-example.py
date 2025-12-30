from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

print("=== PEMBUATAN TANDA TANGAN DIGITAL RSA ===")

# Generate pasangan kunci RSA (2048-bit)
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("Kunci RSA berhasil dibuat")

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
hash_message = SHA256.new(message)

# Membuat tanda tangan digital dengan private key
signature = pkcs1_15.new(private_key).sign(hash_message)

print("Pesan            :", message.decode())
print("Signature (hex)  :", signature.hex())
