# Veri Madenciliği

- Bu repository’i Süleyman Demirel Üniversitesi bilgisayar mühendisliği bölümünde anlatılan Veri Madenciliği dersinde aldığım notlarım ve kendi çalışmalarımla oluşturdum.
- Kodlarda anlatılan konularla ilgili gerekli açıklamalar yorum satırı olarak bulunmaktadır.
- İlk 3 hafta python temelleri, 4.hafta-10.hafta pandas kütüphanesinin detaylı anlatımından oluşmaktadır.
- 11.hafta : Lineer Regresyon yöntemi
- 12.hafta : Sınıflandırma yöntemi
- 13.hafta : Kümeleme yöntemi üzerinde çalışmalardan oluşmaktadır.
- Kendi çalışmalarım kısmında ise derste öğrendiğim bilgiler ve yöntemler üzerine; internetten indirmiş olduğum veri setleri üzerinde yaptığım çalışmalar yer almaktadır.

### Veri Madenciliği Nedir ?

Veri madenciliği, büyük ölçekli veriler arasından faydalı bilgiye ulaşma, bilgiyi madenleme işidir.

### Veri Madenciliği Süreçleri Nelerdir?

1. İşi Anlama : Veri bilimci veya madencisi, proje hedeflerini ve kapsamını belirleyerek işe başlar.
- Ele alınması gereken sorunlar
- Proje kısıtlamaları veya sınırlamaları
- Potansiyel çözümlerin iş üzerindeki etkisi
1. Veriyi Anlama : Veri bilimciler, iş sorununu anladıktan sonra verilerin ön analizine başlarlar. Çeşitli kaynaklardan veri setleri toplar, erişim haklarını elde eder ve bir veri tanımlama raporu hazırlarlar. Raporda veri türleri, miktarı ve veri işleme için donanım ve yazılım gereksinimleri bulunur. İşletme planlarını onayladıktan sonra, verileri keşfetmeye ve doğrulamaya başlarlar. Temel istatistiksel teknikleri kullanarak verileri yönlendirir, veri kalitesini değerlendirir ve bir sonraki aşama için nihai bir veri seti seçerler.
2. Veriyi Hazırlama : Eksik olan verileri sayısalsa ortalama ya da medyanla; sözelse en çok tekrar eden veriyle doldurma aşamasıdır. Eğer verilerde bir tutarsızlık olursa verilerde silme işlemi de yapılabilir. Yani bu aşama verileri modellemeye hazırlık aşamasıdır.
3. Veriyi Modelleme : Hazırlanan veriler veri madenciliği yazılımına girer ve sonuçları incelenir. Bu işlem yapılırken birden fazla veri madenciliği modeli arasından seçim yapabiliriz.

## Modelleme Seçenekleri

- Lineer Regresyon Yöntemi :  İlgili ve bilinen başka bir veri değeri kullanark bilinmeyen verilerin değerini tahmin eden bir veri analizi tekniğidir. Bilinmeyen veya bağımlı değişkeni ve bilinen veya bağımsız değişkeni doğrusal bir denklem olarak matematiksel olarak modeller.
- Sınıflandırma Yöntemi : Bir veri veya veri grubunun mevcut sınıflardan hangisine ait olduğunun belirlenmesi olarak tanımlanmaktadır. Sınıflandırma çalışmalarında en önemli kriter yüksek başarımlı bir sınıflandırıcı model oluşturabilmektir.
- Kümeleme Yöntemi : Kümeleme analizi grupları kesin olarak bilinmeyen, birimleri, değişkenleri birbiriyle benzer alt kümelere (grup, sınıf) ayırmaya yardımcı olan çok değişkenli istatistiksel analiz yöntemlerinden biridir. Kümeleme analizinin temel amacı birimleri sahip oldukları karakteristik özellikleri temel alarak gruplandırmaktır.

Bu modelleme seçeneklerinde :

- Veriler train ve test olmak üzere iki gruba ayrılır.
- train eğittiğimiz veriler, test ise test yaptığımız veriler.
- test verileri 1 e ne kadar yakınsa o kadar gerçekçi bir sonuç alırız.
1.Random
2.Elle %80 Train,%20 Test
- cross validation-> bir başka doğrulama yöntemidir.veriler n kümeye böülünür.
örneğin ne=5 olsun
1 2 3 4 5
1.adımda 1.küme test [2,3,4,5] eğititm için kullanılır.Metrikler bulunur.
2.adımda 2.küme test [1,3,4,5] eğititm için kullanılır.Metrikler bulunur.
3.adımda 3.küme test [1,2,4,5] eğititm için kullanılır.Metrikler bulunur.
4.adımda 4.küme test [1,2,3,5] eğititm için kullanılır.Metrikler bulunur.
5.adımda 5.küme test [1,2,3,4] eğititm için kullanılır.Metrikler bulunur.
- Lineer Regresyon ve Kümeleme tekniklerinde giriş (X ile gösterilir) ve çıkıs (y ile gösterilir) değişkenlerimiz var. Fakat Kümeleme tekniğinde çıkış (y) değişkeni yoktur.

## Aşırı Öğrenme Nedir ?

- Algoritmanın eğitim verisi üzerinden en alt kırılıma kadar çalışıp, sonuçları ezberlemesi ve sadece o veriler üzerinde başarı elde edebilmesidir. Eğitim verisi ile kurduğunuz modeli, test verisi üzerinde çalıştırdığınızda muhtemelen sonuçlar eğitim verisine göre çok düşük çıkacaktır.