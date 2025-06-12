# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mp3_player_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 480)
        Form.setStyleSheet(u"/* \uc804\uccb4 \uc708\ub3c4\uc6b0 \ubc0f \ubc30\uacbd */\n"
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
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.sidebarLayout = QVBoxLayout()
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.searchBox = QGroupBox(Form)
        self.searchBox.setObjectName(u"searchBox")
        self.verticalLayout = QVBoxLayout(self.searchBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.downloadBtn = QPushButton(self.searchBox)
        self.downloadBtn.setObjectName(u"downloadBtn")

        self.verticalLayout.addWidget(self.downloadBtn)

        self.downloadListBtn = QPushButton(self.searchBox)
        self.downloadListBtn.setObjectName(u"downloadListBtn")

        self.verticalLayout.addWidget(self.downloadListBtn)


        self.sidebarLayout.addWidget(self.searchBox)

        self.playlistBox = QGroupBox(Form)
        self.playlistBox.setObjectName(u"playlistBox")
        self.playlistBox.setLayoutDirection(Qt.RightToLeft)
        self.playlistBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.verticalLayout_6 = QVBoxLayout(self.playlistBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.addMusicBtn = QPushButton(self.playlistBox)
        self.addMusicBtn.setObjectName(u"addMusicBtn")

        self.verticalLayout_6.addWidget(self.addMusicBtn)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.sidebarLayout.addWidget(self.playlistBox)


        self.mainLayout.addLayout(self.sidebarLayout)

        self.songInfoLayout = QVBoxLayout()
        self.songInfoLayout.setObjectName(u"songInfoLayout")
        self.songTitleLabel = QLabel(Form)
        self.songTitleLabel.setObjectName(u"songTitleLabel")

        self.songInfoLayout.addWidget(self.songTitleLabel)

        self.artistLabel = QLabel(Form)
        self.artistLabel.setObjectName(u"artistLabel")

        self.songInfoLayout.addWidget(self.artistLabel)


        self.mainLayout.addLayout(self.songInfoLayout)

        self.playBox = QGroupBox(Form)
        self.playBox.setObjectName(u"playBox")
        self.horizontalLayout_2 = QHBoxLayout(self.playBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.musicList = QListWidget(self.playBox)
        self.musicList.setObjectName(u"musicList")

        self.horizontalLayout_2.addWidget(self.musicList)


        self.mainLayout.addWidget(self.playBox)

        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 5)
        self.mainLayout.setStretch(2, 8)

        self.verticalLayout_5.addLayout(self.mainLayout)

        self.activityLayout = QGroupBox(Form)
        self.activityLayout.setObjectName(u"activityLayout")
        self.horizontalLayout = QHBoxLayout(self.activityLayout)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.nowPlayLayout = QVBoxLayout()
        self.nowPlayLayout.setObjectName(u"nowPlayLayout")
        self.nowTitleLabel = QLabel(self.activityLayout)
        self.nowTitleLabel.setObjectName(u"nowTitleLabel")

        self.nowPlayLayout.addWidget(self.nowTitleLabel)

        self.nowArtistLabel = QLabel(self.activityLayout)
        self.nowArtistLabel.setObjectName(u"nowArtistLabel")

        self.nowPlayLayout.addWidget(self.nowArtistLabel)


        self.horizontalLayout.addLayout(self.nowPlayLayout)

        self.playerControl = QVBoxLayout()
        self.playerControl.setObjectName(u"playerControl")
        self.playControlBar = QHBoxLayout()
        self.playControlBar.setObjectName(u"playControlBar")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.playControlBar.addItem(self.horizontalSpacer)

        self.prevBtn = QPushButton(self.activityLayout)
        self.prevBtn.setObjectName(u"prevBtn")
        self.prevBtn.setMaximumSize(QSize(40, 16777215))
        icon = QIcon()
        icon.addFile(u"../resources/icons/prev_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevBtn.setIcon(icon)

        self.playControlBar.addWidget(self.prevBtn)

        self.playBtn = QPushButton(self.activityLayout)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setMaximumSize(QSize(40, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"../resources/icons/play_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u"../resources/icons/pause_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.playBtn.setIcon(icon1)

        self.playControlBar.addWidget(self.playBtn)

        self.nextBtn = QPushButton(self.activityLayout)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setMaximumSize(QSize(40, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"../resources/icons/next_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextBtn.setIcon(icon2)

        self.playControlBar.addWidget(self.nextBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.playControlBar.addItem(self.horizontalSpacer_2)


        self.playerControl.addLayout(self.playControlBar)

        self.playTimeBar = QHBoxLayout()
        self.playTimeBar.setObjectName(u"playTimeBar")
        self.playTimeView = QLabel(self.activityLayout)
        self.playTimeView.setObjectName(u"playTimeView")
        self.playTimeView.setAlignment(Qt.AlignCenter)

        self.playTimeBar.addWidget(self.playTimeView)

        self.playTimeSlider = QSlider(self.activityLayout)
        self.playTimeSlider.setObjectName(u"playTimeSlider")
        self.playTimeSlider.setOrientation(Qt.Horizontal)

        self.playTimeBar.addWidget(self.playTimeSlider)

        self.space = QLabel(self.activityLayout)
        self.space.setObjectName(u"space")

        self.playTimeBar.addWidget(self.space)

        self.playTimeBar.setStretch(0, 1)
        self.playTimeBar.setStretch(1, 5)
        self.playTimeBar.setStretch(2, 1)

        self.playerControl.addLayout(self.playTimeBar)


        self.horizontalLayout.addLayout(self.playerControl)

        self.controlLayout = QHBoxLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.PlaybackBtn = QPushButton(self.activityLayout)
        self.PlaybackBtn.setObjectName(u"PlaybackBtn")
        icon3 = QIcon()
        icon3.addFile(u"../resources/icons/loop_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u"../resources/icons/single_vector_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.PlaybackBtn.setIcon(icon3)

        self.controlLayout.addWidget(self.PlaybackBtn)

        self.label = QLabel(self.activityLayout)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"../resources/icons/volume_icon.svg"))

        self.controlLayout.addWidget(self.label)

        self.volumeSlider = QSlider(self.activityLayout)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.controlLayout.addWidget(self.volumeSlider)

        self.controlLayout.setStretch(2, 3)

        self.horizontalLayout.addLayout(self.controlLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout_5.addWidget(self.activityLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.searchBox.setTitle("")
        self.downloadBtn.setText(QCoreApplication.translate("Form", u"Download", None))
        self.downloadListBtn.setText(QCoreApplication.translate("Form", u"List", None))
        self.playlistBox.setTitle(QCoreApplication.translate("Form", u"Play List", None))
        self.addMusicBtn.setText(QCoreApplication.translate("Form", u"Add Player", None))
        self.songTitleLabel.setText("")
        self.artistLabel.setText("")
        self.playBox.setTitle(QCoreApplication.translate("Form", u"Play List", None))
        self.activityLayout.setTitle("")
        self.nowTitleLabel.setText(QCoreApplication.translate("Form", u"Title", None))
        self.nowArtistLabel.setText(QCoreApplication.translate("Form", u"Artist", None))
        self.prevBtn.setText("")
        self.playBtn.setText("")
        self.nextBtn.setText("")
        self.playTimeView.setText(QCoreApplication.translate("Form", u"0:00/0:00", None))
        self.space.setText("")
        self.PlaybackBtn.setText("")
        self.label.setText("")
    # retranslateUi

