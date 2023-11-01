import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)

"""
# 메서드
setCheckable() True 설정 시, 누른 상태와 그렇지 않은 상태를 구분합니다.
toggle() 상태를 바꿉니다.
setIcon() 버튼의 아이콘을 설정합니다.
setEnabled() False 설정 시, 버튼을 사용할 수 없습니다.
isChecked() 버튼의 선택 여부를 반환합니다.
setText() 버튼에 표시될 텍스트를 설정합니다.
text() 버튼에 표시된 텍스트를 반환합니다

# 시그널
clicked()	버튼을 클릭할 때 발생합니다.
pressed()	버튼이 눌렸을 때 발생합니다.
released()	버튼을 눌렀다 뗄 때 발생합니다.
toggled()	버튼의 상태가 바뀔 때 발생합니다.
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("&Button1", self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn1.toggled.connect(self.clickBtn)

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    @pyqtSlot(bool)
    def clickBtn(self, state):
        self.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
