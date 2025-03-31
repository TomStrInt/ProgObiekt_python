import sys
import unicodedata
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QRadioButton, QCheckBox, QLineEdit, QPushButton, QScrollArea, QMessageBox
)
from PySide6.QtCore import Qt

def stylizuj_tekst(tekst):
    return f"<div style='border: 2px solid #ff8c00; color:black; padding:10px;'><b>{tekst}</b></div>"

def normalize_text(text):
  #uwzglednianie duzych i malych liter normalizacja tekstu, polskie znaki
    text = unicodedata.normalize("NFKD", text)
    text = "".join([c for c in text if not unicodedata.combining(c)])
    return " ".join(text.split()).lower()

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Harry Potter Quiz")
        self.resize(700, 800)

        scroll_area = QScrollArea()
        central_widget = QWidget()
        scroll_area.setWidget(central_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background-color: #2c2f33;")  
        self.setCentralWidget(scroll_area)

        main_layout = QVBoxLayout()

        # Question 1 (QGridLayout)
        q1_layout = QGridLayout()
        self.q1_label = QLabel(stylizuj_tekst("1. Jak nazywa się najlepszy przyjaciel Harry'ego Pottera?"))
        self.q1_radio1 = QRadioButton("Ron Weasley")
        self.q1_radio2 = QRadioButton("Draco Malfoy")
        self.q1_radio3 = QRadioButton("Neville Longbottom")
        q1_layout.addWidget(self.q1_label, 0, 0, 1, 3)
        q1_layout.addWidget(self.q1_radio1, 1, 0)
        q1_layout.addWidget(self.q1_radio2, 1, 1)
        q1_layout.addWidget(self.q1_radio3, 1, 2)
        main_layout.addLayout(q1_layout)

        # Question 2 (QGridLayout)
        q2_layout = QGridLayout()
        self.q2_label = QLabel(stylizuj_tekst("2. Kto był nauczycielem eliksirów w Hogwarcie?"))
        self.q2_checkbox1 = QCheckBox("Severus Snape")
        self.q2_checkbox2 = QCheckBox("Minerva McGonagall")
        self.q2_checkbox3 = QCheckBox("Rubeus Hagrid")
        q2_layout.addWidget(self.q2_label, 0, 0, 1, 3)
        q2_layout.addWidget(self.q2_checkbox1, 1, 0)
        q2_layout.addWidget(self.q2_checkbox2, 1, 1)
        q2_layout.addWidget(self.q2_checkbox3, 1, 2)
        main_layout.addLayout(q2_layout)

        # Question 3 (QFormLayout)
        form_layout_q3 = QFormLayout()
        self.q3_label = QLabel(stylizuj_tekst("3. Jakiego patronusa ma Harry Potter?"))
        self.q3_correct_label = QLabel("")
        self.q3_correct_label.setStyleSheet("color: green; font-style: italic;")  
        self.q3_input = QLineEdit()
        self.q3_input.setPlaceholderText("Wpisz odpowiedź...")
        form_layout_q3.addRow(self.q3_label)
        form_layout_q3.addRow("Odpowiedź:", self.q3_input)
        main_layout.addLayout(form_layout_q3)

        # Question 4 (QGridLayout)
        q4_layout = QGridLayout()
        self.q4_label = QLabel(stylizuj_tekst("4. Kim była siostra Albusa Dumbledore'a?"))
        self.q4_radio1 = QRadioButton("Ariana Dumbledore")
        self.q4_radio2 = QRadioButton("Helena Ravenclaw")
        self.q4_radio3 = QRadioButton("Bathilda Bagshot")
        q4_layout.addWidget(self.q4_label, 0, 0, 1, 3)
        q4_layout.addWidget(self.q4_radio1, 1, 0)
        q4_layout.addWidget(self.q4_radio2, 1, 1)
        q4_layout.addWidget(self.q4_radio3, 1, 2)
        main_layout.addLayout(q4_layout)

        # Question 5 (QGridLayout)
        q5_layout = QGridLayout()
        self.q5_label = QLabel(stylizuj_tekst("5. Które z poniższych stworzeń występuje w serii Harry Potter?"))
        self.q5_checkbox1 = QCheckBox("Zgredek (Domowy Skrzat)")
        self.q5_checkbox2 = QCheckBox("Centaur")
        self.q5_checkbox3 = QCheckBox("Feniks")
        q5_layout.addWidget(self.q5_label, 0, 0, 1, 3)
        q5_layout.addWidget(self.q5_checkbox1, 1, 0)
        q5_layout.addWidget(self.q5_checkbox2, 1, 1)
        q5_layout.addWidget(self.q5_checkbox3, 1, 2)
        main_layout.addLayout(q5_layout)

        # Submit Button (QHBoxLayout)
        footer_layout = QHBoxLayout()
        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        footer_layout.addWidget(self.check_button)
        main_layout.addLayout(footer_layout)

        central_widget.setLayout(main_layout)

    def sprawdzenie_odp(self):
        punkty = 0

        # Question 1: Ron Weasley
        if self.q1_radio1.isChecked():
            punkty += 1
        self.q1_radio1.setStyleSheet("color: green;")

        # Question 2: Severus Snape
        if self.q2_checkbox1.isChecked() and not self.q2_checkbox2.isChecked() and not self.q2_checkbox3.isChecked():
            punkty += 1
        self.q2_checkbox1.setStyleSheet("color: green;")

        # Question 3: Jeleń
        user_answer_q3 = normalize_text(self.q3_input.text())
        correct_answer_q3 = normalize_text("Jeleń")
        self.q3_correct_label.setText("Poprawna odpowiedź: Jeleń")
        if user_answer_q3 == correct_answer_q3:
            punkty += 1
            self.q3_input.setStyleSheet("background-color: lightgreen;")
        else:
            self.q3_input.setStyleSheet("background-color: red;")

        # Question 4: Ariana Dumbledore
        if self.q4_radio1.isChecked():
            punkty += 1
        self.q4_radio1.setStyleSheet("color: green;")

        # Question 5: Multi-choice answers
        self.q5_checkbox1.setStyleSheet("color: green;")
        self.q5_checkbox2.setStyleSheet("color: green;")
        self.q5_checkbox3.setStyleSheet("color: green;")
        if self.q5_checkbox1.isChecked() and self.q5_checkbox2.isChecked() and self.q5_checkbox3.isChecked():
            punkty += 1

        QMessageBox.information(self, "Wynik", f"Zdobyłeś {punkty} na 5 punktów!")

app = QApplication([])
quiz = Quiz()
quiz.show()
app.exec()
