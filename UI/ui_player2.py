# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# 以下为designer设置的
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
                               QWidget)


# ui界面
class Ui_app(object):
    def setupUi(self, app):
        if not app.objectName():
            app.setObjectName(u"app")
        app.setEnabled(True)
        app.resize(1007, 554)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(app.sizePolicy().hasHeightForWidth())
        app.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(app)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(app)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"background-color: rgb(179, 208, 255);")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_upper = QFrame(self.tab_5)
        self.line_upper.setObjectName(u"line_upper")
        self.line_upper.setFrameShape(QFrame.HLine)
        self.line_upper.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_upper)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vedio_label1 = QLabel(self.tab_5)
        self.vedio_label1.setObjectName(u"vedio_label1")
        self.vedio_label1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.vedio_label1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.vedio_label1)

        self.line_mid = QFrame(self.tab_5)
        self.line_mid.setObjectName(u"line_mid")
        self.line_mid.setFrameShape(QFrame.VLine)
        self.line_mid.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_mid)

        self.vedio_label2 = QLabel(self.tab_5)
        self.vedio_label2.setObjectName(u"vedio_label2")
        self.vedio_label2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.vedio_label2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.vedio_label2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_above = QFrame(self.tab_5)
        self.line_above.setObjectName(u"line_above")
        self.line_above.setFrameShape(QFrame.HLine)
        self.line_above.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_above)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 500, -1)
        self.button1 = QPushButton(self.tab_5)
        self.button1.setObjectName(u"button1")
        self.button1.setEnabled(True)
        self.button1.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
                                   "font: 12pt \"Agency FB\";")

        self.horizontalLayout_6.addWidget(self.button1)

        self.button2 = QPushButton(self.tab_5)
        self.button2.setObjectName(u"button2")
        self.button2.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
                                   "font: 12pt \"Agency FB\";")

        self.horizontalLayout_6.addWidget(self.button2)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.add = QLabel(self.tab_5)
        self.add.setObjectName(u"add")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy1)
        self.add.setStyleSheet(u"background-color: rgb(255, 170, 127);\n"
                               "font: 12pt \"Agency FB\";")

        self.horizontalLayout_8.addWidget(self.add)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(app)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(app)

    # setupUi

    def retranslateUi(self, app):
        app.setWindowTitle(QCoreApplication.translate("app", u"\u667a\u80fd\u8def\u51b5\u8bc6\u522b\u7cfb\u7edf", None))
        self.vedio_label1.setText(QCoreApplication.translate("app", u"TextLabel", None))
        self.vedio_label2.setText(QCoreApplication.translate("app", u"TextLabel", None))
        self.button1.setText(QCoreApplication.translate("app", u"\u5f00\u59cb", None))
        self.button2.setText(QCoreApplication.translate("app", u"\u505c\u6b62", None))
        self.add.setText(QCoreApplication.translate("app", u"address\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  QCoreApplication.translate("app", u"\u667a\u80fd\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6),
                                  QCoreApplication.translate("app", u"\u63d0\u793a\u624b\u518c", None))

    # retranslateUi

    def set_text(self, text):
        self.add.setText('****' + text + '****')
