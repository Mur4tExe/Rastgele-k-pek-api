# 🐾 Rastgele Köpek API

Bu proje, FastAPI kullanılarak geliştirilmiş, popüler köpek görselleri servisinden veri çekerek rastgele köpek fotoğrafları sunan hızlı bir API uygulamasıdır.

## 🚀 Özellikler

* **FastAPI Altyapısı:** Modern ve yüksek performanslı bir yapı.
* **Anlık Veri:** Dog CEO API üzerinden güncel köpek fotoğrafları çeker.
* **Kolay Kullanım:** Sade JSON çıktıları.

## 🛠 Kullanılan Teknolojiler

* **Python 3.x**
* **FastAPI**
* **Uvicorn**
* **Requests**

## 📥 Kurulum ve Çalıştırma

1. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt

 * Uygulamayı başlatın:
   uvicorn main:app --reload

📋 API Kullanımı
API çalıştıktan sonra aşağıdaki uç noktalara (endpoints) istek atabilirsiniz:
 * Ana Sayfa: GET / - Hoş geldin mesajı ve kullanım bilgisi döner.
 * Rastgele Köpek: GET /randomdog - Yeni bir köpek fotoğrafı linki döner.
Örnek Yanıt (JSON)
{
    "success": true,
    "image": "[https://images.dog.ceo/breeds/terrier-border/n02093754_3650.jpg](https://images.dog.ceo/breeds/terrier-border/n02093754_3650.jpg)",
    "note": "Telegram: @ZaherOrj @QueryBots"
}

👨‍💻 İletişim
Geliştirici ve destek kanalları:
 * Telegram: @ZaherOrj
 * Telegram: @QueryBots
