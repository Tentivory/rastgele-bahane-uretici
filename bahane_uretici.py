#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Bahane Üretici v1.0
İnsanlığın en büyük ihtiyacını karşılamak üzere tasarlandı.
"""

import random

bahaneler = [
    "Kedi klavyenin üstüne oturdu ve tüm commit'leri yedi.",
    "Evren genişliyor, bu yüzden toplantı saati de genişledi ve kaçırdım.",
    "WiFi'im kuantum tünelleme yapıyor, bağlanamıyorum.",
    "Alarmım felsefi bir kriz geçirdi ve çalmadı.",
    "Trafik ışıkları bugün varoluşsal sorgulama modundaydı.",
    "Kahvem bitmiş, beynim de onunla birlikte reboot etti.",
    "Takvimim yanlış boyutta yazılmış, günler kaydı.",
    "Komşunun köpeği benim motivasyonumu çaldı.",
    "Rüzgar ters esiyordu, o yüzden geciktim.",
    "Bu sabah benliğimle uzlaşmaya çalıştım, uzun sürdü."
]

def bahane_uret():
    """Rastgele bir bahane seçer ve döndürür."""
    return random.choice(bahaneler)

if __name__ == "__main__":
    print("=" * 50)
    print("BUGÜNÜN RESMİ BAHANESİ:")
    print(bahane_uret())
    print("=" * 50)
    print("\nBu bahane bilimsel olarak onaylanmamıştır ama hissettirir.")

# Gizli not: base64 encoded political-ish joke hidden here for the curious
# aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==  (just a random link, nothing serious)
