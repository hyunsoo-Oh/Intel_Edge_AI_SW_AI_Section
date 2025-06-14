# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recommend_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(840, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_banner = QtWidgets.QLabel(Dialog)
        self.lbl_banner.setObjectName("lbl_banner")
        self.verticalLayout.addWidget(self.lbl_banner)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_male = QtWidgets.QCheckBox(self.groupBox)
        self.check_male.setStyleSheet("margin-left: 20px;")
        self.check_male.setObjectName("check_male")
        self.verticalLayout_2.addWidget(self.check_male)
        self.check_female = QtWidgets.QCheckBox(self.groupBox)
        self.check_female.setStyleSheet("margin-left: 20px;")
        self.check_female.setObjectName("check_female")
        self.verticalLayout_2.addWidget(self.check_female)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.cb_skin = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_skin.setObjectName("cb_skin")
        self.cb_skin.addItem("")
        self.horizontalLayout_3.addWidget(self.cb_skin)
        self.cb_category = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_category.setObjectName("cb_category")
        self.cb_category.addItem("")
        self.horizontalLayout_3.addWidget(self.cb_category)
        self.line_cmd = QtWidgets.QLineEdit(self.groupBox_2)
        self.line_cmd.setObjectName("line_cmd")
        self.horizontalLayout_3.addWidget(self.line_cmd)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 2)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_table = QtWidgets.QListView(Dialog)
        self.list_table.setObjectName("list_table")
        self.horizontalLayout_2.addWidget(self.list_table)
        self.lbl_item = QtWidgets.QLabel(Dialog)
        self.lbl_item.setObjectName("lbl_item")
        self.horizontalLayout_2.addWidget(self.lbl_item)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 10)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_banner.setText(_translate("Dialog", "TextLabel"))
        self.groupBox.setTitle(_translate("Dialog", "성별"))
        self.check_male.setText(_translate("Dialog", "남성"))
        self.check_female.setText(_translate("Dialog", "여성"))
        self.cb_skin.setItemText(0, _translate("Dialog", "피부타입"))
        self.cb_category.setItemText(0, _translate("Dialog", "카테고리"))
        self.lbl_item.setText(_translate("Dialog", "TextLabel"))
