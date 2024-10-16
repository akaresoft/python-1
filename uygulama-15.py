# oğrencinin 6 notunu diziye aktar
# 50 60 40 90 45 85
# dizideki notların toplamını bul ve ekrana yaz (döngüyle)

notlar = [50, 60, 40, 90, 45, 85]
toplam=0
for nt in notlar:
  toplam+=nt
print(f"6 notun toplamı ={toplam}")

# dizideki notların ortalamasını bul ve ekrana yaz

ortalama = toplam /6
print(f"6 notun ortalaması ={ortalama}")

# 3. notu 100 olarak değiştir # 50 60 100 90 45 85
notlar[2] = 100

# 5. notu sil # 50 60 100 90 85
notlar.pop(4)

# dizinin sonuna 90 notunu ekle # 50 60 100 90 85 90
notlar.append(90)

# dizinin 4 elamanına 20 notunu ekle # 50 60 100 20 90 85 90
notlar.insert(3, 20)

# dizinin ilk elamanını sil  # 60 100 20 90 85 90
notlar.pop(0)

# ortalamayı tekrar hesapla (sum ve count komutuyla)
ortalama = sum(notlar) / len(notlar)
print(f" Notların ortalaması ={ortalama}")
