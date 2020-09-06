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

        for link in links_for_cloning:
            link = link.strip()
            if link != '':
                system(f'git clone {link}')

        QMessageBox.about(self, 'OK', 'Completed! :D')

    def clone_all(self):
        if self.ui.is_clone_all.isChecked() == True:
            git_username = self.ui.profile.text().strip().split('/')[-1]
            git_repos = bs(get(f'https://github.com/{git_username}?tab=repositories').text)
            for repo in git_repos.find_all('a', itemprop='name codeRepository'):
                system(f'git clone https://github.com/{git_username}/{repo.text.strip()}')
            QMessageBox.about(self, 'OK', 'Completed! :D')
        else:
            QMessageBox.about(self, 'Error', 'First select the checkbox \'Clone all repos from account\'.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
