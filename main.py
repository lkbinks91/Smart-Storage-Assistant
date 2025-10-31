import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QGridLayout()
    layout.setSpacing(5)
    layout.setContentsMargins(5, 5, 5, 5)


 
    
    for i in range (6):
        for j in range (6):
            letter  = chr(ord('A') + i)
            number = j + 1
            reference = f"{letter}{number}"

            button = QPushButton(reference)
            button.setFixedSize(80, 80)
            layout.addWidget(button, i, j)
    window.setLayout(layout)

    window.setWindowTitle("Smart Storage Assistant")
    window.setGeometry(100, 100, 800, 600)

    window.show()

    sys.exit(app.exec_())

