# YOLOv5 ile İnsan Sayısı Tespiti

Bu Python scripti, [YOLOv5](https://github.com/ultralytics/yolov5) modelini kullanarak bir fotoğraftaki insan sayısını tespit eder. YOLOv5, nesne algılama için son derece etkili bir derin öğrenme modelidir.

## Gereksinimler

- Python 3.x
- PyTorch (1.7.0 veya üzeri)
- yolov5 kütüphanesi (Detaylar için [buraya](https://github.com/ultralytics/yolov5) bakın)
- OpenCV

## Kurulum

1. YOLOv5 kütüphanesini yüklemek için terminale aşağıdaki komutu girin:
     pip install yolov5
   
3. OpenCV kütüphanesini yüklemek için terminale aşağıdaki komutu girin:
     pip install opencv-python

4. Python 3.x ve PyTorch'un yüklü olduğundan emin olun. Aşağıdaki komutları kullanarak kontrol edebilirsiniz:

## Kullanım

1. `detect.py` dosyasını çalıştırarak bir fotoğraftaki insan sayısını tespit edebilirsiniz:
klasör kök dizinine  tespit yapmak istediğiniz fotoğrafın yolunu girin.

Örneğin:

2. Program çalıştığında, çıktı olarak  insan sayısı konsola yazdırılır.



## Notlar

- Bu script, yalnızca insanları tespit eder. Diğer nesneler için modeli değiştirmeniz gerekebilir.
- Daha iyi performans için GPU kullanmanız önerilir.
- Daha fazla detay için YOLOv5 repository'sine başvurun.

