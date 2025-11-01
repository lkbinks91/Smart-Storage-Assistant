import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtWidgets import QGridLayout, QPushButton, QLabel


def display_item(reference, inventory):
        content = inventory.get(reference, "Empty")
        print(f"Compartment: {reference}, Content: {content}")
        info_label.setText(f"Content : {content}")

def highlight_project(project_name, projects, buttons):
    # Réinitialiser toutes les couleurs
    for btn in buttons.values():
        btn.setStyleSheet("background-color: none;")
    # Colorer les cases du projet
    for ref in projects.get(project_name, []):
        if ref in buttons:
            buttons[ref].setStyleSheet("background-color: lightgreen;")



projects = {    
            "Mini Station Raspberry": ["A1", "B1", "B2", "B3", "C3"],
            "Clignotant Arduino": ["A2", "B1", "B2", "B3", "C3"],
            "Station météo mini": ["A3", "B1", "B2", "F1", "C3"],
            "Petit robot moteur": ["A3", "B1", "B2", "C4", "C5", "D1"],
            "Station son / caméra": ["A1", "D4", "D5", "D6", "E1", "E4", "E6"],
            "Système de sécurité IoT": ["A3", "B1", "B2", "F2", "F3", "F6"],
        }

inventory = {
        "A1": "Raspberry Pi",
        "A2": "Arduino",
        "A3": "ESP32",
        "A4": "ESP8266",
        "A5": "ESP32",
        "A6": "ESP8266",
        "B1": "Breadboard",
        "B2": "Jumper Wires",
        "B3": "Resistors",
        "B4": "Capacitors",
        "B5": "Inductors",
        "B6": "Transistors",
        "C1": "ICs",
        "C2": "Diodes",
        "C3": "LEDs",
        "C4": "Motors",
        "C5": "Sensors",
        "C6": "Actuators",
        "D1": "Battery",
        "D2": "Power Supply",
        "D3": "Battery Pack",
        "D4": "Monitors",
        "D5": "Keyboards",
        "D6": "Mice",
        "E1": "microphone",
        "E2": "Scanners",
        "E3": "Projectors",
        "E4": "Speakers",
        "E5": "Microphones",
        "E6": "Headphones",
        "F1": "temperature sensor",
        "F2": "ultrasonic sensor",
        "F3": "motion sensor",
        "F4": "humidity sensor",
        "F5": "pressure sensor",
        "F6": "camera sensor",
    }



if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = QWidget()
    layout = QGridLayout()
    layout.setSpacing(5)
    layout.setContentsMargins(5, 5, 5, 5)
    main_layout = QVBoxLayout()
    window.setLayout(main_layout)


    combo = QComboBox()
    combo.addItems(projects.keys())
    main_layout.addWidget(combo)

    info_label = QLabel("Choisis une case pour voir son contenu")
    main_layout.addWidget(info_label)

    layout = QGridLayout()
    layout.setSpacing(5)
    layout.setContentsMargins(5, 5, 5, 5)
    main_layout.addLayout(layout)

    buttons = {}
    
    for i in range (6):
        for j in range (6):
            letter  = chr(ord('A') + i)
            number = j + 1
            reference = f"{letter}{number}"

            button = QPushButton(reference)
            button.clicked.connect(lambda checked, ref=reference: display_item(ref, inventory))
            button.setFixedSize(80, 80)
            layout.addWidget(button, i, j)
            buttons[reference] = button

    combo.currentTextChanged.connect(lambda text: highlight_project(text, projects, buttons))

    window.setWindowTitle("Smart Storage Assistant")
    window.setGeometry(100, 100, 800, 600)

    window.show()
  

    sys.exit(app.exec_())

