import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime


# more details > https://wikidocs.net/22074
# now = QDate.currentDate()
# print(now.toString())  # 월 10 30 2023
# print(now.toString('d.M.yy'))  # 30.10.23
# print(now.toString('dd.MM.yyyy'))  # 30.10.2023
# print(now.toString('ddd.MMMM,yyyy'))  # 월.10월,2023
# print(now.toString(Qt.ISODate))  # 2023-10-30
# print(now.toString(Qt.DefaultLocaleLongDate))  # 2023년 10월 30일 월요일
#
# time = QTime.currentTime()
# print(time.toString())  # 14:32:52
# print(time.toString('h.m.s'))  # 14.34.24
# print(time.toString('hh.mm.ss'))  # 14.34.24
# print(time.toString('hh.mm.ss.zzz'))  # 14.34.24.414
# print(time.toString(Qt.DefaultLocaleLongDate))  # 오후 2:34:24
# print(time.toString(Qt.DefaultLocaleShortDate))  # 오후 2:34
#
#
# dateTime = QDateTime.currentDateTime()
# print(dateTime.toString())  # 월 10 30 14:35:40 2023
# print(dateTime.toString('d.M.yy hh:mm:ss'))  # 30.10.23 14:36:51
# print(dateTime.toString('dd.MM.yyyy, hh:mm:ss'))  # 30.10.2023, 14:36:51
# print(dateTime.toString(Qt.DefaultLocaleLongDate))  # 2023년 10월 30일 월요일 오후 2:36:51
# print(dateTime.toString(Qt.DefaultLocaleShortDate))  # 2023-10-30 오후 2:36

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
