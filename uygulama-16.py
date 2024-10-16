# kullanıcıdan alınan değeri tıpple da arayıp sonucunu ekrana yazan program
thistuple = ("apple", "banana", "cherry")
aranan = input("lütfen aranan elemanı gir: ")
if  aranan in thistuple:
  print(f"Evet, {aranan} listemizde bulunmaktadır")
else:
  print(f"Hayır, {aranan} listemizde bulunmamaktadır")
