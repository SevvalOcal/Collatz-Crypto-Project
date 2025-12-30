# 🛡️ Collatz-Balance: Binary Stream Cipher

Bu proje, **Collatz Sanısı** ($3n + 1$) matematiksel modelini kullanarak tasarlanmış bir kriptografik şifreleme algoritmasıdır. Algoritmanın temel amacı, deterministik bir kaosu kullanarak güvenli ve dengeli bir anahtar akışı (Key Stream) üretmektir.

---

## 🚀 Algoritma Nasıl Çalışır? (Akış Şeması)

Sistem üç temel aşamadan oluşur:

1.  **Anahtar Üretimi (Collatz):** Kullanıcının girdiği başlangıç sayısı (Seed), Collatz yörüngesine sokulur. Sayının her adımındaki tek/çift durumu ham bitleri (0 ve 1) oluşturur.
2.  **Dengeleme (Von Neumann Corrector):** Collatz dizisindeki istatistiksel sapmaları önlemek için bitler çiftler halinde kontrol edilir:
    * `01` gelirse -> `0` çıktısı verilir.
    * `10` gelirse -> `1` çıktısı verilir.
    * `00` veya `11` durumları elenir. 
    * *Bu yöntem, çıktıdaki 0 ve 1 sayısının eşit olmasını garanti eder.*
3.  **XOR Maskeleme:** Elde edilen dengeli anahtar dizisi, orijinal metnin bitleri ile XOR işlemine sokularak şifreli **0-1 çıktısı** üretilir.



---

## 📝 Anahtar Üreteci Sözde Kodu (Pseudocode)

```text
BAŞLA
  GİRDİ: Seed_Sayı, Metin
  DÖNGÜ: İhtiyaç duyulan bit uzunluğu dolana kadar
    Sayı Çift ise: Sayı = Sayı / 2, Bit = 0
    Sayı Tek ise: Sayı = 3 * Sayı + 1, Bit = 1
    
    Von_Neumann_Filtresi(Bit1, Bit2):
      Eğer 01 ise: Sonuç = 0
      Eğer 10 ise: Sonuç = 1
  Şifre = Metin_Bitleri XOR Sonuç_Bitleri
BİTİŞ
