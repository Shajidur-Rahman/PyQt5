import PyQt5.QtWidgets as qt # importing pyqt5
import PyQt5.QtGui as qtg


class Main(qt.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        # add title
        self.setWindowTitle('Hello World')
        # set layout
        self.setLayout(qt.QVBoxLayout())

        # creating a lable

        my_lable = qt.QLabel('Hello world !!')

        # changing the fonts
        my_lable.setFont(qtg.QFont('Helvetica', 18))

        # display to the window
        self.layout().addWidget(my_lable)

        # crearting a entry box
        my_enter = qt.QLineEdit()
        my_enter.setObjectName('Name')
        self.layout().addWidget(my_enter)

        # creating a button
        my_button = qt.QPushButton('Press me !!', clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            # add lable to the box 
            my_lable.setText(f"Hello {my_enter.text()} !!")
            # clear the input box
            my_enter.setText('')

        # show the app
        self.show()


app = qt.QApplication([])
mw = Main()
app.exec_()