# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtui/mainwindow.ui'
#
# Created: Fri Aug  7 18:28:32 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1062, 728)
        self.main_widget = QtGui.QWidget(MainWindow)
        self.main_widget.setObjectName(_fromUtf8("main_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.h_layout_main = QtGui.QHBoxLayout()
        self.h_layout_main.setSpacing(0)
        self.h_layout_main.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.h_layout_main.setObjectName(_fromUtf8("h_layout_main"))
        self.tab_widget = QtGui.QTabWidget(self.main_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy)
        self.tab_widget.setTabPosition(QtGui.QTabWidget.North)
        self.tab_widget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.ElideRight)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.tab_files = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_files.sizePolicy().hasHeightForWidth())
        self.tab_files.setSizePolicy(sizePolicy)
        self.tab_files.setObjectName(_fromUtf8("tab_files"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_files)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.group_files = QtGui.QGroupBox(self.tab_files)
        self.group_files.setObjectName(_fromUtf8("group_files"))
        self.verticalLayout = QtGui.QVBoxLayout(self.group_files)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.table_files = FilesTableView(self.group_files)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_files.sizePolicy().hasHeightForWidth())
        self.table_files.setSizePolicy(sizePolicy)
        self.table_files.setDragDropMode(QtGui.QAbstractItemView.DropOnly)
        self.table_files.setAlternatingRowColors(True)
        self.table_files.setObjectName(_fromUtf8("table_files"))
        self.table_files.horizontalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.table_files)
        self.horizontalLayout.addWidget(self.group_files)
        self.v_layout_right = QtGui.QVBoxLayout()
        self.v_layout_right.setObjectName(_fromUtf8("v_layout_right"))
        self.groupBox = QtGui.QGroupBox(self.tab_files)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.btn_validate = QtGui.QPushButton(self.groupBox)
        self.btn_validate.setAutoDefault(False)
        self.btn_validate.setDefault(False)
        self.btn_validate.setFlat(False)
        self.btn_validate.setObjectName(_fromUtf8("btn_validate"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.btn_validate)
        self.btn_clear = QtGui.QPushButton(self.groupBox)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.btn_clear)
        self.v_layout_right.addWidget(self.groupBox)
        self.group_options = QtGui.QGroupBox(self.tab_files)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_options.sizePolicy().hasHeightForWidth())
        self.group_options.setSizePolicy(sizePolicy)
        self.group_options.setMinimumSize(QtCore.QSize(190, 200))
        self.group_options.setMaximumSize(QtCore.QSize(50, 16777215))
        self.group_options.setObjectName(_fromUtf8("group_options"))
        self.formLayout = QtGui.QFormLayout(self.group_options)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.check_best_practices = QtGui.QCheckBox(self.group_options)
        self.check_best_practices.setObjectName(_fromUtf8("check_best_practices"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.check_best_practices)
        self.check_profile = QtGui.QCheckBox(self.group_options)
        self.check_profile.setObjectName(_fromUtf8("check_profile"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.check_profile)
        self.v_layout_right.addWidget(self.group_options)
        self.horizontalLayout.addLayout(self.v_layout_right)
        self.tab_widget.addTab(self.tab_files, _fromUtf8(""))
        self.tab_remove = QtGui.QWidget()
        self.tab_remove.setEnabled(False)
        self.tab_remove.setObjectName(_fromUtf8("tab_remove"))
        self.tab_widget.addTab(self.tab_remove, _fromUtf8(""))
        self.h_layout_main.addWidget(self.tab_widget)
        self.verticalLayout_2.addLayout(self.h_layout_main)
        MainWindow.setCentralWidget(self.main_widget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_stix_validator = QtGui.QMenu(self.menubar)
        self.menu_stix_validator.setObjectName(_fromUtf8("menu_stix_validator"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_options = QtGui.QMenu(self.menubar)
        self.menu_options.setObjectName(_fromUtf8("menu_options"))
        self.menu_xml_schema = QtGui.QMenu(self.menu_options)
        self.menu_xml_schema.setObjectName(_fromUtf8("menu_xml_schema"))
        self.menu_stix_profile = QtGui.QMenu(self.menu_options)
        self.menu_stix_profile.setObjectName(_fromUtf8("menu_stix_profile"))
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtGui.QStatusBar(MainWindow)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        MainWindow.setStatusBar(self.status_bar)
        self.action_add_file = QtGui.QAction(MainWindow)
        self.action_add_file.setObjectName(_fromUtf8("action_add_file"))
        self.action_add_directory = QtGui.QAction(MainWindow)
        self.action_add_directory.setObjectName(_fromUtf8("action_add_directory"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_set_schema_dir = QtGui.QAction(MainWindow)
        self.action_set_schema_dir.setObjectName(_fromUtf8("action_set_schema_dir"))
        self.actionEnable = QtGui.QAction(MainWindow)
        self.actionEnable.setObjectName(_fromUtf8("actionEnable"))
        self.action_set_stix_profile = QtGui.QAction(MainWindow)
        self.action_set_stix_profile.setObjectName(_fromUtf8("action_set_stix_profile"))
        self.action_enable_all_profile = QtGui.QAction(MainWindow)
        self.action_enable_all_profile.setObjectName(_fromUtf8("action_enable_all_profile"))
        self.action_disable_all_profile = QtGui.QAction(MainWindow)
        self.action_disable_all_profile.setObjectName(_fromUtf8("action_disable_all_profile"))
        self.action_enable_all_best_practice = QtGui.QAction(MainWindow)
        self.action_enable_all_best_practice.setObjectName(_fromUtf8("action_enable_all_best_practice"))
        self.action_disable_all_best_practice = QtGui.QAction(MainWindow)
        self.action_disable_all_best_practice.setObjectName(_fromUtf8("action_disable_all_best_practice"))
        self.menu_help.addAction(self.action_about)
        self.menu_file.addAction(self.action_add_file)
        self.menu_xml_schema.addAction(self.action_set_schema_dir)
        self.menu_stix_profile.addAction(self.action_set_stix_profile)
        self.menu_options.addAction(self.menu_xml_schema.menuAction())
        self.menu_options.addAction(self.menu_stix_profile.menuAction())
        self.menubar.addAction(self.menu_stix_validator.menuAction())
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "STIX Document Validator", None))
        self.group_files.setTitle(_translate("MainWindow", "Validate Files", None))
        self.groupBox.setTitle(_translate("MainWindow", "Actions", None))
        self.btn_validate.setText(_translate("MainWindow", "Validate", None))
        self.btn_clear.setText(_translate("MainWindow", "Clear Files", None))
        self.group_options.setTitle(_translate("MainWindow", "Options", None))
        self.check_best_practices.setText(_translate("MainWindow", "Validate Best Practices", None))
        self.check_profile.setText(_translate("MainWindow", "Valdiate STIX Profile", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_files), _translate("MainWindow", "Documents", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_remove), _translate("MainWindow", "Tab 2", None))
        self.menu_stix_validator.setTitle(_translate("MainWindow", "STIX Validator", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_options.setTitle(_translate("MainWindow", "Options", None))
        self.menu_xml_schema.setTitle(_translate("MainWindow", "XML Schema", None))
        self.menu_stix_profile.setTitle(_translate("MainWindow", "STIX Profile", None))
        self.action_add_file.setText(_translate("MainWindow", "Add Files...", None))
        self.action_add_file.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_add_directory.setText(_translate("MainWindow", "Add Directory...", None))
        self.action_about.setText(_translate("MainWindow", "About...", None))
        self.action_set_schema_dir.setText(_translate("MainWindow", "Set Schema Diectory", None))
        self.actionEnable.setText(_translate("MainWindow", "Enable", None))
        self.action_set_stix_profile.setText(_translate("MainWindow", "Set STIX Profile", None))
        self.action_enable_all_profile.setText(_translate("MainWindow", "Enable All", None))
        self.action_disable_all_profile.setText(_translate("MainWindow", "Disable All", None))
        self.action_enable_all_best_practice.setText(_translate("MainWindow", "Enable All", None))
        self.action_disable_all_best_practice.setText(_translate("MainWindow", "Disable All", None))

from cutiestix.widgets import FilesTableView
