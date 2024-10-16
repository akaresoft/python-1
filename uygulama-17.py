# meyveler tuple oluştur. sırayla elemanları ekrana yaz (for in ile)
meyveler = ("apple", "banana", "cherry")
for x in meyveler:
  print(x)
  
print()
print()

# 0-5 arası sayıları ekrana yaz
for i in range(5):
  print(i)

print()
print()


#  sırayla meyveler tuple ının elemanlarını sıra numarasıyla ekrana yaz (for in range ile)
for i in range(len(meyveler)):
  print(i+1,meyveler[i])


