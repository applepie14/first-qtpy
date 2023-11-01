import sys
from PyQt5.QtWidgets import QApplication, QWidget, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Q')
        exitAction.setStatusTip('Stop Rulet')
        exitAction.triggered.connect(qApp.quit)

        self.setWindowTitle('식집사')
        self.setWindowIcon(QIcon('plant.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
