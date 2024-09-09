# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_platform_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(692, 584)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 250, 521, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.description_setting = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.description_setting.setContentsMargins(0, 0, 0, 0)
        self.description_setting.setObjectName("description_setting")
        self.Description = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Description.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Description.setAutoFillBackground(False)
        self.Description.setOpenExternalLinks(False)
        self.Description.setObjectName("Description")
        self.description_setting.addWidget(self.Description)
        self.inhalt = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.inhalt.setObjectName("inhalt")
        self.description_setting.addWidget(self.inhalt)
        self.description_btn_setting = QtWidgets.QHBoxLayout()
        self.description_btn_setting.setObjectName("description_btn_setting")
        self.clear_inhalt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_inhalt.setObjectName("clear_inhalt")
        self.description_btn_setting.addWidget(self.clear_inhalt)
        self.save_inhalt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_inhalt.setObjectName("save_inhalt")
        self.description_btn_setting.addWidget(self.save_inhalt)
        self.description_setting.addLayout(self.description_btn_setting)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 130, 521, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.file_upload_setting = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.file_upload_setting.setContentsMargins(0, 0, 0, 0)
        self.file_upload_setting.setObjectName("file_upload_setting")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.include_onnx_file = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.include_onnx_file.setObjectName("include_onnx_file")
        self.verticalLayout.addWidget(self.include_onnx_file)
        self.target_folder = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_folder.sizePolicy().hasHeightForWidth())
        self.target_folder.setSizePolicy(sizePolicy)
        self.target_folder.setObjectName("target_folder")
        self.verticalLayout.addWidget(self.target_folder)
        self.file_select = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.file_select.setObjectName("file_select")
        self.verticalLayout.addWidget(self.file_select)
        self.file_upload_setting.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 30, 521, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.ssh_setting = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.ssh_setting.setContentsMargins(0, 0, 0, 0)
        self.ssh_setting.setObjectName("ssh_setting")
        self.ssh_username = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ssh_username.setObjectName("ssh_username")
        self.ssh_setting.addWidget(self.ssh_username)
        self.ssh_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.ssh_password.setObjectName("ssh_password")
        self.ssh_setting.addWidget(self.ssh_password)
        self.ssh_connect_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ssh_connect_btn.setObjectName("ssh_connect_btn")
        self.ssh_setting.addWidget(self.ssh_connect_btn)
        self.file_upload_btn = QtWidgets.QPushButton(Form)
        self.file_upload_btn.setGeometry(QtCore.QRect(80, 540, 521, 26))
        self.file_upload_btn.setObjectName("file_upload_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Description.setText(_translate("Form", "                       Description"))
        self.clear_inhalt.setText(_translate("Form", "清空"))
        self.save_inhalt.setText(_translate("Form", "保存"))
        self.include_onnx_file.setText(_translate("Form", "ONNX文件"))
        self.file_select.setText(_translate("Form", "选择文件"))
        self.ssh_connect_btn.setText(_translate("Form", "连接"))
        self.file_upload_btn.setText(_translate("Form", "上传"))
