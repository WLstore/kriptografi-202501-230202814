import random
from functools import reduce

# --- FUNGSI MATEMATIKA MODULAR ---
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# --- PROSES SHAMIR SECRET SHARING ---
def split_secret(secret_int, k, n, prime):
    # Membuat koefisien polinomial secara acak (a1, a2, ... ak-1)
    # a0 adalah secret itu sendiri
    coeffs = [secret_int] + [random.randint(0, prime - 1) for _ in range(k - 1)]
    
    def f(x):
        res = 0
        for i, coeff in enumerate(coeffs):
            res = (res + coeff * pow(x, i, prime)) % prime
        return res

    # Membuat n shares (x, f(x))
    return [(i, f(i)) for i in range(1, n + 1)]

def recover_secret(shares, prime):
    def lagrange_interpolation(x, x_s, y_s, p):
        def basis(j):
            num = 1
            den = 1
            for i in range(len(x_s)):
                if i == j: continue
                num = (num * (x - x_s[i])) % p
                den = (den * (x_s[j] - x_s[i])) % p
            return (num * mod_inverse(den, p)) % p
        
        res = 0
        for j in range(len(y_s)):
            res = (res + y_s[j] * basis(j)) % p
        return res

    x_s, y_s = zip(*shares)
    return lagrange_interpolation(0, x_s, y_s, prime)

# --- EKSEKUSI PROGRAM ---
# Gunakan bilangan prima yang lebih besar dari rahasia Anda
PRIME = 2**31 - 1  # Mersenne Prime
SECRET = 230202814 # Contoh menggunakan NIM Anda sebagai rahasia
K = 3 # Threshold
N = 5 # Total Shares

print(f"--- SIMULASI SHAMIR SECRET SHARING ---")
print(f"Rahasia (NIM): {SECRET}")
print(f"Skema: ({K}, {N})")

# 1. Bagi Rahasia
shares = split_secret(SECRET, K, N, PRIME)
print("\nShares yang dihasilkan:")
for s in shares:
    print(f"  Share ke-{s[0]}: {s[1]}")

# 2. Rekonstruksi dengan 3 kunci (Berhasil)
kunci_minimal = shares[:K]
reconstructed = recover_secret(kunci_minimal, PRIME)
print(f"\nRekonstruksi dengan {K} kunci: {reconstructed}")

# 3. Rekonstruksi dengan 2 kunci (Pasti Salah)
kunci_kurang = shares[:K-1]
gagal = recover_secret(kunci_kurang, PRIME)
print(f"Rekonstruksi dengan {K-1} kunci: {gagal} (TIDAK SESUAI)")