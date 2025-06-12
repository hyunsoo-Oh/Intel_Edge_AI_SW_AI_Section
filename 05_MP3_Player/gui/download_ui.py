# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLineEdit, QListView, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"/* \uc804\uccb4 \uc708\ub3c4\uc6b0 \ubc0f \ubc30\uacbd */\n"
"QWidget {\n"
"    background-color: #121212;\n"
"    color: #FFFFFF;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* QPushButton (\uc7ac\uc0dd, \uc77c\uc2dc\uc815\uc9c0 \ub4f1) */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    padding: 8px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1DB954;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* QListWidget (\uc7ac\uc0dd\ubaa9\ub85d) */\n"
"QListWidget {\n"
"    background-color: #181818;\n"
"    border: none;\n"
"    padding: 8px;\n"
"}\n"
"QListWidget::item {\n"
"    padding: 10px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: #1DB954;\n"
"    color: black;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* QTableWidget (\uace1 \ubaa9\ub85d) */\n"
"QTableWidget {\n"
"    background-color: #181818;\n"
"    border: none;\n"
"    color: #FFFFFF;\n"
"    "
                        "gridline-color: #2a2a2a;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #282828;\n"
"    color: #B3B3B3;\n"
"    padding: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* QLineEdit (\uac80\uc0c9\ucc3d \ub4f1) */\n"
"QLineEdit {\n"
"    background-color: #282828;\n"
"    color: #FFFFFF;\n"
"    border: 1px solid #3E3E3E;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #1DB954;\n"
"}\n"
"\n"
"/* QSlider (\uc7ac\uc0dd \uc704\uce58, \uc74c\ub7c9 \uc870\uc808) */\n"
"QSlider::groove:horizontal {\n"
"    background: #404040;\n"
"    height: 4px;\n"
"    border-radius: 2px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: #1DB954;\n"
"    border: none;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 6px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background: #1DB954;\n"
"}\n"
"\n"
"/* QLabel (\ud0c0\uc774\ud2c0, \uc2dc\uac04 \ub4f1) */\n"
"QLabel {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* ScrollB"
                        "ar (\uc2a4\ud06c\ub864 \uc788\ub294 \uc704\uc82f\uc5d0 \ud544\uc694) */\n"
"QScrollBar:vertical {\n"
"    background: #181818;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #3E3E3E;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #1DB954;\n"
"}\n"
"\n"
"/* Hover \ud6a8\uacfc \uac15\uc870\uc6a9 \ud074\ub798\uc2a4\ub85c \ud65c\uc6a9 \uac00\ub2a5 */\n"
".play-hover:hover {\n"
"    background-color: #1DB954;\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchEdit = QLineEdit(Dialog)
        self.searchEdit.setObjectName(u"searchEdit")

        self.horizontalLayout.addWidget(self.searchEdit)

        self.searchBtn = QPushButton(Dialog)
        self.searchBtn.setObjectName(u"searchBtn")
        icon = QIcon()
        icon.addFile(u"../resources/icons/search_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.searchBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.searchBtn.setText("")
    # retranslateUi

