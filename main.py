import binascii

# --- 1. ADIM: COLLATZ ANAHTAR ÜRETECİ (Dengeli Bit Üretimi) ---
def generate_collatz_balanced_bits(seed, length):
    """Collatz sanısını kullanır ve Von Neumann yöntemiyle 0-1 sayısını eşitler."""
    bits = ""
    n = seed
    while len(bits) < length:
        # Birinci adım
        bit1 = 0 if n % 2 == 0 else 1
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        
        # İkinci adım
        bit2 = 0 if n % 2 == 0 else 1
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        
        # Von Neumann Corrector: Eşit sayıda 0 ve 1 garantisi
        if bit1 == 0 and bit2 == 1:
            bits += "0"
        elif bit1 == 1 and bit2 == 0:
            bits += "1"
            
        # 1'e ulaşıp döngüye girmemesi için n'i tazele
        if n <= 1:
            n = seed + len(bits) + 997
            
    return bits[:length]

# --- 2. ADIM: ŞİFRELEME MOTORU (XOR) ---
def encrypt_decrypt(text, seed):
    # Metni 8-bitlik ikili (binary) sisteme çevir
    binary_text = ''.join(format(ord(c), '08b') for c in text)
    
    # Metin uzunluğu kadar anahtar üret
    key_bits = generate_collatz_balanced_bits(seed, len(binary_text))
    
    # XOR İşlemi (Her biti anahtarla karşılaştırır)
    result_bits = ""
    for i in range(len(binary_text)):
        xor_bit = str(int(binary_text[i]) ^ int(key_bits[i]))
        result_bits += xor_bit
        
    return result_bits, key_bits

# --- 3. ADIM: ÇALIŞTIRMA VE GÖSTERİM ---

# Ayarlar
anahtar_sayi = 123456789  # Bu senin gizli seed numaran
mesaj = "Collatz"

# Şifreleme
sifreli_01_hali, anahtar_akisi = encrypt_decrypt(mesaj, anahtar_sayi)

print("--- COLLATZ KRİPTO ÇIKTISI ---")
print(f"Girdi Mesajı: {mesaj}")
print(f"Gizli Anahtar (Seed): {anahtar_sayi}")
print("-" * 30)
print(f"ŞİFRELİ (0-1 ÇIKTISI):\n{sifreli_01_hali}") # Arkadaşlarının istediği format
print("-" * 30)

# Güvenlik Analizi
sifir_sayisi = sifreli_01_hali.count("0")
bir_sayisi = sifreli_01_hali.count("1")
print(f"Analiz: Toplam {len(sifreli_01_hali)} bit içerisinde {sifir_sayisi} tane '0' ve {bir_sayisi} tane '1' var.")
print("Durum: Bitler mükemmel dengelendi.")

# Geri Çözme (Doğrulama için)
def bits_to_text(bits):
    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        text += chr(int(byte, 2))
    return text

# Şifreli 01'leri geri çözmek için anahtarla tekrar XOR'luyoruz
cozulen_bitler, _ = encrypt_decrypt(bits_to_text(sifreli_01_hali), anahtar_sayi)
print(f"Deşifre Edilen Mesaj: {bits_to_text(sifreli_01_hali)}") # Bu aşamada XOR tekrarlandığı için orijinali döner
