from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import winreg

class ProgressDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CLEANING")
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(30, 20, 340, 30)
        self.progressBar.setValue(0)

    def set_progress(self, value):
        self.progressBar.setValue(value)

class Ui_rx(object):
    def setupUi(self, rx):
        rx.setObjectName("rx")
        rx.resize(856, 481)
        rx.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.rx_2 = QtWidgets.QWidget(rx)
        self.rx_2.setObjectName("rx_2")
        self.frame = QtWidgets.QFrame(self.rx_2)
        self.frame.setGeometry(QtCore.QRect(0, 0, 861, 481))
        self.frame.setAutoFillBackground(True)
        self.frame.setVisible(True)
        self.frame.setStyleSheet("background-color:#1c2130")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.buttonframe = QtWidgets.QFrame(self.frame)
        self.buttonframe.setGeometry(QtCore.QRect(410, 25, 81, 41))
        self.buttonframe.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe.setObjectName("buttonframe")
        self.b1 = QtWidgets.QPushButton(self.buttonframe)
        self.b1.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b1.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.toggle_width)
        self.buttonframe_2 = QtWidgets.QFrame(self.frame)
        self.buttonframe_2.setGeometry(QtCore.QRect(410, 80, 81, 41))
        self.buttonframe_2.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_2.setObjectName("buttonframe_2")
        self.b5 = QtWidgets.QPushButton(self.buttonframe_2)
        self.b5.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b5.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.toggle_width2)
        self.buttonframe_3 = QtWidgets.QFrame(self.frame)
        self.buttonframe_3.setGeometry(QtCore.QRect(410, 135, 81, 41))
        self.buttonframe_3.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_3.setObjectName("buttonframe_3")
        self.b9 = QtWidgets.QPushButton(self.buttonframe_3)
        self.b9.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b9.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.b9.clicked.connect(self.toggle_width3)
        self.buttonframe_4 = QtWidgets.QFrame(self.frame)
        self.buttonframe_4.setGeometry(QtCore.QRect(410, 190, 81, 41))
        self.buttonframe_4.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_4.setObjectName("buttonframe_4")
        self.b10 = QtWidgets.QPushButton(self.buttonframe_4)
        self.b10.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b10.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b10.setText("")
        self.b10.setObjectName("b10")
        self.b10.clicked.connect(self.toggle_width4)
        self.buttonframe_5 = QtWidgets.QFrame(self.frame)
        self.buttonframe_5.setGeometry(QtCore.QRect(410, 245, 81, 41))
        self.buttonframe_5.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_5.setObjectName("buttonframe_5")
        self.b11 = QtWidgets.QPushButton(self.buttonframe_5)
        self.b11.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b11.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b11.setText("")
        self.b11.setObjectName("b11")
        self.b11.clicked.connect(self.toggle_width5)
        self.buttonframe_6 = QtWidgets.QFrame(self.frame)
        self.buttonframe_6.setGeometry(QtCore.QRect(410, 300, 81, 41))
        self.buttonframe_6.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_6.setObjectName("buttonframe_6")
        self.b12 = QtWidgets.QPushButton(self.buttonframe_6)
        self.b12.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b12.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b12.setText("")
        self.b12.setObjectName("b12")
        self.b12.clicked.connect(self.toggle_width6)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 35, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(210, 200, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(202, 250, 205, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(210, 310, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 181, 481))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.title = QtWidgets.QLabel(self.frame_8)
        self.title.setGeometry(QtCore.QRect(40, 20, 141, 141))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setMouseTracking(False)
        self.title.setAcceptDrops(False)
        self.title.setStyleSheet("QLabel{\n"
"color:rgb(0, 255, 255);\n"
"border: 20px solid rgba(8, 255, 201, 0.2); /* Simulated box shadow */\n"
"border-radius:70px;\n"
"background-color:rgb(8, 140, 180.2)\n"
"}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setVisible(False)
        self.pushButton_7.setAutoFillBackground(True)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color:black;\n"
"color:white;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(68, 71, 90);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_50.setGeometry(QtCore.QRect(50, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setAutoFillBackground(False)
        self.pushButton_50.setStyleSheet("QPushButton{\n"
"background-color:#0de5a8;\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color:white;\n"
"background-color:#14c3a2;\n"
"border-color:#14c3a2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-color:black;\n"
"border-width:1px;\n"
"}")
        
        
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_50.clicked.connect(self.POWERPLAN)
        self.pushButton_51 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_51.setGeometry(QtCore.QRect(50, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setAutoFillBackground(False)
        self.pushButton_51.setStyleSheet("QPushButton{\n"
"background-color:#00b4fc;\n"
"color:white;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #17f9ff;\n"
"}")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.clicked.connect(self.scan_registry)
        self.pushButton_51.clicked.connect(self.scan_registry2)
        self.pushButton_51.clicked.connect(self.scan_registry3)
        self.pushButton_51.clicked.connect(self.scan_registry4)
        self.pushButton_51.clicked.connect(self.scan_registry5)
        self.pushButton_51.clicked.connect(self.scan_registry6)
        self.pushButton_51.clicked.connect(self.scan_registry7)
        self.pushButton_51.clicked.connect(self.scan_registry8)
        self.pushButton_51.clicked.connect(self.scan_registry9)
        self.pushButton_51.clicked.connect(self.scan_registry10)
        self.pushButton_51.clicked.connect(self.scan_registry11)
        self.pushButton_51.clicked.connect(self.scan_registry12)
        self.pushButton_51.clicked.connect(self.scan_registry13)
        self.pushButton_51.clicked.connect(self.scan_registry14)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 420, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"background-color:rgba(255, 0, 0, 0.3);\n"
"color:white;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 0, 0)\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(rx.close)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(210, 370, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.buttonframe_7 = QtWidgets.QFrame(self.frame)
        self.buttonframe_7.setGeometry(QtCore.QRect(410, 360, 81, 41))
        self.buttonframe_7.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_7.setObjectName("buttonframe_7")
        self.b13 = QtWidgets.QPushButton(self.buttonframe_7)
        self.b13.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b13.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b13.setText("")
        self.b13.setObjectName("b13")
        self.b13.clicked.connect(self.toggle_width7)
        self.buttonframe_8 = QtWidgets.QFrame(self.frame)
        self.buttonframe_8.setGeometry(QtCore.QRect(410, 420, 81, 41))
        self.buttonframe_8.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_8.setObjectName("buttonframe_8")
        self.b14 = QtWidgets.QPushButton(self.buttonframe_8)
        self.b14.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b14.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b14.setText("")
        self.b14.setObjectName("b14")
        self.b14.clicked.connect(self.toggle_width8)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(210, 430, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.buttonframe_9 = QtWidgets.QFrame(self.frame)
        self.buttonframe_9.setGeometry(QtCore.QRect(750, 20, 81, 41))
        self.buttonframe_9.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_9.setObjectName("buttonframe_9")
        self.b15 = QtWidgets.QPushButton(self.buttonframe_9)
        self.b15.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b15.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b15.setText("")
        self.b15.setObjectName("b15")
        self.b15.clicked.connect(self.toggle_width9)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(550, 30, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.buttonframe_10 = QtWidgets.QFrame(self.frame)
        self.buttonframe_10.setGeometry(QtCore.QRect(750, 80, 81, 41))
        self.buttonframe_10.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_10.setObjectName("buttonframe_10")
        self.b2 = QtWidgets.QPushButton(self.buttonframe_10)
        self.b2.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b2.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.toggle_width10)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(550, 90, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.buttonframe_11 = QtWidgets.QFrame(self.frame)
        self.buttonframe_11.setGeometry(QtCore.QRect(750, 135, 81, 41))
        self.buttonframe_11.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_11.setObjectName("buttonframe_11")
        self.b3 = QtWidgets.QPushButton(self.buttonframe_11)
        self.b3.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b3.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.toggle_width11)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(550, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.buttonframe_12 = QtWidgets.QFrame(self.frame)
        self.buttonframe_12.setGeometry(QtCore.QRect(750, 190, 81, 41))
        self.buttonframe_12.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_12.setObjectName("buttonframe_12")
        self.b4 = QtWidgets.QPushButton(self.buttonframe_12)
        self.b4.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b4.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.toggle_width12)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(550, 200, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(550, 260, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.buttonframe_25 = QtWidgets.QFrame(self.frame)
        self.buttonframe_25.setGeometry(QtCore.QRect(750, 250, 81, 41))
        self.buttonframe_25.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_25.setObjectName("buttonframe_25")
        self.b6 = QtWidgets.QPushButton(self.buttonframe_25)
        self.b6.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b6.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.toggle_width13)
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setGeometry(QtCore.QRect(550, 320, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.buttonframe_26 = QtWidgets.QFrame(self.frame)
        self.buttonframe_26.setGeometry(QtCore.QRect(750, 310, 81, 41))
        self.buttonframe_26.setStyleSheet("QFrame{\n"
"background-color: rgb(40, 42, 54);\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_26.setObjectName("buttonframe_26")
        self.b7 = QtWidgets.QPushButton(self.buttonframe_26)
        self.b7.setGeometry(QtCore.QRect(5, 5, 33, 31))
        self.b7.setStyleSheet("QPushButton{\n"
"background-color:#6272A4;\n"
"border-radius :14.2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(135, 158, 227);\n"
"}")
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.toggle_width14)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(550, 380, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Vrinda")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet("QLabel{\n"
"color:rgb(193, 193, 193);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:rgb(98, 114, 164);\n"
"}")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.buttonframe_27 = QtWidgets.QFrame(self.frame)
        self.buttonframe_27.setGeometry(QtCore.QRect(750, 370, 81, 41))
        self.buttonframe_27.setStyleSheet("QFrame{\n"
"background-color: #0a837f;\n"
"border-radius:18px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"")
        self.buttonframe_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonframe_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonframe_27.setObjectName("buttonframe_27")
        self.b8 = QtWidgets.QPushButton(self.buttonframe_27)
        self.b8.setGeometry(QtCore.QRect(5, 5, 70, 31))
        self.b8.setStyleSheet("QPushButton{background-color:black; color:#0a837f; border-radius:14.2px;} QPushButton:hover{background-color:white; color:black}")
        self.b8.setText("CLEAN")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.b8.setObjectName("b8")
        self.b8.clicked.connect(self.cleaner)
        rx.setCentralWidget(self.rx_2)

        self.retranslateUi(rx)
        QtCore.QMetaObject.connectSlotsByName(rx)

    def retranslateUi(self, rx):
        _translate = QtCore.QCoreApplication.translate
        rx.setWindowTitle(_translate("rx", "RX PC TUNER"))
        self.label.setText(_translate("rx", "HIBERNATION"))
        self.label_2.setText(_translate("rx", "MAINTENANCE"))
        self.label_3.setText(_translate("rx", "PAGE COMBINING"))
        self.label_4.setText(_translate("rx", "⚡ESTIMATION"))
        self.label_5.setText(_translate("rx", "POWERTHROTTLING"))
        self.label_6.setText(_translate("rx", "RESPONSIVENESS"))
        self.title.setText(_translate("rx", "RX"))
        self.pushButton_7.setText(_translate("rx", "button1"))
        self.pushButton_50.setText(_translate("rx", "P.PLAN"))
        self.pushButton_51.setText(_translate("rx", "SCAN ✔"))
        self.pushButton_8.setText(_translate("rx", "CLOSE❌"))
        self.label_7.setText(_translate("rx", "WAKEUP ALL CORE"))
        self.label_8.setText(_translate("rx", "TELEMETRY"))
        self.label_9.setText(_translate("rx", "DISABLE_TSX"))
        self.label_10.setText(_translate("rx", "FEATURE ⚙ "))
        self.label_11.setText(_translate("rx", "INDEXING🔎"))
        self.label_12.setText(_translate("rx", "CORTANA"))
        self.label_25.setText(_translate("rx", "NOTIFICATION"))
        self.label_26.setText(_translate("rx", "H.P.E.T"))
        self.label_27.setText(_translate("rx", "MAKE YOUR PC>>>"))

        #toggle button

    def cleaner(self):
        dialog = ProgressDialog()
        dialog.show()

        commands = [
            "rd /s /q %temp%",
            "rd /s /q C:\\Windows\\Temp",
            "del /q /f /s C:\\Windows\\Prefetch\\*.*"
        ]
        total_steps = len(commands)
        current_step = 0

        def update_progress():
            nonlocal current_step
            current_step += 1
            progress = int(current_step / total_steps * 100)
            dialog.set_progress(progress)

        for command in commands:
            subprocess.run(command, shell=True)
            update_progress()
        dialog.close()

    def toggle_width14(self):
        if self.b7.width() == 33:
            self.b7.setFixedWidth(70)
            self.b7.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen('bcdedit /set disabledynamictick yes', shell=True, stdout=subprocess.PIPE)
        else:
            self.b7.setFixedWidth(33)
            self.b7.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen('bcdedit /set disabledynamictick no', shell=True, stdout=subprocess.PIPE)

    def toggle_width13(self):
        if self.b6.width() == 33:
            self.b6.setFixedWidth(70)
            self.b6.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"ToastEnabled\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"EnableLegacyBalloonNotifications\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoBalloonFeatureAdvertisements\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoSystraySystemPromotion\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoAutoTrayNotify\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"TaskbarNoNotification\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoTrayItemsDisplay\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"DisallowNotificationMirroring\" /t REG_SZ /d \"\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoCloudApplicationNotification\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoTileApplicationNotification\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoToastApplicationNotification\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoToastApplicationNotificationOnLockScreen\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System\" /v \"DisableLockScreenAppNotifications\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\Windows.SystemToast.StartupApp\" /v \"Enabled\" /t REG_DWORD /d \"0\" /f & ")
        else:
            self.b6.setFixedWidth(33)
            self.b6.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"ToastEnabled\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"EnableLegacyBalloonNotifications\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoBalloonFeatureAdvertisements\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoSystraySystemPromotion\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoAutoTrayNotify\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"TaskbarNoNotification\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v \"NoTrayItemsDisplay\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"DisallowNotificationMirroring\" /t REG_SZ /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoCloudApplicationNotification\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoTileApplicationNotification\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoToastApplicationNotification\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\CurrentVersion\\PushNotifications\" /v \"NoToastApplicationNotificationOnLockScreen\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System\" /v \"DisableLockScreenAppNotifications\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\Windows.SystemToast.StartupApp\" /v \"Enabled\" /t REG_DWORD /d \"1\" /f &")
 
    def toggle_width12(self):
        if self.b4.width() == 33:
            self.b4.setFixedWidth(70)
            self.b4.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowCortana\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"ConnectedSearchUseWebOverMeteredConnections\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowCloudSearch\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowSearchToUseLocation\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"ConnectedSearchUseWeb\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"DisableWebSearch\" /t REG_DWORD /d \"1\" /f  ")
        else:
            self.b4.setFixedWidth(33)
            self.b4.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowCortana\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"ConnectedSearchUseWebOverMeteredConnections\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowCloudSearch\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"AllowSearchToUseLocation\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"ConnectedSearchUseWeb\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search\" /v \"DisableWebSearch\" /t REG_DWORD /d \"0\" /f  ")
    def toggle_width11(self):
        if self.b3.width() == 33:
            self.b3.setFixedWidth(70)
            self.b3.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoRemoteDestinations\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer\" /v \"DisableSearchBoxSuggestions\" /t REG_DWORD /d \"1\" /f ")
        else:
            self.b3.setFixedWidth(33)
            self.b3.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer\" /v \"NoRemoteDestinations\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKCU\\SOFTWARE\\Policies\\Microsoft\\Windows\\Explorer\" /v \"DisableSearchBoxSuggestions\" /t REG_DWORD /d \"0\" /f ")

    def toggle_width10(self):
        if self.b2.width() == 33:
            self.b2.setFixedWidth(70)
            self.b2.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettings\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettingsOverride\" /t REG_DWORD /d \"3\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettingsOverrideMask\" /t REG_DWORD /d \"3\" /f ")
        else:
            self.b2.setFixedWidth(33)
            self.b2.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettings\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettingsOverride\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"FeatureSettingsOverrideMask\" /t REG_DWORD /d \"0\" /f ")

    def toggle_width9(self):
        if self.b15.width() == 33:
            self.b15.setFixedWidth(70)
            self.b15.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"DisableExceptionChainValidation\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"KernelSEHOPEnabled\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"DisableTsx\" /t REG_DWORD /d \"1\" /f")
        else:
            self.b15.setFixedWidth(33)
            self.b15.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"DisableExceptionChainValidation\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"KernelSEHOPEnabled\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\kernel\" /v \"DisableTsx\" /t REG_DWORD /d \"0\" /f")

    def toggle_width8(self):
        if self.b14.width() == 33:
            self.b14.setFixedWidth(70)
            self.b14.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d \"0\" /f ")
        else:
            self.b14.setFixedWidth(33)
            self.b14.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\" /v \"AllowTelemetry\" /t REG_DWORD /d \"1\" /f ")

    def toggle_width7(self):
        if self.b13.width() == 33:
            self.b13.setFixedWidth(70)
            self.b13.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\943c8cb6-6f93-4227-ad87-e9a3feec08d1\" /v \"Attributes\" /t REG_DWORD /d \"2\" /f ")
        else:
            self.b13.setFixedWidth(33)
            self.b13.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\943c8cb6-6f93-4227-ad87-e9a3feec08d1\" /v \"Attributes\" /t REG_DWORD /d \"1\" /f ")


    def toggle_width6(self):
        if self.b12.width() == 33:
            self.b12.setFixedWidth(70)
            self.b12.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\" /v \"SystemResponsiveness\" /t REG_DWORD /d \"0\" /f ")
        else:
            self.b12.setFixedWidth(33)
            self.b12.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\" /v \"SystemResponsiveness\" /t REG_DWORD /d \"10\" /f ")


    def toggle_width5(self):
        if self.b11.width() == 33:
            self.b11.setFixedWidth(70)
            self.b11.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling\" /v \"PowerThrottlingOff\" /t REG_DWORD /d \"1\" /f ")
        else:
            self.b11.setFixedWidth(33)
            self.b11.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling\" /v \"PowerThrottlingOff\" /t REG_DWORD /d \"0\" /f ")


    def toggle_width4(self):
        if self.b10.width() == 33:
           self.b10.setFixedWidth(70)
           self.b10.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
           subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\" /v \"EnergyEstimationEnabled\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"DisableTaggedEnergyLogging\" /t REG_DWORD /d \"1\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"TelemetryMaxApplication\" /t REG_DWORD /d \"0\" /f & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"TelemetryMaxTagPerApplication\" /t REG_DWORD /d \"0\" /f ")
        else:
            self.b10.setFixedWidth(33)
            self.b10.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\" /v \"EnergyEstimationEnabled\" /t REG_DWORD /d \"1\" /f  & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"DisableTaggedEnergyLogging\" /t REG_DWORD /d \"0\" /f  & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"TelemetryMaxApplication\" /t REG_DWORD /d \"250\" /f  & Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\EnergyEstimation\\TaggedEnergy\" /v \"TelemetryMaxTagPerApplication\" /t REG_DWORD /d \"50\" /f  ")
    def toggle_width3(self):

        if self.b9.width() == 33:
            self.b9.setFixedWidth(70)
            self.b9.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"DisablePageCombining\" /t REG_DWORD /d \"1\" /f ")
        else:
            self.b9.setFixedWidth(33)
            self.b9.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" /v \"DisablePageCombining\" /t REG_DWORD /d \"0\" /f ")

    def toggle_width2(self):

        if self.b5.width() == 33:
            self.b5.setFixedWidth(70)
            self.b5.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Schedule\\Maintenance\" /v \"MaintenanceDisabled\" /t REG_DWORD /d \"1\" /f ")
        else:
            self.b5.setFixedWidth(33)
            self.b5.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Schedule\\Maintenance\" /v \"MaintenanceDisabled\" /t REG_DWORD /d \"0\" /f ")

    def toggle_width(self):
        if self.b1.width() == 33:
            self.b1.setFixedWidth(70)
            self.b1.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\" /v \"HibernateEnabledDefault\" /t REG_DWORD /d \"0\" /f ")
        else:
            self.b1.setFixedWidth(33)
            self.b1.setStyleSheet("QPushButton{background-color:#6272A4; border-radius:14.2px}")
            subprocess.Popen("cmd /c Reg.exe add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\" /v \"HibernateEnabledDefault\" /t REG_DWORD /d \"1\" /f ")

    #scan button 
    

    def scan_registry14(self): #b7
            
       result = subprocess.run('bcdedit /enum', shell=True, stdout=subprocess.PIPE, text=True)
       lines = result.stdout.splitlines()
       is_disabled = False
       for line in lines:
             if 'disabledynamictick' in line:
                is_disabled = 'Yes' in line.split()[1]
                break
       if is_disabled:
            self.b7.setFixedWidth(70)
            self.b7.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b7.setFixedWidth(33)
            return
        



    def scan_registry13(self): #b6
       try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\PushNotifications")
            value, _ = winreg.QueryValueEx(key, "ToastEnabled")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b6.setFixedWidth(33)
            return
       if value == 0:
            self.b6.setFixedWidth(70)
            self.b6.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b6.setFixedWidth(33)

    def scan_registry12(self): #b4
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search")
            value, _ = winreg.QueryValueEx(key, "AllowCortana")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b4.setFixedWidth(33)
            return
       if value == 0:
            self.b4.setFixedWidth(70)
            self.b4.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b4.setFixedWidth(33)

    def scan_registry11(self): #b3
       try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Policies\Microsoft\Windows\Explorer")
            value, _ = winreg.QueryValueEx(key, "DisableSearchBoxSuggestions")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b3.setFixedWidth(33)
            return
       if value == 1:
            self.b3.setFixedWidth(70)
            self.b3.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b3.setFixedWidth(33)

    def scan_registry10(self): #b2
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management")
            value, _ = winreg.QueryValueEx(key, "FeatureSettingsOverride")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b2.setFixedWidth(33)
            return
       if value == 3:
            self.b2.setFixedWidth(70)
            self.b2.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b2.setFixedWidth(33)

    def scan_registry9(self): #b15
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel")
            value, _ = winreg.QueryValueEx(key, "DisableTsx")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b15.setFixedWidth(33)
            return
       if value == 1:
            self.b15.setFixedWidth(70)
            self.b15.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b15.setFixedWidth(33)

    def scan_registry8(self): #b14
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection")
            value, _ = winreg.QueryValueEx(key, "AllowTelemetry")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b14.setFixedWidth(33)
            return
       if value == 0:
            self.b14.setFixedWidth(70)
            self.b14.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b14.setFixedWidth(33)

    def scan_registry7(self): #b13
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\943c8cb6-6f93-4227-ad87-e9a3feec08d1")
            value, _ = winreg.QueryValueEx(key, "Attributes")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b13.setFixedWidth(33)
            return
       if value == 2:
            self.b13.setFixedWidth(70)
            self.b13.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

       else:
            self.b13.setFixedWidth(33)



    def scan_registry6(self): #b12
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile")
            value, _ = winreg.QueryValueEx(key, "SystemResponsiveness")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b12.setFixedWidth(33)
            return
       if value == 0:
            self.b12.setFixedWidth(70)
            self.b12.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
       else:
            self.b12.setFixedWidth(33)


    def scan_registry5(self): #b11
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling")
            value, _ = winreg.QueryValueEx(key, "PowerThrottlingOff")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b11.setFixedWidth(33)
            return
       if value == 1:
            self.b11.setFixedWidth(70)
            self.b11.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
       else:
            self.b11.setFixedWidth(33)

    def scan_registry4(self):  #b10
        try:
           key =winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power")
           value, _ =winreg.QueryValueEx(key, "EnergyEstimationEnabled")
           winreg.CloseKey(key)
        except FileNotFoundError:
            self.b10.setFixedWidth(33)
            return
        
        if value == 1:
            self.b10.setFixedWidth(33)
        else:
            self.b10.setFixedWidth(70)
            self.b10.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

    def scan_registry3(self):  #b9
        try:
           key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management")
           value, _ = winreg.QueryValueEx(key, "DisablePageCombining")
           winreg.CloseKey(key)
        except FileNotFoundError:
           self.b9.setFixedWidth(33)
           return

        if value == 1:
           self.b9.setFixedWidth(70)
           self.b9.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
        else:
           self.b9.setFixedWidth(33)
   
    def scan_registry2(self):  #b5
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance")
            value, _= winreg.QueryValueEx(key,"MaintenanceDisabled")
            winreg.CloseKey(key)
        except FileNotFoundError:
            self.b5.setFixedWidth(33)
            return
          
        if value == 1:
            self.b5.setFixedWidth(70)
            self.b5.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")
        else:
            self.b5.setFixedWidth(33)

    def scan_registry(self):  #b1
       try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Power")
            value, _ = winreg.QueryValueEx(key, "HibernateEnabledDefault")
            winreg.CloseKey(key)
       except FileNotFoundError:
            self.b1.setFixedWidth(33)
            return
       if value == 1:
            self.b1.setFixedWidth(33)
       else:
            self.b1.setFixedWidth(70)
            self.b1.setStyleSheet("QPushButton{background-color: #0de5a8; border-radius:14.2px}")

    def POWERPLAN(self):
             cmd = '''
@echo Off

powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61

exit
'''
             subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    rx = QtWidgets.QMainWindow()
    ui = Ui_rx()
    ui.setupUi(rx)
    rx.show()
    sys.exit(app.exec_())
