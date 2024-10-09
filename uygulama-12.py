# 50 den 80e kadar sayıların toplamını bulup ekrana yazan program (25p)
# Format: 50 den 80 e kadar olan sayıların toplamı = 323723
toplam=0
for sayi in range(50,81):
  toplam = toplam + sayi
  print(f"{sayi }   { toplam}")

print(f"50 den 80 e kadar olan sayıların toplamı = {toplam}")

