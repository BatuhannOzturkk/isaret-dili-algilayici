# Kütüphanelerin İçe Aktarılması
import mediapipe as mp
import cv2, math, datetime, pyttsx3
from tkinter import*
from PIL import Image, ImageTk

# TKinter Arayüzünün Başlatılması 
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))

frame_1 = Frame(win, width=width, height=height, bg="#181823").place(x=0, y=0)
win.title('İşaret Dili Algılayıcı')
mylabel1 = Label(
    win,
    text='İşaret Dili Algılayıcı',
    font=('Comic Sans MS', 26, 'bold'),
    bd=5,
    bg='#20262E',
    fg='#F5EAEA',
    relief=GROOVE,
    width=5000
)
mylabel1.pack(pady=20, padx=500)

# Saat Güncelleyici Fonksiyon ve Tarih Ekranı
def update_clock():
    now = datetime.datetime.now()
    clock.config(text=now.strftime("%H:%M:%S"))
    clock.after(1000, update_clock)
##### === Saat Etiketi ===
clock = Label(
    win,
    font=("Arial", 20),
    relief=GROOVE,
    width=15,
    bd=5,
    fg="#F5EAEA",
    bg="#20262E"
)
clock.pack(anchor=NW, padx=150, pady=10)
clock.place(x=100, y=350)

##### === Takvim Etiketi ===
cal = Label(
    win,
    font=("Arial", 20),
    relief=GROOVE,
    width=15,
    bd=5,
    fg="#F5EAEA",
    bg="#20262E"
)
cal.pack(anchor=NW, padx=150, pady=10)
cal.place(x=100, y=400)

#### Saat güncelleme fonksiyonunu başlatıyoruz
update_clock()
cal.config(text=datetime.date.today().strftime("%B %d, %Y"))

# İsim ve Öğrenci Numarası Etiketleri 
namee = Label(
    win,
    text='Batuhan Öztürk',
    font=('Verdana', 14, 'bold'),
    relief=GROOVE,
    width=22,
    bd=5,
    fg="#F5EAEA",
    bg="#20262E"
)
namee.place(x=1200, y=650)



# Mediapipe Kurulumu ve Sınıf Tanımı
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class SignLanguageConverter:
    current_gesture = None
    global CountGesture
    CountGesture = StringVar()

    def __init__(self):

        pass

       #   detect_gesture Fonksiyonu
       
    def detect_gesture(self, image):
        
        with mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        ) as hands:
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                self.current_gesture = self.get_gesture(hand_landmarks)


#  get_gesture Fonksiyonu


    def get_gesture(self, hand_landmarks):
        
        thumb_tip = hand_landmarks.landmark[4]
        index_finger_tip = hand_landmarks.landmark[8]
        middle_finger_tip = hand_landmarks.landmark[12]
        ring_finger_tip = hand_landmarks.landmark[16]
        little_finger_tip = hand_landmarks.landmark[20]

        # Beğendim (başparmak yukarı) işareti kontrolü 
        if thumb_tip.y < index_finger_tip.y < middle_finger_tip.y < ring_finger_tip.y < little_finger_tip.y:
            CountGesture.set('BEĞENDİM')
            return "BEGENDIM"
        
        # Zafer işareti kontrolü (işaret ve orta parmak açık)

        elif (
            index_finger_tip.y < hand_landmarks.landmark[6].y and
            middle_finger_tip.y < hand_landmarks.landmark[10].y and
            ring_finger_tip.y > hand_landmarks.landmark[14].y and
            little_finger_tip.y > hand_landmarks.landmark[18].y and
            thumb_tip.x < hand_landmarks.landmark[2].x
            ):
            CountGesture.set('ZAFER')
            return "VICTORY"
        

        # Beğenmedim (başparmak aşağı) kontrolü
      
        elif thumb_tip.y > index_finger_tip.y > middle_finger_tip.y > ring_finger_tip.y > little_finger_tip.y:
            CountGesture.set('Beğenmedim')
            return "BEGENMEDIM"
        

        #  Bozkurt Jest Kontrolü  

        elif index_finger_tip.y < middle_finger_tip.y and abs(index_finger_tip.x - middle_finger_tip.x) < 0.2:
            CountGesture.set('Bozkurt')
            return "TURK SEMBOLU"
        
        
        # OK işareti (başparmak ve işaret parmağı ucu birbirine yakın)

        elif (
            abs(thumb_tip.x - index_finger_tip.x) < 0.05 and
            abs(thumb_tip.y - index_finger_tip.y) < 0.05 and
            middle_finger_tip.y < hand_landmarks.landmark[10].y and
            ring_finger_tip.y < hand_landmarks.landmark[14].y and
            little_finger_tip.y < hand_landmarks.landmark[18].y
            ):
                CountGesture.set('TAMAM')
                return "OK"
        
        # Dur işareti (avuç içi açık, tüm parmaklar yukarıda)
        elif (
            index_finger_tip.y < hand_landmarks.landmark[6].y and
            middle_finger_tip.y < hand_landmarks.landmark[10].y and
            ring_finger_tip.y < hand_landmarks.landmark[14].y and
            little_finger_tip.y < hand_landmarks.landmark[18].y and
            thumb_tip.x > hand_landmarks.landmark[2].x
            ):
                CountGesture.set('DUR')
                return "STOP"
       
        

         # Yumruk Hareketi (tüm parmak uçları bileğe yakın)
        else: 
            if (
        index_finger_tip.y > hand_landmarks.landmark[6].y and
        middle_finger_tip.y > hand_landmarks.landmark[10].y and
        ring_finger_tip.y > hand_landmarks.landmark[14].y and
        little_finger_tip.y > hand_landmarks.landmark[18].y and
        thumb_tip.x < hand_landmarks.landmark[2].x
    ):
                CountGesture.set('YUMRUK')
                return "YUMRUK"
            else:
                return None
            
           # get_current_gesture & release Fonksiyonları

    def get_current_gesture(self):
        """
        Mevcut jestin ne olduğunu dışarıya döndürür.
        """
        return self.current_gesture

    def release(self):
        """
        Kaynakları serbest bırakmak için kullanılabilir (Ör: self.hands.close()).
        """
        pass

