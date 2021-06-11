import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui


class Main(pq.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle('Forms !!')
        #self.setLayout(pq.QVBoxLayout())

        form_layout = pq.QFormLayout()
        self.setLayout(form_layout)

        # add stuff
        my_lable = pq.QLabel('It is a lable ')
        my_lable.setFont(gui.QFont('Helvetica', 12))

        first_name = pq.QLineEdit()
        last_name = pq.QLineEdit()

        # add rows to the app
        form_layout.addRow(my_lable)
        # form_layout.addRow('first name ', first_name)
        form_layout.addRow(first_name, last_name)
        form_layout.addRow(pq.QPushButton('Push Button'))

        self.show()


app = pq.QApplication([])
main = Main()
app.exec_()