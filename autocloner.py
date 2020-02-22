from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from os import system 
import design
import sys

class App(QMainWindow, design.Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = design.Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_clone.clicked.connect(self.clone)

    def clone(self):
        links_for_cloning = self.ui.links.toPlainText().split('\n')
        for k in links_for_cloning:
            k = k.strip()
            if k == '': continue
            system(f'git clone {k}')
        QMessageBox.about(self, 'OK', 'Completed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
