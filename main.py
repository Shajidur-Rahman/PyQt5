import sys

from PyQt5.QtWidgets import *

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()

        
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())