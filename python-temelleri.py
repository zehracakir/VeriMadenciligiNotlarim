# ''' print fonku '''
# # ekrana bastırma
print("hello world")
print("aaaa")

# # tek satır açıklama satırı
# ''' yorum satırı çok satır için  '''

# ''' 
# veri tipleri 
# int veri tipi : tam sayılar için
# float veri tipi : virgüllü sayılar
# str veri tipi : string veriler tek veya çift tırnak içerisinde gösterilirler.Char veri tipi yok python da
# bool veri tipi : True veya False
# complex veri tipi : Karmaşık sayı veri tipi.3+5i
# '''

# # veri tipini verir
tamSayi = 5
print(type(tamSayi))

reelSAyi = 3.14
print(type(reelSAyi))

strVeri = "merhaba"
print(type(strVeri))

boolVeri = True
print(type(boolVeri))

complexVeri = 3+5j
print(type(complexVeri))

# yeni satıra geçmez merhaba ve dünya arasına bir boşluk bırakır, farklı bir şeyde koyabilir. Örneğin $ & vs.
print("merhaba",end=" ")
print("dünya")

#default hali bir boşluk biz bunu değiştirebiliriz
print("merhaba","dünya",sep=',')

# ''' klavyeden değer almak için input fonku kullanılır '''
# input string döndürür 
sayi1 = input("birinci sayı")
sayi2 = input("ikinci sayı")
print(sayi1+sayi2)#birincisayi+ikincisayi

#int olarak toplar
sayi1 = int(input("birinci sayı"))
sayi2 = int(input("ikinci sayı"))
print(sayi1+sayi2)

# ''' koşullu ifadeler
# if şart veya şartlar:
#     doğruysa yapılacaklar
# else:
#     yanlışsa yapılacaklar
    
    
# if şart1:
#     şart doğruysa yapılacaklar
# elif şart2:
#     şart2 doğruysa yapılacaklar
# elif şart3:
#      şart3 doğruysa yapılacaklar 
# else:
#     hiçbir şart sağlanmıyorsa yapılacaklar'''

if 5> 3:
    print("5 büyük")
elif 5 < 3:
    print("3 büyük")
else:
    print("eşittir")

# ''' for donduDegiskeni in range(start,stop,increment veya decrement):
#     yapılacaklar
    
# '''

for i in range(5): # 0 dan 5 e kadar 5 dahil değil
    print(i)

for i in range(1,5): # 1 den 5 e kadar 5 dahil, default olarak 1 er 1 er artar
        print(i)

for i in range(1,10,2):# 1 den 10 a kadar 2şer 2şer artırarak yazar 10 dahil değil
    print(i)

# #kelimenin harflerini alt alta bastırır
kelime = "merhaba"
for i in kelime:
    print(i)

# #f string -> kelimenin kaçıncı harfinin ne olduğunu bastırır
kelime = "merhaba"
sira = 1
for chr in kelime:
    print(f"kelimenin {sira}. harfi {chr}")
    sira += 1

# ''' 
# while şart veya şartlar
#     yapılacak
# '''
i = 0
while i < 10:
    print(i)
    i += 1 # i++ olmaz pythonda yok

while True:
   sayi = int(input("Sayı: "))
   if sayi % 2 == 0:
        break 

# ''' 
# fonksiyonlar
# def funcName(parametreler):
#     yapılacaklar
#     eğer geri değer döndürecekse
#     return geri döndüreceği değer
# '''

def ekranaYaz():
    print("merhaba")
ekranaYaz()

def ekranaYaz (kelime,tekrar=1):
    for i in range():
        print(kelime)
ekranaYaz("güle güle")

def ekranaYaz(kelime = "gelmedi",tekrar = 1): # default olarak değer atayabiliriz -> tekrar = 1 ya da kelime = "gelmedi"
    for i in range(tekrar):
        print(kelime)
ekranaYaz()


def ekranaYaz (kelime,tekrar):
    for i in range(tekrar):
        print(kelime)
ekranaYaz(tekrar=5,kelime="ali") # Default olarak ilk verileni ilk parametreye atar.Fakat belirtirsek sorun olmaz


def topla(sayi1,sayi2)->int: #Bu fonk çalışacak ve geriye int değer döndürecek demek "->int"
    return sayi1 + sayi2
print(topla(3,5))


def topla(sayi1:int,sayi2:int)->int: #Bu fonk çalışacak ve geriye int değer döndürecek demek "->int"
    return sayi1 + sayi2
print(topla(3,5))

# '''operatörler'''
print(5 // 2) # bölümü verir

print(5 ** 2) # sayının üssünü alır

import math  #python da projemize kütüphane eklemek için -> math ile mateamtiksel fonklara ulaşabiliriz
print(math.factorial(5))

# '''listeler'''
liste = [] # boş liste
liste1 = list() # boş liste
print(type(liste)) # liste tipinde 
print(type(liste1)) # liste tipinde

liste2 = []
for i in range(5):
    liste2.append(1 ** 2) # eleman ekleme
print(liste2)

for elm in liste2:
    print(elm)

for index in range(len(liste2)):
    print(liste2[index])

liste = []
for i in range(5):
    liste.append(i ** 2)
print(liste)
liste2 = liste.copy() #shallow copy
print(liste2)

print(liste.index(9)) # bir sayının listede kaçıncı indexte olduğunu öğrenmemizi sağlar

liste.insert(1,8) # istediğimiz aralığa istediğimiz değeri eklememizi sağlar
print(liste)

liste.extend([1,2,3]) # extend ile bir başka listeyi listemizin sonuna ekleyebiliriz
print(liste)

print(liste.pop()) # default olarak en sondaki elemanı siler
print(liste)

#dictionary: verileri key value biçminde saklayan bir veri yapısıdır
sozluk = {}
sozluk1 = dict()
sozluk = {"kalem":3,"silgi":5,"defter":4}
print(sozluk)

for key in sozluk.keys():
    print(f'sozluk[{key}]={sozluk[key]}')

print("kalem" in sozluk)
sozluk = {"kalem":3,"silgi":4,"defter":5};
new_dict = dict.fromkeys(["kalem","defter"],3)
print(new_dict)
liste=[1,2,23,3,2,2,1,1,4,5,4,2]
tekrar={}

for key in liste:
    if(key not in tekrar):
        tekrar[key] = 1
    else:
        tekrar[key] += 1
print(tekrar)

sozluk = {"kalem":3,"silgi":4,"defter":5}
print(sozluk.pop("kalem"))
print(sozluk)
print(sozluk.pop("kagit",-1))
#Eğer sozlukte aaaa yoksa -1 döner varsa keyini döner
print(sozluk.setdefault("aaaa",-1))
# Tuplelar
list = ()
list1 = tuple()
