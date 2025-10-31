import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QGridLayout()
    layout.setSpacing(5)
    layout.setContentsMargins(5, 5, 5, 5)

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

    def display_item(reference, inventory):
        content = inventory.get(reference, "Empty")
        print(f"Compartment: {reference}, Content: {content}")

    
    for i in range (6):
        for j in range (6):
            letter  = chr(ord('A') + i)
            number = j + 1
            reference = f"{letter}{number}"

            button = QPushButton(reference)
            button.clicked.connect(lambda checked, ref=reference: display_item(ref, inventory))
            button.setFixedSize(80, 80)
            layout.addWidget(button, i, j)
    window.setLayout(layout)

    window.setWindowTitle("Smart Storage Assistant")
    window.setGeometry(100, 100, 800, 600)

    window.show()

    sys.exit(app.exec_())

