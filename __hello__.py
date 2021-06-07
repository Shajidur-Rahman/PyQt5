import  PyQt5.QtWidgets as qt
import  PyQt5.QtGui as qtg


class Main(qt.QWidget):
    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle('__HELLO__')
        self.setLayout(qt.QVBoxLayout())

        my_lable = qt.QLabel("Hello world")

        my_lable.setFont(qtg.QFont('Dancing Script', 15))

        self.layout().addWidget(my_lable)

        my_enter = qt.QLineEdit()
        my_enter.setObjectName('name')
        # my_enter.setText('Enter your name')

        self.layout().addWidget(my_enter)


        my_button = qt.QPushButton('Click me', clicked = lambda : click_me())

        self.layout().addWidget(my_button)

        def click_me():
            my_lable.setText(f"Good morning {my_enter.text()}")
            my_enter.clear()

        self.show()


app = qt.QApplication([])
window = Main()
app.exec_()