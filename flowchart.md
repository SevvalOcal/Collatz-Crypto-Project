# 📊 Algoritma Akış Şeması

Bu şema, Collatz Sanısı tabanlı şifreleme sistemimizin adım adım nasıl çalıştığını göstermektedir.

```mermaid
graph TD
    A[Başla: Seed Sayısı ve Metin Girişi] --> B[Metni Bit Dizisine Çevir]
    B --> C{Bit Uzunluğu Tamam mı?}
    C -- Hayır --> D[Collatz İşlemi: n/2 veya 3n+1]
    D --> E[Ham Bit Oluştur: 0 veya 1]
    E --> F{Von Neumann Filtresi}
    F -- "01 ise" --> G[Çıktı: 0]
    F -- "10 ise" --> H[Çıktı: 1]
    F -- "00 veya 11" --> D
    G --> I[Anahtar Dizisine Ekle]
    H --> I
    I --> C
    C -- Evet --> J[Metin Bitleri XOR Anahtar Bitleri]
    J --> K[Şifreli 0-1 Dizisini Yazdır]
    K --> L[Bitiş]
