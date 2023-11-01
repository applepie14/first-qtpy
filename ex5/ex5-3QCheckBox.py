import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QCheckBox)

"""
메서드 
text()	체크 박스의 라벨 텍스트를 반환합니다.
setText()	체크 박스의 라벨 텍스트를 설정합니다.
isChecked()	체크 박스의 상태를 반환합니다. (True/False)
checkState()	체크 박스의 상태를 반환합니다. (2/1/0)
toggle()	체크 박스의 상태를 변경합니다.

시그널
pressed()	체크 박스를 누를 때 신호를 발생합니다.
released()	체크 박스에서 뗄 때 신호를 발생합니다.
clicked()	체크 박스를 클릭할 때 신호를 발생합니다.
stateChanged()	체크 박스의 상태가 바뀔 때 신호를 발생합니다.
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
