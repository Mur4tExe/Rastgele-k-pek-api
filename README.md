# 🐾 Rastgele Köpek API

[span_0](start_span)Bu proje, **FastAPI** kullanılarak geliştirilmiş, popüler köpek görselleri servisinden veri çekerek rastgele köpek fotoğrafları sunan basit ve hızlı bir API uygulamasıdır.[span_0](end_span)

## 🚀 Özellikler

* **[span_1](start_span)Hızlı ve Hafif:** FastAPI tabanlı yüksek performans.[span_1](end_span)
* **[span_2](start_span)Kolay Entegrasyon:** JSON formatında veri dönüşü.[span_2](end_span)
* **[span_3](start_span)Hata Yönetimi:** İstek sırasında oluşabilecek hatalar için kontrol mekanizması (try-except yapısı).[span_3](end_span)

## 🛠 Kullanılan Teknolojiler

* **[span_4](start_span)Python 3.x**[span_4](end_span)
* **[span_5](start_span)FastAPI:** Modern ve hızlı web framework.[span_5](end_span)
* **[span_6](start_span)Uvicorn:** ASGI sunucusu.[span_6](end_span)
* **[span_7](start_span)Requests:** HTTP istekleri için.[span_7](end_span)

## 📥 Kurulum

Projeyi yerel makinenizde çalıştırmak için şu adımları izleyin:

1.  **Depoyu klonlayın:**
    ```bash
    git clone [https://github.com/kullaniciadi/Rastgele-k-pek-api.git](https://github.com/kullaniciadi/Rastgele-k-pek-api.git)
    cd Rastgele-k-pek-api
    ```

2.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install fastapi uvicorn requests
    ```

3.  **Uygulamayı başlatın:**
    ```bash
    uvicorn main:app --reload
    ```

## 📋 Kullanım

API çalıştıktan sonra tarayıcınızdan veya bir API istemcisinden şu uç noktalara erişebilirsiniz:

* **[span_8](start_span)Ana Sayfa:** `http://127.0.0.1:8000/`[span_8](end_span)
* **[span_9](start_span)Rastgele Köpek:** `http://127.0.0.1:8000/randomdog`[span_9](end_span)

### Örnek Yanıt (JSON)

```json
{
  "success": true,
  "image": "[https://images.dog.ceo/breeds/beagle/n02088364_1111.jpg](https://images.dog.ceo/breeds/beagle/n02088364_1111.jpg)",
  "note": "Telegram: @ZaherOrj @QueryBots"
}
