import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QGridLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QSpinBox
)

class LayoutDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout Demo App")
        self.resize(600, 400)

        # Główny widget i layout
        central_widget = QWidget(self)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Sekcja 1: QVBoxLayout (Nagłówek)
        header_layout = QVBoxLayout()
        header_label = QLabel("Witamy w aplikacji Layout Demo!")
        header_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")
        header_layout.addWidget(header_label)
        main_layout.addLayout(header_layout)

        # Sekcja 2: QHBoxLayout (Opcje w poziomie)
        options_layout = QHBoxLayout()
        label_option = QLabel("Wybierz opcję:")
        dropdown_option = QComboBox()
        dropdown_option.addItems(["Opcja 1", "Opcja 2", "Opcja 3"])
        button_submit = QPushButton("Zatwierdź")
        options_layout.addWidget(label_option)
        options_layout.addWidget(dropdown_option)
        options_layout.addWidget(button_submit)
        main_layout.addLayout(options_layout)

        # Sekcja 3: QGridLayout (Tabelaryczne wprowadzanie danych)
        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Imię:"), 0, 0)
        grid_layout.addWidget(QLineEdit(), 0, 1)
        grid_layout.addWidget(QLabel("Nazwisko:"), 1, 0)
        grid_layout.addWidget(QLineEdit(), 1, 1)
        grid_layout.addWidget(QLabel("Wiek:"), 2, 0)
        grid_layout.addWidget(QSpinBox(), 2, 1)
        main_layout.addLayout(grid_layout)

        # Sekcja 4: QFormLayout (Formularz)
        form_layout = QFormLayout()
        form_layout.addRow("Adres e-mail:", QLineEdit())
        form_layout.addRow("Numer telefonu:", QLineEdit())
        main_layout.addLayout(form_layout)

        # Sekcja 5: Przyciski na dole (QHBoxLayout)
        buttons_layout = QHBoxLayout()
        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Anuluj")
        buttons_layout.addWidget(button_ok)
        buttons_layout.addWidget(button_cancel)
        main_layout.addLayout(buttons_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LayoutDemo()
    demo.show()
    sys.exit(app.exec())
