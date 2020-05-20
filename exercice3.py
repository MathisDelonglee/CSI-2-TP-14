from PySide2.QtWidgets import *
from PySide2.QtGui import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setFixedSize(400,300)
        #self.setWindowTitle(QIcon('drapeaufr.png'))

        self.__layout = QVBoxLayout()

        self.__QLabel = QLabel("HelloWord")
        self.__QLabel.setAlignment(Qt.AlignCenter)

        self.__QprogrssBar = QProgressBar()
        self.__QprogrssBar.setValue(50)

        self.__QLineEdit = QLineEdit()

        self.__Boutton = QPushButton('Click me !')
        self.__Boutton.setToolTip('Salut mon pote')

        self.__layout.addWidget(self.__QLabel)
        self.__layout.addWidget(self.__QprogrssBar)
        self.__layout.addWidget(self.__QLineEdit)
        self.__layout.addWidget(self.__Boutton)

        self.setLayout(self.__layout)

if __name__ == "__main__":
    app = QApplication([])
    ihm = IHM()
    ihm.show()
    app.exec_()
