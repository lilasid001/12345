import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
app = QtWidgets.QApplication([])

u1 = uic.loadUi("PODSVETKA_DESIGN.ui")
u1.setWindowTitle("ASID")
#brS = u1.bS.value()

serial = QSerialPort()
serial.setBaudRate(115200)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
u1.comL.addItems(portList)  #показ портов в списке


def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
     #   txs += ','
    #txs = txs[:-1]
   # txs += ';'
    serial.write(txs.encode())

def pOpen ():
 serial.setPortName(u1.comL.currentText())
 serial.open(QIODevice.ReadWrite)

def pClose ():
 serial.close()

def task1 ():
 serialSend(['A'])
 serialSend([0])

def task2 ():
 serialSend(['A'])
 serialSend([1])

def task3 (val):
 serialSend(['A'])
 serialSend([2])

def task4 (val):
 serialSend(['A'])
 serialSend([3])

def task5 ():
 serialSend(['A'])
 serialSend([4])

def task6 ():
 serialSend(['A'])
 serialSend([5])

def task7 ():
 serialSend(['A'])
 serialSend([6])

def task8 ():
 serialSend(['A'])
 serialSend([7])

def task21 ():
 serialSend(['B'])
 serialSend([chr(0)])

def task22 ():
 serialSend(['B'])
 serialSend([chr(25)])

def task23 (val):
 serialSend(['B'])
 serialSend([chr(50)])

def task24 (val):
 serialSend(['B'])
 serialSend([chr(100)])

def task25 ():
 serialSend(['B'])
 serialSend([chr(75)])


def OnOffBright (val):
 brS = u1.bS.value()
 if val == 2: val = brS;
 if val == 0: val = 0;
 serialSend(['B'])
 serialSend([chr(val)])

#def brightControl ():
#brS = u1.bS.value()
#serialSend(['B'])
#serialSend([chr(u1.bS.value())])

u1.openB.clicked.connect(pOpen) #кнопка открытия порта
u1.closeB.clicked.connect(pClose) #кнопка закрытия порта
u1.c1B.clicked.connect(task1) #кнопка первого режима
u1.c2B.clicked.connect(task2) #кнопка второго режима
u1.c3B.clicked.connect(task3) #кнопка третьего режима
u1.c4B.clicked.connect(task4) #кнопка четвертого режима
u1.c5B.clicked.connect(task5) #кнопка пятого режима
u1.c6B.clicked.connect(task6) #кнопка шестого режима
u1.c7B.clicked.connect(task7) #кнопка седьмого режима
u1.c8B.clicked.connect(task8) #кнопка восьмого режима

u1.onOffBox.stateChanged.connect(OnOffBright) #чекбокс яркости 0/100

u1.c1B_3.clicked.connect(task21) #кнопка 0%
u1.c1B_4.clicked.connect(task22) #кнопка 25%
u1.c1B_5.clicked.connect(task23) #кнопка 50%
u1.c1B_6.clicked.connect(task24) #кнопка 75%
u1.c1B_7.clicked.connect(task25) #кнопка 100%

#u1.bS.valueChanged.connect(brightControl) #слайдер яркости
#u1.bS.setValue(100)

u1.show()
app.exec()