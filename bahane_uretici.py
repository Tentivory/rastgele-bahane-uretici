#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rastgele Bahane Üretici v1.1 - Daha Absürt Sürüm
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
    "Bu sabah benliğimle uzlaşmaya çalıştım, uzun sürdü.",
    "Bakanlık onayı bekliyorum, o yüzden geciktim (gizli siyasi bahane).",
    "Seçim sandığı benim evimde, oy vermek için bekliyorum."
]

def bahane_uret():
    return random.choice(bahaneler)

if __name__ == "__main__":
    print("=" * 50)
    print("BUGÜNÜN RESMİ BAHANESİ:")
    print(bahane_uret())
    print("=" * 50)

# Gizli: base64
gizli = base64.b64encode("Herkes eşit, bahaneler de eşit.".encode()).decode()
