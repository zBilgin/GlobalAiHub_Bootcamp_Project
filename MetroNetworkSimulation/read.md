# Global AI Hub 
# Akbank Python ile Yapay Zekaya Giriş Bootcamp 
# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu) 

## 📌 Açıklama
Bu proje, BFS (Breadth-First Search) ve A* (A-Star) algoritmalarını kullanarak bir metro ağında en kısa ve en hızlı rotayı bulan bir simülasyon uygulamasıdır. 

🔹 Kullanıcılar, başlangıç ve hedef istasyonlarını belirterek en verimli güzergahı hesaplayabilirler.

## 🚀 Kullanılan Teknolojiler ve Kütüphaneler
Bu projede **Python** dili ve aşağıdaki kütüphaneler kullanılmıştır:

- heapq → A* algoritması için öncelikli kuyruk yapısını sağlar.
- collections.deque → BFS algoritması için hızlı kuyruk işlemleri sağlar.
- defaultdict → Metro ağını daha düzenli tutmak için kullanılır.
- typing → {Dict, List, Set, Tuple, Optional} türleri için ipuçları sağlayarak kodun okunabilirliğini artırır.

## 🔍 Algoritmaların Çalışma Mantığı

### 🟢 BFS (Breadth-First Search) Algoritması
BFS, **en az aktarma yapılan güzergahı** bulmak için kullanılır. **FIFO (First In, First Out)** prensibiyle çalışır ve seviyeli bir şekilde tüm istasyonları tarar.

**Adımlar:**
1. Başlangıç istasyonu kuyruğa (queue) eklenir.
2. Kuyruğun başındaki istasyon çıkarılır ve komşu istasyonlar kuyruğa eklenir.
3. Eğer hedef istasyona ulaşılmışsa, rota döndürülür.
4. Kuyruk boşalana kadar bu işlem devam eder.

**✔️ Neden BFS?** En kısa adım sırasıyla hedefe ulaşmayı garanti eder.

---

### 🟢 A* (A-Star) Algoritması
A* algoritması, **en hızlı rotayı** bulmak için kullanılır. BFS'den farklı olarak, her istasyonun tahmini bir maliyetini (**heuristic**) hesaplar ve düşük maliyetli rotayı seçer.

**Adımlar:**
1. Başlangıç düğümü **open list** adlı öncelikli kuyruğa eklenir.
2. En düşük **f(n) = g(n) + h(n)** değerine sahip düğüm seçilir.
3. Eğer hedef istasyona ulaşıldıysa, rota döndürülür.
4. Komşular keşfedilir ve **heuristic (h(n))** değeri ile maliyet güncellenerek **open list**'e eklenir.
5. Tüm düğümler işlenene kadar devam eder.

**✔️ Neden A*?** BFS’den daha hızlı çalışabilir çünkü hedefe yakın olan yolları önceliklendirir. Daha az gereksiz düğüm ziyaret ederek verimli bir hesaplama yapar.

## 📌 Örnek Kullanım ve Çıktılar

---

![Metro Görseli](MetroNetworkSimulation/MetroAg.png)

---


### 🎯 **Senaryo 3: OSTİM'den Kızılay'a**
```python
print("\nOSTİM'den Kızılay'a")
rota = metro.en_az_aktarma_bul("O1", "K1")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("O1", "K1")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
```

**Çıktı:**
```
OSTİM'den Kızılay'a
En az aktarmalı rota: OSTİM -> Gar -> Sıhhiye -> Kızılay
En hızlı rota (14 dakika): OSTİM -> Gar -> Kızılay
```

### 🎯 **Senaryo 4: Batıkent'ten Mamak'a**
```python
print("\nBatıkent'ten Mamak'a")
rota = metro.en_az_aktarma_bul("B1", "M2")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("B1", "M2")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
```

**Çıktı:**
```
Batıkent'ten Mamak'a
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Kızılay -> Mamak
En hızlı rota (25 dakika): Batıkent -> Ulus -> Kızılay -> Mamak
```

### 🎯 **Senaryo 5: Kızılay'dan Keçiören'e**

```python
print("\n5. Kızılay'dan Keçiören'e")
rota = metro.en_az_aktarma_bul("K1", "T4")
if rota:
    print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

sonuc = metro.en_hizli_rota_bul("K1", "T4")
if sonuc:
    rota, sure = sonuc
    print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
```

**Çıktı:**
```
Kızılay'dan Keçiören'e
En az aktarmalı rota: Kızılay -> Ulus -> Demetevler -> Gar -> Keçiören
En hızlı rota (16 dakika): Kızılay -> Sıhhiye -> Gar -> Keçiören

```

## 📌 Projeyi Geliştirme Fikirleri
✅ Daha büyük ve detaylı bir metro haritası entegre edilebilir.  
✅ Kullanıcıdan başlangıç noktası ve hedef seçimi alınarak **görsel bir arayüz** ile desteklenebilir.  
✅ Metroya ek olarak, trafik yoğunluğu ve otobüs aktarmaları içeren **dinamik bir ulaşım ağı** geliştirilebilir.  

