# 18. uygulamayı faturaya dönüştür.
fatura = [
            {"urunadi":"MERMER", "bfiyat":0,"miktar":0},
            {"urunadi":"GRANİT", "bfiyat":0,"miktar":0},
            {"urunadi":"FAYANS", "bfiyat":0,"miktar":0},
            {"urunadi":"SERAMİK", "bfiyat":0,"miktar":0},
            {"urunadi":"EPOKSİ", "bfiyat":0,"miktar":0},
          ]

for i in range(len(fatura)):
  fatura[i]["bfiyat"] = input(fatura[i]["urunadi"] + "  birim fiyatını gir:")
  fatura[i]["miktar"] = input(fatura[i]["urunadi"] + " miktarını gir:")
   
print()
print("ÜRÜNADI       Miktar  Birim Fiyat  TOPLAM")
print("--------       --- --- --- --- ---")

gtoplam=0
for urun in fatura:
  toplam = int(urun["bfiyat"]) * int(urun["miktar"])
  gtoplam += toplam
  print(urun["urunadi"], urun["miktar"], urun["bfiyat"], toplam)
 
print("Genel Toplam = ", gtoplam)
