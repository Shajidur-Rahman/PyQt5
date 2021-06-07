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

        # crearting a combo box

        my_combo = qt.QComboBox(self, editable=True, insertPolicy=qt.QComboBox.InsertAtTop)

        # Add items to the box
        my_combo.addItem('Mango')
        my_combo.addItem('Apple')
        my_combo.addItem('Orange')
        my_combo.addItem('Banana')

        #put combo box on the screen
        self.layout().addWidget(my_combo)


        # creating a button
        my_button = qt.QPushButton('Press me !!', clicked=lambda : pick())
        self.layout().addWidget(my_button)

        def pick():
            my_lable.setText(f'You picked {my_combo.currentText()}')


        # show the app
        self.show()


app = qt.QApplication([])
mw = Main()
app.exec_()