
# Sayı Eşleştirme Oyunu


Bu, Python'da basit bir sayı eşleştirme oyunudur. Oyunun amacı, oyun tahtasındaki bitişik sayıları bulmak ve eşleştirmektir. Eşleştirilen sayıların değeri ne kadar yüksekse, oyuncu o kadar fazla puan kazanır.

## Başlarken
Oyunu çalıştırmak için aşağıdaki adımları izleyin:

   1. Sisteminizde Python'un yüklü olduğundan emin olun.
   2. Proje dosyalarını indirin ve proje dizinine gidin.
   3. Proje dizininde bir komut istemi veya terminal açın.


## Önkoşullar
    
    * Python 3.x



## Ekran Görüntüleri
![1](https://github.com/kagantemizkan/python-number-matching/assets/46727689/59d6e8b2-288e-4bf7-944c-768af3f16094)

![2](https://github.com/kagantemizkan/python-number-matching/assets/46727689/99b298c0-f60a-4a91-9fb9-53910a315615)
##
![3](https://github.com/kagantemizkan/python-number-matching/assets/46727689/fe724e82-313b-4fbc-a356-cf53715b7e04)
##
![4](https://github.com/kagantemizkan/python-number-matching/assets/46727689/b05b74f2-76d5-403d-a330-39c8fa281b81)
##
![5](https://github.com/kagantemizkan/python-number-matching/assets/46727689/e34738d7-3300-42d4-a1d1-9e8030418e8f)
## 


## Oyunu Çalıştırma
 
Oyunu çalıştırmak için aşağıdaki komutu kullanın:

```bash 
python game.py <board_dosyası> <output_dosyası>
```

<board_dosyası>: Oyun tahtasını saklamak için dosya yoludur.

<output_dosyası>: Oyun istatistiklerini ve son oyun tahtasını saklamak için dosya yoludur.
    
## Oyun Talimatları

 1. Oyun tahtasının istediğiniz boyutlarını (satır ve sütun sayısı) girin.
 2. Oynamak istediğiniz tur sayısını girin.
 3. Oyun tahtası, her hücredeki sayıları göstererek görüntülenecektir.
 4. Bir hücre seçmek için satır ve sütun dizinlerini girin.
 5. Seçilen sayı kaldırılacak ve aynı değere sahip bitişik sayılar da kaldırılacaktır.
 6. Oyun tahtası güncellenecek ve kaldırılan sayılara dayanarak puanlar verilecektir.
 7. Belirtilen tur sayısı için 4-6 adımlarını tekrarlayın.
 8. Belirtilen tur sayısı sona erdikten sonra, nihai oyun tahtası ve oyun istatistikleri   görüntülenecektir.

 ## Oyun Özellikleri
+ Oyun tahtası, 1 ila 9 arasındaki sayılarla rastgele oluşturulur. Sayının değeri ne kadar yüksekse, oluşma olasılığı o kadar düşüktür.
+ Aynı değere sahip bitişik sayıları eşleştirmek, sayının değeri ve Fibonacci dizisine dayanarak puan kazandırır.
+ Oyun tahtasından kaldırılan sayılar, üstlerindeki hücreleri aşağıya doğru düşürerek boşlukları doldurur.
+ Bir sütun tamamen boş hale geldiğinde, o sütundan sağdaki hücreler boşluğu doldurmak için sola kayar.
+ Oyun, belirtilen tur sayısı sonunda biter ve nihai oyun tahtası ile oyun istatistikleri çıktı dosyasına kaydedilir.
## 

Sayı Eşleştirme Oyunu'nu oynarken iyi eğlenceler!
