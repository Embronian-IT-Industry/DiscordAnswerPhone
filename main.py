import fix_qt_import_error
from discord import Client, LoginFailure
import random
import asyncio
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from asyncqt import QEventLoop, asyncSlot


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(380, 320, 181, 23))
        self.run_button.setObjectName("run_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 161, 16))
        self.label.setObjectName("label")
        self.token_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.token_edit.setGeometry(QtCore.QRect(30, 40, 201, 31))
        self.token_edit.setObjectName("token_edit")
        self.min_box = QtWidgets.QSpinBox(self.centralwidget)
        self.min_box.setGeometry(QtCore.QRect(320, 30, 51, 31))
        self.min_box.setReadOnly(False)
        self.min_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.min_box.setMinimum(5)
        self.min_box.setMaximum(89)
        self.min_box.setObjectName("min_box")
        self.max_box = QtWidgets.QSpinBox(self.centralwidget)
        self.max_box.setGeometry(QtCore.QRect(400, 30, 51, 31))
        self.max_box.setReadOnly(False)
        self.max_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.max_box.setMinimum(6)
        self.max_box.setMaximum(90)
        self.max_box.setObjectName("max_box")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 10, 31, 16))
        self.label_3.setObjectName("label_3")
        self.channel_id_line = QtWidgets.QLineEdit(self.centralwidget)
        self.channel_id_line.setGeometry(QtCore.QRect(30, 130, 181, 20))
        self.channel_id_line.setMaxLength(20)
        self.channel_id_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.channel_id_line.setObjectName("channel_id_line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 161, 16))
        self.label_4.setObjectName("label_4")
        self.phrase_1_box = QtWidgets.QLineEdit(self.centralwidget)
        self.phrase_1_box.setGeometry(QtCore.QRect(30, 190, 181, 20))
        self.phrase_1_box.setMaxLength(20)
        self.phrase_1_box.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.phrase_1_box.setObjectName("phrase_1_box")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 170, 231, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 111, 16))
        self.label_6.setObjectName("label_6")
        self.phrase_1_box_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.phrase_1_box_2.setGeometry(QtCore.QRect(30, 250, 181, 20))
        self.phrase_1_box_2.setMaxLength(20)
        self.phrase_1_box_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.phrase_1_box_2.setObjectName("phrase_1_box_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 230, 111, 16))
        self.label_7.setObjectName("label_7")
        self.start_number = QtWidgets.QLineEdit(self.centralwidget)
        self.start_number.setGeometry(QtCore.QRect(330, 250, 41, 20))
        self.start_number.setMaxLength(20)
        self.start_number.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.start_number.setObjectName("start_number")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Economy destructor"))
        self.run_button.setText(_translate("MainWindow", "RUN ASSISTANT"))
        self.label.setText(_translate("MainWindow", "Введите token от аккаунта"))
        self.label_2.setText(_translate("MainWindow", "MIN "))
        self.label_3.setText(_translate("MainWindow", "MAX"))
        self.label_4.setText(_translate("MainWindow", "ID канала для работы"))
        self.label_5.setText(_translate("MainWindow", "Тип действия (добываю/строю и т.д.)"))
        self.label_6.setText(_translate("MainWindow", "Ресурс/постройка"))
        self.label_7.setText(_translate("MainWindow", "Стартовое значение"))


class Game(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.min_sleep_time = 5
        self.max_sleep_time = 6
        self.client = DSBotClient()

        self.client.loop.create_task(auto_message())

    def initUI(self):
        super().setupUi(self)
        self.max_box.valueChanged.connect(self.change_max)
        self.min_box.valueChanged.connect(self.change_min)
        self.run_button.clicked.connect(self.run_discord)

    def change_max(self):
        self.min_box.setMaximum(self.max_box.value() - 1)
        self.max_sleep_time = self.max_box.value()

    def change_min(self):
        self.max_box.setMinimum(self.min_box.value() + 1)
        self.min_sleep_time = self.min_box.value()

    @asyncSlot()
    async def run_discord(self):
        try:
            self.channel_id = int(self.channel_id_line.text())
        except Exception:
            self.statusBar().showMessage('ID канала - число!')
            return
        try:
            self.counter = int(self.start_number.text())
        except Exception:
            self.statusBar().showMessage('Стартовое значение это число!')
            return
        self.resourse = self.phrase_1_box_2.text()
        self.work = self.phrase_1_box.text()
        self.token = self.token_edit.text()
        if not all((self.token, self.resourse, self.work)):
            self.statusBar().showMessage('Необходимо заполнить все поля!')
            return
        print((self.token, self.resourse, self.work))
        try:
            print(2)
            await self.client.run(self.token)
            print(3)
        except LoginFailure as e:
            self.statusBar().showMessage('неверный токен')
            print('not done!')
            return
        except ValueError:
            self.statusBar().showMessage('Неправильно задан ID канала')
            await self.client.logout()
            return
        except SyntaxError:
            self.statusBar().showMessage('У вас нет роли доступа в экономику!')
            await self.client.logout()
            return
        except Exception as e:
            print(e)
            print(type(e))
            return

        print('done!')


class DSBotClient(Client):
    def __init__(self):
        super().__init__()

        self.counter = 0
        self.work = 'продаю'
        self.resourse = 'говно'
        self.channel_id = 663516107398840358
        self.end_channel_id = 709758881559085126
        self.flag = True
        self.channel = None
        self.end_channel = None

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.channel.id == self.channel_id:
            print('qq')
            if 'добываю'.lower() in message.content.lower() and self.resourse.lower() in message.content.lower():
                self.counter += 1


async def auto_message():
    ex.client.channel_id = ex.channel_id
    ex.client.counter = ex.counter
    ex.client.work = ex.work
    ex.client.resourse = ex.resourse
    ex.client.min_sleep = ex.min_sleep_time
    ex.client.max_sleep = ex.max_sleep_time
    print('m?')
    await asyncio.sleep(5)
    async for guild in ex.client.guilds:
        async for channel in guild.text_channels:
            if channel.id == ex.client.channel_id:
                ex.client.channel = channel
                if ex.client.channel is None:
                    raise ValueError
                if not ex.client.end_channel is None:
                    break
            elif channel.id == ex.client.end_channel_id:
                ex.client.end_channel = channel
                if ex.client.end_channel is None:
                    raise SyntaxError
                if not ex.client.channel is None:
                    break
    if ex.client.channel is None:
        raise ValueError
    if ex.client.end_channel is None:
        raise SyntaxError
    print('20 seconds left')
    await asyncio.sleep(1)
    while True:
        print('message sent', ex.client.counter)
        await ex.client.channel.send(f'{ex.client.work.capitalize()} {ex.client.resourse} {ex.client.counter}')
        time_asleep = random.randint(ex.client.min_sleep, ex.client.max_sleep)
        print(f'sleeping {time_asleep} seconds')
        await asyncio.sleep(time_asleep)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    ex = Game()
    ex.show()
    loop.run_forever()
