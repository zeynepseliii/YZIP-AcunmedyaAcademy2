# kullanıcıdan alınan sayının asal olup olmadığının çıktısını veren program

sayi=int(input("Lutfen bir Sayı girin : "))
if sayi > 1:
   
   for i in range(2,sayi):
       if (sayi % i) == 0:
           print(sayi," Asal Sayı Değildir.")
           break
   else:
       print(sayi," Asal Sayıdır.")

# 2. Basit Hesap Makinesi
# Kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın.
# ✅ Kurallar:
# Kullanıcı +, -, *, / işlemlerinden birini seçmelidir.
# Bölme işleminde, ikinci sayı 0 olursa "Bölme işlemi için ikinci sayı 0 olamaz!" şeklinde uyarı verin.
# Kullanıcı geçersiz bir işlem girerse, "Geçersiz işlem türü!" mesajı gösterin.
# 🎯 Örnek Kullanım:
# hesap_makinesi(5, 3, '+')   # Çıktı: 5 + 3 = 8
# hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
# hesap_makinesi(4, 0, '/')   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
# hesap_makinesi(6, 2, '%')   # Çıktı: Geçersiz işlem türü!


def Topla(x, y):
   return x + y
 

def Cikar(x, y):
   return x - y
 

def Carp(x, y):
   return x * y
 

def Bol(x, y):
   if y == 0:
      return "Bölme işlemi için ikinci sayı 0 olamaz!"
   return x / y
 
print("Lutfen yapmak istediğiniz işlemi seçiniz.")
print("***********************")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
 
secim = input("Seçiminiz (1/2/3/4):")
 
sayi1 = int(input("lutfen 1. sayiyi giriniz: "))
sayi2 = int(input("lutfen 2. sayiyi giriniz: "))
 
if secim == '1':
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
elif secim == '2':
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
elif secim == '3':
   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
elif secim == '4':
   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
else:
   print("Geçersiz işlem türü!")











