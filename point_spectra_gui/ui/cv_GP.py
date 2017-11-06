# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setTitle("")
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.reductionMethodLabel = QtWidgets.QLabel(self.formGroupBox)
        self.reductionMethodLabel.setObjectName("reductionMethodLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.reductionMethodLabel)
        self.DimRedList = QtWidgets.QListWidget(self.formGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DimRedList.sizePolicy().hasHeightForWidth())
        self.DimRedList.setSizePolicy(sizePolicy)
        self.DimRedList.setMinimumSize(QtCore.QSize(0, 0))
        self.DimRedList.setMaximumSize(QtCore.QSize(16777215, 50))
        self.DimRedList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.DimRedList.setObjectName("DimRedList")
        item = QtWidgets.QListWidgetItem()
        self.DimRedList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.DimRedList.addItem(item)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DimRedList)
        self.numOfComponenetsLabel = QtWidgets.QLabel(self.formGroupBox)
        self.numOfComponenetsLabel.setObjectName("numOfComponenetsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.numOfComponenetsLabel)
        self.numOfComponenetsLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.numOfComponenetsLineEdit.setObjectName("numOfComponenetsLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.numOfComponenetsLineEdit)
        self.regrLabel = QtWidgets.QLabel(self.formGroupBox)
        self.regrLabel.setObjectName("regrLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.regrLabel)
        self.regression_list = QtWidgets.QListWidget(self.formGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regression_list.sizePolicy().hasHeightForWidth())
        self.regression_list.setSizePolicy(sizePolicy)
        self.regression_list.setMaximumSize(QtCore.QSize(16777215, 75))
        self.regression_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.regression_list.setObjectName("regression_list")
        item = QtWidgets.QListWidgetItem()
        self.regression_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.regression_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.regression_list.addItem(item)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.regression_list)
        self.corrLabel = QtWidgets.QLabel(self.formGroupBox)
        self.corrLabel.setObjectName("corrLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.corrLabel)
        self.CorrelationList = QtWidgets.QListWidget(self.formGroupBox)
        self.CorrelationList.setMaximumSize(QtCore.QSize(16777215, 75))
        self.CorrelationList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.CorrelationList.setObjectName("CorrelationList")
        item = QtWidgets.QListWidgetItem()
        self.CorrelationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CorrelationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CorrelationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CorrelationList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.CorrelationList.addItem(item)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.CorrelationList)
        self.theta0Label = QtWidgets.QLabel(self.formGroupBox)
        self.theta0Label.setObjectName("theta0Label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.theta0Label)
        self.theta0LineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.theta0LineEdit.setObjectName("theta0LineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.theta0LineEdit)
        self.ThetaL_Label = QtWidgets.QLabel(self.formGroupBox)
        self.ThetaL_Label.setObjectName("ThetaL_Label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.ThetaL_Label)
        self.ThetaL = QtWidgets.QLineEdit(self.formGroupBox)
        self.ThetaL.setObjectName("ThetaL")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.ThetaL)
        self.ThetaU_Label = QtWidgets.QLabel(self.formGroupBox)
        self.ThetaU_Label.setObjectName("ThetaU_Label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ThetaU_Label)
        self.ThetaU = QtWidgets.QLineEdit(self.formGroupBox)
        self.ThetaU.setObjectName("ThetaU")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ThetaU)
        self.randomStartLabel = QtWidgets.QLabel(self.formGroupBox)
        self.randomStartLabel.setObjectName("randomStartLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.randomStartLabel)
        self.randomStartLineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.randomStartLineEdit.setObjectName("randomStartLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.randomStartLineEdit)
        self.normalize_label = QtWidgets.QLabel(self.formGroupBox)
        self.normalize_label.setObjectName("normalize_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.normalize_label)
        self.normalize_list = QtWidgets.QListWidget(self.formGroupBox)
        self.normalize_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.normalize_list.setObjectName("normalize_list")
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.normalize_list.addItem(item)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.normalize_list)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setToolTip(("<html><head/><body><p><span style=\" font-weight:600;\">Gaussian Processes (GP)</span>�are a generic supervised learning method designed to solve�<span style=\" font-style:italic;\">regression</span>�and�<span style=\" font-style:italic;\">probabilistic classification</span>�problems.</p><p>The advantages of Gaussian processes are:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">The prediction interpolates the observations (at least for regular kernels).</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">The prediction is probabilistic (Gaussian) so that one can compute empirical confidence intervals and decide based on those if one should refit (online fitting, adaptive fitting) the prediction in some region of interest.</li><li style=\" margin-top:0px; margin-bottom:10px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">Versatile: different�<a href=\"http://scikit-learn.org/stable/modules/gaussian_process.html#gp-kernels\"><span style=\" color:#2878a2;\">kernels</span></a>�can be specified. Common kernels are provided, but it is also possible to specify custom kernels.</li></ul><p>The disadvantages of Gaussian processes include:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">They are not sparse, i.e., they use the whole samples/features information to perform the prediction.</li><li style=\" margin-top:0px; margin-bottom:10px; margin-left:65px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\">They lose efficiency in high dimensional spaces � namely when the number of features exceeds a few dozens.</li></ul><p><a name=\"gaussian-process-regression-gpr\"/><br/></p></body></html>"))
        self.reductionMethodLabel.setText(("Choose dimensionality reduction method:"))
        __sortingEnabled = self.DimRedList.isSortingEnabled()
        self.DimRedList.setSortingEnabled(False)
        item = self.DimRedList.item(0)
        item.setText(("PCA"))
        item = self.DimRedList.item(1)
        item.setText(("FastICA"))
        self.DimRedList.setSortingEnabled(__sortingEnabled)
        self.numOfComponenetsLabel.setText(("Number of Components"))
        self.numOfComponenetsLineEdit.setText(("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"))
        self.regrLabel.setText(("Regression Types"))
        __sortingEnabled = self.regression_list.isSortingEnabled()
        self.regression_list.setSortingEnabled(False)
        item = self.regression_list.item(0)
        item.setText(("Linear"))
        item = self.regression_list.item(1)
        item.setText(("Constant"))
        item = self.regression_list.item(2)
        item.setText(("Quadratic"))
        self.regression_list.setSortingEnabled(__sortingEnabled)
        self.corrLabel.setText(("Correlation Types"))
        __sortingEnabled = self.CorrelationList.isSortingEnabled()
        self.CorrelationList.setSortingEnabled(False)
        item = self.CorrelationList.item(0)
        item.setText(("Squared Exponential"))
        item = self.CorrelationList.item(1)
        item.setText(("Absolute Exponential"))
        item = self.CorrelationList.item(2)
        item.setText(("Generalized Exponential"))
        item = self.CorrelationList.item(3)
        item.setText(("Cubic"))
        item = self.CorrelationList.item(4)
        item.setText(("Linear"))
        self.CorrelationList.setSortingEnabled(__sortingEnabled)
        self.theta0Label.setText(("Theta"))
        self.theta0LineEdit.setText(("0.1"))
        self.ThetaL_Label.setText(("Theta - Lower Bound"))
        self.ThetaU_Label.setText(("Theta - Upper Bound"))
        self.randomStartLabel.setText(("# of random starts for MLE"))
        self.normalize_label.setText(("Normalize"))
        __sortingEnabled = self.normalize_list.isSortingEnabled()
        self.normalize_list.setSortingEnabled(False)
        item = self.normalize_list.item(0)
        item.setText(("True"))
        item = self.normalize_list.item(1)
        item.setText(("False"))
        self.normalize_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

