from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


def on_button_click():
    print("Test")
    
app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt Example")
window.resize(800,600)

layout = QVBoxLayout()

button = QPushButton("Click Me!")
button.clicked.connect(on_button_click)
button.setFixedSize(200,50)
button.move(50,400)


layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec_()