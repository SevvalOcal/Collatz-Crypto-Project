import math

def nist_monobit_testi(bit_string):
    """NIST Monobit (Frekans) Testi: P-Değeri hesaplar."""
    n = len(bit_string)
    if n == 0: return 0
    # 1 ve 0 farkının istatistiksel ağırlığı
    s_n = bit_string.count('1') - bit_string.count('0')
    s_obs = abs(s_n) / math.sqrt(n)
    p_value = math.erfc(s_obs / math.sqrt(2))
    return p_value

def ki_kare_testi(bit_string):
    """Ki-Kare (Chi-Square) Testi: Dağılım dengesini ölçer."""
    n = len(bit_string)
    if n == 0: return 0
    n0 = bit_string.count('0')
    n1 = bit_string.count('1')
    beklenen = n / 2
    chi_square = ((n0 - beklenen)**2 / beklenen) + ((n1 - beklenen)**2 / beklenen)
    return chi_square

def rapor_olustur(bit_string):
    p_degeri = nist_monobit_testi(bit_string)
    ki_skoru = ki_kare_testi(bit_string)
    
    print("\n" + "="*50)
    print("🔬 COLLATZ ALGORİTMASI İSTATİSTİKSEL ANALİZ RAPORU")
    print("="*50)
    print(f"📌 Analiz Edilen Toplam Bit : {len(bit_string)}")
    print(f"📌 Ki-Kare (Chi-Square) Skoru: {ki_skoru:.4f}")
    print(f"📌 NIST Monobit P-Değeri     : {p_degeri:.4f}")
    print("-" * 50)
    
    # Kriptografik standart: P > 0.01 ise dizi rastgeledir.
    if p_degeri > 0.01:
        print("✅ SONUÇ: Rastgelelik testi BAŞARILI.")
        print("Açıklama: Dizi istatistiksel olarak güvenli dağılıma sahiptir.")
    else:
        print("❌ SONUÇ: Rastgelelik testi BAŞARISIZ.")
        print("Açıklama: Belirgin bir sapma tespit edildi.")
    print("="*50)

if __name__ == "__main__":
    print("Bu bir modül dosyasıdır, lütfen main.py üzerinden çalıştırın.")
