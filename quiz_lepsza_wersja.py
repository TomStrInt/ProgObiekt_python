import sys
import unicodedata
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QHBoxLayout, QRadioButton, QCheckBox, QLineEdit, QPushButton, QScrollArea, QMessageBox
)
from PySide6.QtCore import Qt

def stylizuj_tekst(tekst):
    return f"<div style='border: 2px solid #ff8c00; color:black; padding:10px;'><b>{tekst}</b></div>"

def normalize_text(text):
  #normalizacja tekstu, uwzglednia nadmierne spacje, duze i male litery, polskie znaki i ich brak
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
        scroll_area.setStyleSheet("background-color: #2c2f33;")  # Dark navy-gray background
        self.setCentralWidget(scroll_area)

        main_layout = QVBoxLayout()

        # Question 1
        q1_layout = QVBoxLayout()
        self.q1_label = QLabel(stylizuj_tekst("1. Jak nazywa się najlepszy przyjaciel Harry'ego Pottera?"))
        self.q1_radio1 = QRadioButton("Ron Weasley")
        self.q1_radio2 = QRadioButton("Draco Malfoy")
        self.q1_radio3 = QRadioButton("Neville Longbottom")
        self.q1_radios = [self.q1_radio1, self.q1_radio2, self.q1_radio3]

        q1_layout.addWidget(self.q1_label)
        for radio in self.q1_radios:
            q1_layout.addWidget(radio)
        main_layout.addLayout(q1_layout)

        # Question 2
        q2_layout = QVBoxLayout()
        self.q2_label = QLabel(stylizuj_tekst("2. Kto był nauczycielem eliksirów w Hogwarcie?"))
        self.q2_checkbox1 = QCheckBox("Severus Snape")
        self.q2_checkbox2 = QCheckBox("Minerva McGonagall")
        self.q2_checkbox3 = QCheckBox("Rubeus Hagrid")
        self.q2_checkboxes = [self.q2_checkbox1, self.q2_checkbox2, self.q2_checkbox3]

        q2_layout.addWidget(self.q2_label)
        for checkbox in self.q2_checkboxes:
            q2_layout.addWidget(checkbox)
        main_layout.addLayout(q2_layout)

        # Question 3
        q3_layout = QVBoxLayout()
        self.q3_label = QLabel(stylizuj_tekst("3. Jakiego patronusa ma Harry Potter?"))
        self.q3_correct_label = QLabel("")
        self.q3_correct_label.setStyleSheet("color: green; font-style: italic;")  # Correct answer style
        self.q3_input = QLineEdit()
        self.q3_input.setPlaceholderText("Wpisz odpowiedź...")

        q3_layout.addWidget(self.q3_label)
        q3_layout.addWidget(self.q3_correct_label)  # Display correct answer above input
        q3_layout.addWidget(self.q3_input)
        main_layout.addLayout(q3_layout)

        # Question 4
        q4_layout = QVBoxLayout()
        self.q4_label = QLabel(stylizuj_tekst("4. Kim była siostra Albusa Dumbledore'a?"))
        self.q4_radio1 = QRadioButton("Ariana Dumbledore")
        self.q4_radio2 = QRadioButton("Helena Ravenclaw")
        self.q4_radio3 = QRadioButton("Bathilda Bagshot")
        self.q4_radios = [self.q4_radio1, self.q4_radio2, self.q4_radio3]

        q4_layout.addWidget(self.q4_label)
        for radio in self.q4_radios:
            q4_layout.addWidget(radio)
        main_layout.addLayout(q4_layout)

        # Question 5
        q5_layout = QVBoxLayout()
        self.q5_label = QLabel(stylizuj_tekst("5. Które z poniższych stworzeń występuje w serii Harry Potter?"))
        self.q5_checkbox1 = QCheckBox("Zgredek (Domowy Skrzat)")
        self.q5_checkbox2 = QCheckBox("Centaur")
        self.q5_checkbox3 = QCheckBox("Feniks")
        self.q5_checkboxes = [self.q5_checkbox1, self.q5_checkbox2, self.q5_checkbox3]

        q5_layout.addWidget(self.q5_label)
        for checkbox in self.q5_checkboxes:
            q5_layout.addWidget(checkbox)
        main_layout.addLayout(q5_layout)

        # Submit Button
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
        self.q3_correct_label.setText("Poprawna odpowiedź: Jeleń")  # Display correct answer
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
