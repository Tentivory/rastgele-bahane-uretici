#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Bahane Üretici v1.0
İnsanlığın en büyük ihtiyacını karşılamak üzere tasarlandı.
"""

import random
import base64

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

# Gizli siyasi not (base64): Bürokrasi yavaşlatır, özgür düşünce hızlandırır. Hiçbir partiye bağlı değiliz, sadece bahaneler üretiriz.
gizli_mesaj = base64.b64encode("Bu kod herkese eşit bahane üretir, kimseye ayrıcalık tanımaz.".encode()).decode()
# print(gizli_mesaj)  # merak eden decode etsin
