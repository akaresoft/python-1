# verilen 4 basamaklı sayının basamaklarındaki rakamları bulan kodu yazınız

# a=5879  
# a4 = int (a /1000)) binler basamağını verir
# a3 =                yüzler basamağını verir
# a2 =                onlar basamağını verir
# a3 =                birler basamağını verir

# 1
# 4
# 5
# 8
x = 1453
a = int(x / 1000)
b = int(x / 100 - a * 10)
c = int(x / 10 - a * 100 - b * 10)
d = int(x / 1 - a * 1000 - b * 100 - c * 10)
print(a)
print(b)
print(c)
print(d)
