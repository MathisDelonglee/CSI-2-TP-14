from PySide2.QtWidgets import QLabel,QWidget,QPushButton,QApplication,QVBoxLayout,QProgressBar

app = QApplication([])
mainWidget = QWidget()

layout = QVBoxLayout()

label = QLabel("Voulez vous continuer le TP?")
button1 = QPushButton('Oui')
button2 = QPushButton('Non')
Bar = QProgressBar()

layout.addWidget(label)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(Bar)

mainWidget.setLayout(layout)

mainWidget.show()
app.exec_()
