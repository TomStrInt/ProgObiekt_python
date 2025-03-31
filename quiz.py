import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QRadioButton, QCheckBox, QPushButton,
    QScrollArea, QButtonGroup, QMessageBox
)
from PySide6.QtCore import Qt

def stylizuj_tekst(tekst):
    return f"<div style='background-color:white; color:black; padding:5px;'><b>{tekst}</b></div>"

class Quiz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Harry Potter Quiz")

        scroll_area = QScrollArea()
        centralny_widget = QWidget()
        scroll_area.setWidget(centralny_widget)
        scroll_area.setWidgetResizable(True)
        self.setCentralWidget(scroll_area)
        self.resize(500, 700)

      
        scroll_area.setStyleSheet("background-color: #0c1a34;")  # Kolor tła: ciemnogranatowy (hex: #0c1a34)

        layout = QVBoxLayout()

        self.tytul = QLabel("HARRY POTTER QUIZ - PYTANIA O CZARODZIEJACH")
        self.tytul.setAlignment(Qt.AlignCenter)
        self.tytul.setStyleSheet("font-weight: bold; color: white;")  # Białe litery na ciemnogranatowym tle
        layout.addWidget(self.tytul)

        # Pytanie nr 1
        self.pytanie1 = QLabel(stylizuj_tekst("1. Jak nazywa się najlepszy przyjaciel Harry'ego Pottera?"))
        self.radio_group1 = QButtonGroup(self)
        self.radio_button1_1 = QRadioButton("Ron Weasley")
        self.radio_button1_2 = QRadioButton("Draco Malfoy")
        self.radio_button1_3 = QRadioButton("Neville Longbottom")
        self.radio_group1.addButton(self.radio_button1_1)
        self.radio_group1.addButton(self.radio_button1_2)
        self.radio_group1.addButton(self.radio_button1_3)

        layout.addWidget(self.pytanie1)
        layout.addWidget(self.radio_button1_1)
        layout.addWidget(self.radio_button1_2)
        layout.addWidget(self.radio_button1_3)

        # Pytanie nr 2
        self.pytanie2 = QLabel(stylizuj_tekst("2. Kto z poniższych był nauczycielem eliksirów w Hogwarcie?"))
        self.checkbox2_1 = QCheckBox("Severus Snape")
        self.checkbox2_2 = QCheckBox("Minerva McGonagall")
        self.checkbox2_3 = QCheckBox("Rubeus Hagrid")

        layout.addWidget(self.pytanie2)
        layout.addWidget(self.checkbox2_1)
        layout.addWidget(self.checkbox2_2)
        layout.addWidget(self.checkbox2_3)

        # Pytanie nr 3
        self.pytanie3 = QLabel(stylizuj_tekst("3. Jakiego patronusa ma Harry Potter?"))
        self.radio_group3 = QButtonGroup(self)
        self.radio_button3_1 = QRadioButton("Jeleń")
        self.radio_button3_2 = QRadioButton("Wilk")
        self.radio_button3_3 = QRadioButton("Kot")
        self.radio_group3.addButton(self.radio_button3_1)
        self.radio_group3.addButton(self.radio_button3_2)
        self.radio_group3.addButton(self.radio_button3_3)

        layout.addWidget(self.pytanie3)
        layout.addWidget(self.radio_button3_1)
        layout.addWidget(self.radio_button3_2)
        layout.addWidget(self.radio_button3_3)

        # Pytanie nr 4
        self.pytanie4 = QLabel(stylizuj_tekst("4. Kim była siostra Albusa Dumbledore'a?"))
        self.radio_group4 = QButtonGroup(self)
        self.radio_button4_1 = QRadioButton("Ariana Dumbledore")
        self.radio_button4_2 = QRadioButton("Helena Ravenclaw")
        self.radio_button4_3 = QRadioButton("Bathilda Bagshot")
        self.radio_group4.addButton(self.radio_button4_1)
        self.radio_group4.addButton(self.radio_button4_2)
        self.radio_group4.addButton(self.radio_button4_3)

        layout.addWidget(self.pytanie4)
        layout.addWidget(self.radio_button4_1)
        layout.addWidget(self.radio_button4_2)
        layout.addWidget(self.radio_button4_3)

        # Pytanie nr 5
        self.pytanie5 = QLabel(stylizuj_tekst("5. Które z poniższych stworzeń występuje w serii Harry Potter?"))
        self.checkbox5_1 = QCheckBox("Zgredek (Domowy Skrzat)")
        self.checkbox5_2 = QCheckBox("Centaur")
        self.checkbox5_3 = QCheckBox("Feniks")

        layout.addWidget(self.pytanie5)
        layout.addWidget(self.checkbox5_1)
        layout.addWidget(self.checkbox5_2)
        layout.addWidget(self.checkbox5_3)

        centralny_widget.setLayout(layout)

        # Przycisk do sprawdzania odpowiedzi
        self.check_button = QPushButton("Sprawdź")
        self.check_button.clicked.connect(self.sprawdzenie_odp)
        layout.addWidget(self.check_button)

    def sprawdzenie_odp(self):
        punkty = 0

        if self.radio_button1_1.isChecked():
            punkty += 1

        if self.checkbox2_1.isChecked() and not self.checkbox2_2.isChecked() and not self.checkbox2_3.isChecked():
            punkty += 1

        if self.radio_button3_1.isChecked():
            punkty += 1

        if self.radio_button4_1.isChecked():
            punkty += 1

        if self.checkbox5_1.isChecked() and self.checkbox5_2.isChecked() and self.checkbox5_3.isChecked():
            punkty += 1

        QMessageBox.information(self, "Wynik", f"Zdobyłeś {punkty} na 5 punktów!")

app = QApplication([])
quiz = Quiz()
quiz.show()
app.exec()