# Seslendirme Özelliği 
def voice():
    engine = pyttsx3.init()
    engine.say((CountGesture.get()))
    engine.runAndWait()

### Çıkış Fonksiyonları 
def lbl():
    global label1
    label1.destroy()

def lbl2():
    global label1
    cv2.destroyAllWindows()
    label1.destroy()

# Çıkış Butonu ve Ses Butonu 
exit = Button(
    win, text='CIKIS',
    padx=95,
    bg='#20262E',
    fg='#F5EAEA',
    relief=GROOVE,
    width=7,
    bd=5,
    font=('Verdana', 14, 'bold'),
    command=win.destroy
)
exit.place(x=1200, y=400)

voic = Button(
    win, text='SES',
    padx=95,
    bg='#20262E',
    fg='#F5EAEA',
    relief=GROOVE,
    width=7,
    bd=5,
    font=('Verdana', 14, 'bold'),
    command=voice
)
voic.place(x=1200, y=350)

# Kameradan Görüntü Alma ve Ekranda Gösterme

sign_lang_conv = SignLanguageConverter()
cap = cv2.VideoCapture(0)
label1 = Label(frame_1, width=640, height=480)
label1.place(x=450, y=150)

def select_img():
    """
    Kameradan görüntü alır, jestleri tespit eder, ekranda gösterir.
    Ayrıca her defasında 'Current Gesture' etiketini günceller.
    """
    _, frame = cap.read()
    sign_lang_conv.detect_gesture(frame)
    gesture = sign_lang_conv.get_current_gesture()


    ##### Tespit edilen jest ekrana yazılır
    if gesture:
        cv2.putText(
            frame,
            gesture,
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

    #### Mediapipe ile el landmarklarının çizimi
    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as hands:
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    ##### OpenCV -> PIL -> ImageTk dönüşümü
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(framergb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage

    #### "Current Gesture :" etiketi ve sonucu
    crrgesture = Label(
        win,
        text='Current Gesture :',
        font=('Calibri', 18, 'bold'),
        bd=5,
        bg='#20262E',
        width=15,
        fg='#F5EAEA',
        relief=GROOVE
    )
    crrgesture.place(x=200, y=700)

    status = Label(
        win,
        textvariable=CountGesture,
        font=('Georgia', 18, 'bold'),
        bd=5,
        bg='#20262E',
        width=30,
        fg='#F5EAEA',
        relief=GROOVE
    )
    status.place(x=520, y=700)

    
    win.after(1, select_img)

### Fonksiyonları Başlatma 
select_img()
win.mainloop()
### Kamera ve diğer kaynakları serbest bırakma
cap.release()
sign_lang_conv.release()
cv2.destroyAllWindows()
#Son
