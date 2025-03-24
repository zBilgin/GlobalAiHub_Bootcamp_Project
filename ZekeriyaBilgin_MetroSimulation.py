from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if idx not in self.istasyonlar:  
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur"""
        
        # Başlangıç ve hedef istasyonların varlığını kontrol et
        if baslangic_id not in self.istasyonlar:
            print(f"Hata: '{baslangic_id}' istasyonu bulunamadı! Lütfen geçerli bir başlangıç istasyonu girin.")
            return None

        if hedef_id not in self.istasyonlar:
            print(f"Hata: '{hedef_id}' istasyonu bulunamadı! Lütfen geçerli bir hedef istasyonu girin.")
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic.ad])])  # (istasyon, yol listesi)
        ziyaret_edildi = set()  # Ziyaret edilen istasyonları tutar

        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()  # FIFO prensibiyle istasyonu al

            if mevcut_istasyon == hedef:
                return yol  # Hedefe ulaşıldıysa yolu döndür

            ziyaret_edildi.add(mevcut_istasyon)

            for komsu, _ in mevcut_istasyon.komsular:  # Komşu istasyonları kontrol et
                if komsu not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu.ad]))  # Yeni yolu ekleyerek kuyruğa al

        print(f"Hata: '{baslangic_id}' ile '{hedef_id}' arasında geçerli bir rota bulunamadı!")
        return None  # Hedefe ulaşılamazsa

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[str], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur"""
        
        # Geçersiz istasyon girişlerini kontrol et
        if baslangic_id not in self.istasyonlar:
            print(f"Hata: '{baslangic_id}' istasyonu bulunamadı! Lütfen geçerli bir başlangıç istasyonu girin.")
            return None

        if hedef_id not in self.istasyonlar:
            print(f"Hata: '{hedef_id}' istasyonu bulunamadı! Lütfen geçerli bir hedef istasyonu girin.")
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        # Öncelik kuyruğu (heap) başlat
        pq = [(0, id(baslangic), baslangic, [baslangic.ad])]  # (Toplam süre, id, mevcut istasyon, rota)
        ziyaret_edildi = {}

        while pq:
            toplam_sure, _, mevcut_istasyon, yol = heapq.heappop(pq)  # En düşük süreli rotayı al

            # Eğer hedefe ulaştıysak, rotayı döndür
            if mevcut_istasyon == hedef:
                return yol, toplam_sure

            if mevcut_istasyon in ziyaret_edildi and ziyaret_edildi[mevcut_istasyon] <= toplam_sure:
                continue  # Daha kısa bir yol varsa eski kaydı kullan

            ziyaret_edildi[mevcut_istasyon] = toplam_sure

            # Komşu istasyonları keşfet
            for komsu, sure in mevcut_istasyon.komsular:
                yeni_sure = toplam_sure + sure
                heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yol + [komsu.ad]))

        print(f"Hata: '{baslangic_id}' ile '{hedef_id}' arasında geçerli bir rota bulunamadı!")
        return None  # Hedefe ulaşılamazsa

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i for i in rota))

    # Senaryo 3: Demetevler'den Aşti'ye
    print("\n3. Demetevler'den Aşti'ye:")
    rota = metro.en_az_aktarma_bul("T2", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i for i in rota))

    sonuc = metro.en_hizli_rota_bul("T2", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i for i in rota))

    # Senaryo 4: Batıkent'den Aşti'ye
    print("\n4. Batıkent'den Aşti'ye:")
    rota = metro.en_az_aktarma_bul("T1", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i for i in rota))

    # Senaryo 5: Kızılay'dan Keçiören'e
    print("\n5. Kızılay'dan Keçiören'e")
    rota = metro.en_az_aktarma_bul("K1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("K1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))