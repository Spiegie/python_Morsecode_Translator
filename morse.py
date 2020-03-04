# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morse.ui'
#
# Created: Mon Nov 23 17:59:37 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bsignal = QtGui.QPushButton(Dialog)
        self.Bsignal.setGeometry(QtCore.QRect(10, 280, 621, 191))
        self.Bsignal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bsignal.setObjectName(_fromUtf8("Bsignal"))
        self.Bclear = QtGui.QPushButton(Dialog)
        self.Bclear.setGeometry(QtCore.QRect(20, 250, 85, 27))
        self.Bclear.setObjectName(_fromUtf8("Bclear"))
        self.Btranslate = QtGui.QPushButton(Dialog)
        self.Btranslate.setGeometry(QtCore.QRect(110, 250, 85, 27))
        self.Btranslate.setObjectName(_fromUtf8("Btranslate"))
        self.Bsound = QtGui.QPushButton(Dialog)
        self.Bsound.setGeometry(QtCore.QRect(530, 250, 85, 27))
        self.Bsound.setObjectName(_fromUtf8("Bsound"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 621, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 249, 51, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 260, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(210, 245, 71, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(210, 270, 71, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.Bclear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Bsignal.setText(_translate("Dialog", "Signal", None))
        self.Bclear.setText(_translate("Dialog", "clear", None))
        self.Btranslate.setText(_translate("Dialog", "translate", None))
        self.Bsound.setText(_translate("Dialog", "Sound", None))
        self.pushButton.setText(_translate("Dialog", "toggle", None))
        self.label.setText(_translate("Dialog", "from Morse", None))

