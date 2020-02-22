from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup as bs
from requests import get 
from os import system 
import design
import sys

class App(QMainWindow, design.Ui_GitAutocloner):
    def __init__(self):
        super().__init__()
        self.ui = design.Ui_GitAutocloner()
        self.ui.setupUi(self)
        self.ui.btn_clone.clicked.connect(self.clone)
        self.ui.btn_clone_all.clicked.connect(self.clone_all)

    def clone(self):
        links_for_cloning = self.ui.links.toPlainText().split('\n')
        for k in links_for_cloning:
            k = k.strip()
            if k == '': continue
            system(f'git clone {k}')
        QMessageBox.about(self, 'OK', 'Completed! :D')

    def clone_all(self):
        if self.ui.is_clone_all.isChecked() == True:
            username = self.ui.profile.text().strip().split('/')[-1]
            git = bs(get(f'https://github.com/{username}?tab=repositories').text)
            for k in git.find_all('a', itemprop='name codeRepository'):
                system(f'git clone https://github.com/{username}/{k.text.strip()}')
            QMessageBox.about(self, 'OK', 'Completed! :D')
        else:
            QMessageBox.about(self, 'Error', 'Checkbox isn\'t selected.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
