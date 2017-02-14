# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wire_home_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_wire_home_display(object):
    def setupUi(self, wire_home_display):
        wire_home_display.setObjectName(_fromUtf8("wire_home_display"))
        wire_home_display.resize(301, 431)
        self.wire_text_browser = QtGui.QTextBrowser(wire_home_display)
        self.wire_text_browser.setGeometry(QtCore.QRect(0, 0, 301, 431))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wire_text_browser.sizePolicy().hasHeightForWidth())
        self.wire_text_browser.setSizePolicy(sizePolicy)
        self.wire_text_browser.setObjectName(_fromUtf8("wire_text_browser"))
        self.wire_home_message = QtGui.QLineEdit(wire_home_display)
        self.wire_home_message.setGeometry(QtCore.QRect(10, 10, 281, 27))
        self.wire_home_message.setAutoFillBackground(False)
        self.wire_home_message.setObjectName(_fromUtf8("wire_home_message"))

        self.retranslateUi(wire_home_display)
        QtCore.QMetaObject.connectSlotsByName(wire_home_display)

    def retranslateUi(self, wire_home_display):
        wire_home_display.setWindowTitle(_translate("wire_home_display", "Wire: Home", None))
        self.wire_text_browser.setHtml(_translate("wire_home_display", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.wire_home_message.setPlaceholderText(_translate("wire_home_display", " message...", None))

