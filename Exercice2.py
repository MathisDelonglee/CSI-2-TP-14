from PySide2.QtWidgets import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.__layout = QGridLayout()

        self.__QLabel = QLabel("Laisser un commentaire")
        self.__QTextEdit = QTextEdit()
        self.__Boutton1 = QPushButton('Sucess')
        self.__Boutton2 = QPushButton('Cancel')

        self.__layout.addWidget(self.__QLabel)
        self.__layout.addWidget(self.__QTextEdit)

        self.__layout.addWidget(self.__Boutton1,2,0)
        self.__layout.addWidget(self.__Boutton2,2,1)


        self.setLayout(self.__layout)



if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()
