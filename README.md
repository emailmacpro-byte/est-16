# RIASEC Мэргэжлийн Зөвлөгөө Вэб Апп
## John L. Holland-ын RIASEC онолд суурилсан

---

## 📦 Суулгах заавар

### 1. Python шаардлага
Python 3.8 ба түүнээс дээш хувилбар шаардлагатай.

### 2. Хавтас руу орох
```bash
cd riasec_app
```

### 3. Виртуал орчин үүсгэх (санал болгож байна)
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 4. Хамааралт багцуудыг суулгах
```bash
pip install -r requirements.txt
```

### 5. Апп ажиллуулах
```bash
python app.py
```

### 6. Браузерт нээх
```
http://localhost:5000
```

---

## 🗂️ Файлын бүтэц

```
riasec_app/
├── app.py              ← Flask серверийн үндсэн файл
├── questions.py        ← Богино (30) ба урт (60) тестийн асуултууд
├── riasec_types.py     ← 6 RIASEC хэв шинжийн мэдээлэл
├── careers.py          ← Мэргэжлийн өгөгдлийн сан
├── requirements.txt    ← Python хамааралт багцууд
├── README.md           ← Энэ файл
└── templates/
    ├── index.html      ← Нүүр хуудас
    ├── test.html       ← Тестийн хуудас
    └── result.html     ← Үр дүнгийн хуудас
```

---

## ✨ Функцуудын тайлбар

### Тест
- **Богино тест**: 30 асуулт, ~10 минут
- **Дэлгэрэнгүй тест**: 60 асуулт, ~20 минут

### Оноолол
- 5 оноот хуваарь (1=Огт тийм биш, 5=Маш тийм)
- Хувийн дүн шинжилгээ хийж Holland код гаргана

### Үр дүн
- Holland код (жишээ: RIA, SEC, EIS...)
- Top 3 хэв шинжийн дэлгэрэнгүй тайлбар
- Оноог хувиар харуулах
- Тохирох мэргэжлүүдийн жагсаалт
- Хувийн зөвлөгөө

---

## 🎨 Технологи

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Font**: Plus Jakarta Sans (Google Fonts)
- **Дизайн**: Монохром + Accent өнгөт систем

---

## 👨‍💼 Зориулалт

- Мэргэжлийн зөвлөгч, сэтгэл зүйч нарт
- Сургуулийн чиг баримжаагийн ажилтнуудад
- Хүүхэд, өсвөр насны хүмүүсийн хэв шинж тодорхойлоход
- HR менежерүүдэд

---

## 📚 Эх сурвалж

Holland, J. L. (1997). Making vocational choices: A theory of vocational personalities and work environments (3rd ed.). Psychological Assessment Resources.
