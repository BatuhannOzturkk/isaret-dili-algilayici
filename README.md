
# ✋ İşaret Dili Algılayıcı / Sign Language Recognizer

Bu proje, tek el hareketlerini kamerayla algılayarak jestin ismini ekranda gösteren ve sesli olarak okuyan bir **işaret dili tanıma** uygulamasıdır.

This project is a **sign language recognition** app that detects single-hand gestures using a webcam and reads the gesture out loud while displaying it on the screen.

---

## 📌 Genel Bilgiler / General Information

- 🖥️ Geliştirici / Developer: Batuhan Öztürk  
- 🐍 Python Sürümü / Version: **Python 3.11**
- 💻 Platform: **Yalnızca Windows** / **Windows only**
- 🎤 Sesli Geri Bildirim / Voice Feedback: `pyttsx3` kullanır (SAPI5 - Windows TTS)
- 🖼️ Arayüz: Tkinter GUI
- 📹 Kamera: OpenCV + Mediapipe ile canlı el hareketi algılama

> ⚠️ Bu uygulama **yalnızca Windows işletim sisteminde** çalışır. MacOS ve Linux’ta sesli okuma çalışmayacaktır.

---

## ✋ Desteklenen Jestler / Supported Gestures

| Emoji | Türkçe Jest Adı     | English Gesture Name |
|-------|----------------------|-----------------------|
| 👍     | Beğendim             | Like                  |
| 👎     | Beğenmedim           | Dislike               |
| ✌️     | Zafer                | Victory               |
| 👌     | Tamam                | OK                    |
| ✋     | Dur                  | Stop                  |
| 🐺     | Bozkurt              | Wolf Symbol           |
| ✊     | Yumruk               | Fist                  |

Her jest için el pozisyonu koordinatlara göre tanımlanmıştır. Tanınan jest, ekranda görüntülenir ve sesli olarak okunur.

Each gesture is defined based on finger tip coordinates. When recognized, the gesture is printed on the screen and spoken aloud.

---

## 🧠 Kullanılan Kütüphaneler / Used Libraries

- `mediapipe`
- `opencv-python`
- `pyttsx3`
- `Pillow`
- `tkinter` (Python ile birlikte gelir)

---

## ⚙️ Kurulum / Installation

Aşağıdaki komutla gerekli tüm kütüphaneleri yükleyebilirsiniz:

```bash
pip install mediapipe opencv-python pyttsx3 Pillow
```

> 🔍 Eğer `ModuleNotFoundError` alırsanız, yukarıdaki komut eksik kütüphaneleri yükleyecektir.

Alternatif olarak aşağıdaki komutla tüm kütüphaneleri `requirements.txt` dosyasından otomatik yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```

---

## ▶️ Çalıştırma / Run

```bash
python "İşaret Dili Algılayıcı.py"
```

Kodu çalıştırdıktan sonra:

- Kamera açılır
- Tanınan jest ekranda görünür
- İsterseniz **"SES"** butonuna tıklayarak jestin adını bilgisayarınıza sesli okutabilirsiniz

---

## 📝 Notlar / Notes

- Program **Python 3.11** ile geliştirilmiştir. Bu sürümde sorunsuz çalışır.
- Kamera erişimine izin vermeniz gerekir.
- Eğer performans düşerse, el hareketlerini daha belirgin yapmayı deneyin.

---

## 🙏 Teşekkürler / Thanks

Bu uygulama, el hareketleriyle iletişimi kolaylaştırmak amacıyla geliştirilmiştir. Her türlü katkı ve öneriye açıktır.

This application was developed to support communication via hand gestures. Contributions and feedback are welcome!
