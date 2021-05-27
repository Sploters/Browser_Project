import os
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
        self.setCentralWidget(self.browser)
        # self.browser.urlChanged.connect(self.update_urlbar)
        # self.browser.loadFinished.connect(self.update_title)

        self.setWindowIcon(QtGui.QIcon('./img/shark.svg'))

        # navbar
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(16, 16))
        self.addToolBar(navbar)

        back_btn = QAction(
            QIcon('./img/back.svg'), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        next_btn = QAction(
            QIcon('./img/forward.svg'), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)

        reload_btn = QAction(
            QIcon('./img/reload.svg'), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(
            QIcon('./img/home.svg'), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # self.httpsicon = QLabel()  # Yes, really!
        # self.httpsicon.setPixmap(
        #     QPixmap(os.path.join('icons', 'lock-nossl.png')))
        # navbar.addWidget(self.httpsicon)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        stop_btn = QAction(
            QIcon('./img/stop.svg'), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        self.browser.urlChanged.connect(self.update_url)

        self.show()

        # self.setWindowTitle("Sploters Browser")
        # self.setWindowIcon(QIcon('./img/shark.svg'), "Shark", self)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_url(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Sploters Browser" % title)


app = QApplication(sys.argv)
# browser name in Windowed mode
app.setApplicationName('Sploters Browser')
app.setOrganizationName('Sploters')
app.setOrganizationDomain('duckduckgo.com')
window = MainWindow()

app.exec_()
