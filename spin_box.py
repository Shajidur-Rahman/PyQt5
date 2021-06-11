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

        my_lable = qt.QLabel('Pick something from the list !!')

        # changing the fonts
        my_lable.setFont(qtg.QFont('Helvetica', 18))

        # display to the window
        self.layout().addWidget(my_lable)

        # crearting a spin box

        my_spin = qt.QSpinBox(self, value=5, maximum=50,singleStep=5, minimum=-50, prefix='The number ', suffix=' It is ')
        my_spin.setFont(qtg.QFont('Helvetica', 18))

        # Add items to the box
        # my_spin.addItem('Mango')
        # my_spin.addItem('Apple')
        # my_spin.addItem('Orange')
        # my_spin.addItem('Banana')

        #put spin box on the screen
        self.layout().addWidget(my_spin)


        # creating a button
        my_button = qt.QPushButton('Press me !!', clicked=lambda : pick())
        self.layout().addWidget(my_button)

        def pick():
            my_lable.setText(f'You picked {my_spin.value()}')

        self.show()


app = qt.QApplication([])
mw = Main()
app.exec_()