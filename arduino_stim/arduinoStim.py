# Form implementation generated from reading ui file '.\qt\arduinoStim.ui'
#
# Created: Wed Oct 22 12:41:56 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ArduinoStimControl(object):
    def setupUi(self, ArduinoStimControl):
        ArduinoStimControl.setObjectName("ArduinoStimControl")
        ArduinoStimControl.resize(534, 354)
        self.gridLayout_2 = QtGui.QGridLayout(ArduinoStimControl)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.parametersLayout = QtGui.QFormLayout()
        self.parametersLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.parametersLayout.setObjectName("parametersLayout")
        self.maxCurrentMADoubleSpinBox = QtGui.QDoubleSpinBox(ArduinoStimControl)
        self.maxCurrentMADoubleSpinBox.setMaximum(20.0)
        self.maxCurrentMADoubleSpinBox.setSingleStep(0.1)
        self.maxCurrentMADoubleSpinBox.setProperty("value", 2.0)
        self.maxCurrentMADoubleSpinBox.setObjectName("maxCurrentMADoubleSpinBox")
        self.parametersLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.maxCurrentMADoubleSpinBox)
        self.scalingLabel = QtGui.QLabel(ArduinoStimControl)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.scalingLabel.setFont(font)
        self.scalingLabel.setObjectName("scalingLabel")
        self.parametersLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.scalingLabel)
        self.scalingDoubleSpinBox = QtGui.QDoubleSpinBox(ArduinoStimControl)
        self.scalingDoubleSpinBox.setMaximum(10.0)
        self.scalingDoubleSpinBox.setSingleStep(0.1)
        self.scalingDoubleSpinBox.setProperty("value", 1.0)
        self.scalingDoubleSpinBox.setObjectName("scalingDoubleSpinBox")
        self.parametersLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.scalingDoubleSpinBox)
        self.maxCurrentMALabel = QtGui.QLabel(ArduinoStimControl)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.maxCurrentMALabel.setFont(font)
        self.maxCurrentMALabel.setObjectName("maxCurrentMALabel")
        self.parametersLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.maxCurrentMALabel)
        self.gridLayout_2.addLayout(self.parametersLayout, 1, 0, 1, 1)
        self.currentLayout = QtGui.QFormLayout()
        self.currentLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.currentLayout.setObjectName("currentLayout")
        self.targetDoubleSpinBox = QtGui.QDoubleSpinBox(ArduinoStimControl)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.targetDoubleSpinBox.setFont(font)
        self.targetDoubleSpinBox.setAccelerated(True)
        self.targetDoubleSpinBox.setMinimum(-20.0)
        self.targetDoubleSpinBox.setMaximum(20.0)
        self.targetDoubleSpinBox.setSingleStep(0.01)
        self.targetDoubleSpinBox.setObjectName("targetDoubleSpinBox")
        self.currentLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.targetDoubleSpinBox)
        self.targetLabel = QtGui.QLabel(ArduinoStimControl)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.targetLabel.setFont(font)
        self.targetLabel.setObjectName("targetLabel")
        self.currentLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.targetLabel)
        self.gridLayout_2.addLayout(self.currentLayout, 0, 0, 1, 2)
        self.rtInfoLayout = QtGui.QFormLayout()
        self.rtInfoLayout.setObjectName("rtInfoLayout")
        self.currentLabel = QtGui.QLabel(ArduinoStimControl)
        self.currentLabel.setObjectName("currentLabel")
        self.rtInfoLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.currentLabel)
        self.currentLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.currentLineEdit.setEnabled(False)
        self.currentLineEdit.setText("")
        self.currentLineEdit.setReadOnly(True)
        self.currentLineEdit.setObjectName("currentLineEdit")
        self.rtInfoLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.currentLineEdit)
        self.limitLabel = QtGui.QLabel(ArduinoStimControl)
        self.limitLabel.setObjectName("limitLabel")
        self.rtInfoLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.limitLabel)
        self.limitLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.limitLineEdit.setEnabled(False)
        self.limitLineEdit.setReadOnly(True)
        self.limitLineEdit.setObjectName("limitLineEdit")
        self.rtInfoLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.limitLineEdit)
        self.voltageLabel = QtGui.QLabel(ArduinoStimControl)
        self.voltageLabel.setObjectName("voltageLabel")
        self.rtInfoLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.voltageLabel)
        self.voltageLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.voltageLineEdit.setEnabled(False)
        self.voltageLineEdit.setReadOnly(True)
        self.voltageLineEdit.setObjectName("voltageLineEdit")
        self.rtInfoLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.voltageLineEdit)
        self.tapValueLabel = QtGui.QLabel(ArduinoStimControl)
        self.tapValueLabel.setObjectName("tapValueLabel")
        self.rtInfoLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.tapValueLabel)
        self.tapValueLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.tapValueLineEdit.setEnabled(False)
        self.tapValueLineEdit.setReadOnly(True)
        self.tapValueLineEdit.setObjectName("tapValueLineEdit")
        self.rtInfoLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.tapValueLineEdit)
        self.actualTargetLabel = QtGui.QLabel(ArduinoStimControl)
        self.actualTargetLabel.setObjectName("actualTargetLabel")
        self.rtInfoLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.actualTargetLabel)
        self.actualTargetLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.actualTargetLineEdit.setEnabled(False)
        self.actualTargetLineEdit.setReadOnly(True)
        self.actualTargetLineEdit.setObjectName("actualTargetLineEdit")
        self.rtInfoLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.actualTargetLineEdit)
        self.actualMaxLabel = QtGui.QLabel(ArduinoStimControl)
        self.actualMaxLabel.setObjectName("actualMaxLabel")
        self.rtInfoLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.actualMaxLabel)
        self.actualMaxLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.actualMaxLineEdit.setEnabled(False)
        self.actualMaxLineEdit.setReadOnly(True)
        self.actualMaxLineEdit.setObjectName("actualMaxLineEdit")
        self.rtInfoLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.actualMaxLineEdit)
        self.actualScalingLabel = QtGui.QLabel(ArduinoStimControl)
        self.actualScalingLabel.setObjectName("actualScalingLabel")
        self.rtInfoLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.actualScalingLabel)
        self.actualScalingLineEdit = QtGui.QLineEdit(ArduinoStimControl)
        self.actualScalingLineEdit.setEnabled(False)
        self.actualScalingLineEdit.setReadOnly(True)
        self.actualScalingLineEdit.setObjectName("actualScalingLineEdit")
        self.rtInfoLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.actualScalingLineEdit)
        self.gridLayout_2.addLayout(self.rtInfoLayout, 0, 2, 2, 1)
        self.comPort = QtGui.QComboBox(ArduinoStimControl)
        self.comPort.setObjectName("comPort")
        self.gridLayout_2.addWidget(self.comPort, 2, 0, 1, 2)
        self.stopButton = QtGui.QPushButton(ArduinoStimControl)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("QPushButton  {\n"
"    background: red;\n"
"    color: white;\n"
"}")
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 1, 1, 1, 1)

        self.retranslateUi(ArduinoStimControl)
        QtCore.QMetaObject.connectSlotsByName(ArduinoStimControl)

    def retranslateUi(self, ArduinoStimControl):
        ArduinoStimControl.setWindowTitle(QtGui.QApplication.translate("ArduinoStimControl", "Control you Arduino tDCS device", None, QtGui.QApplication.UnicodeUTF8))
        self.scalingLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Scaling", None, QtGui.QApplication.UnicodeUTF8))
        self.maxCurrentMALabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Max Current (mA)", None, QtGui.QApplication.UnicodeUTF8))
        self.targetLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Target", None, QtGui.QApplication.UnicodeUTF8))
        self.currentLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.currentLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.limitLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.limitLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.voltageLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.voltageLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.tapValueLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Tap value", None, QtGui.QApplication.UnicodeUTF8))
        self.tapValueLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.actualTargetLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Actual Target", None, QtGui.QApplication.UnicodeUTF8))
        self.actualTargetLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.actualMaxLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Actual Max", None, QtGui.QApplication.UnicodeUTF8))
        self.actualMaxLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.actualScalingLabel.setText(QtGui.QApplication.translate("ArduinoStimControl", "Actual Scaling", None, QtGui.QApplication.UnicodeUTF8))
        self.actualScalingLineEdit.setPlaceholderText(QtGui.QApplication.translate("ArduinoStimControl", "Device not started", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("ArduinoStimControl", "Stop", None, QtGui.QApplication.UnicodeUTF8))

