import logging
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance
import random as rand


log = logging.getLogger(__name__)


def maya_main_window():
    """Return the maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window), QtWidgets.QWidget)


class ScatterUI(QtWidgets.QDialog):
    """Scatter UI Class"""

    def __init__(self):
        super(ScatterUI, self).__init__(parent=maya_main_window())
        self.setWindowTitle("Scatter Tool")
        self.setMinimumWidth(300)
        self.setMaximumHeight(1000)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.scatter = Scatter()
        self.create_ui()
        self.main_lay.addWidget(self.scatter_btn)
        self.setLayout(self.main_lay)
        self.create_connections()

    def create_ui(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self.selection_lay = self.create_selection_options()
        self.rotation_lay = self.create_rotation_options()
        self.scale_lay = self.create_scale_options()

        self.scale_lbl = QtWidgets.QLabel("Random Scale Options:")
        self.scale_lbl.setStyleSheet("font: bold 18px")

        self.rotation_lbl = QtWidgets.QLabel("Random Rotation Options:")
        self.rotation_lbl.setStyleSheet("font: bold 18px")

        self.main_lay.addLayout(self.selection_lay)
        self.main_lay.addStretch()
        self.main_lay.addWidget(self.scale_lbl)
        self.main_lay.addLayout(self.scale_lay)
        self.main_lay.addStretch()
        self.main_lay.addWidget(self.rotation_lbl)
        self.main_lay.addLayout(self.rotation_lay)
        self.main_lay.addStretch()
        self.scatter_btn = QtWidgets.QPushButton("Scatter")
        self.setLayout(self.main_lay)

    def create_selection_options(self):
        layout = QtWidgets.QGridLayout()
        self.source_btn = QtWidgets.QPushButton("Add Selection as the Source")
        self.source_select_btn = QtWidgets.QPushButton("Select")
        self.destination_btn = QtWidgets.QPushButton("Add Selection as the Destination")
        self.destination_select_btn = QtWidgets.QPushButton("Select")

        self.source_select_btn.setFixedWidth(75)
        self.destination_select_btn.setFixedWidth(75)

        layout.addWidget(self.source_btn, 0, 0)
        layout.addWidget(self.source_select_btn, 0, 1)
        layout.addWidget(self.destination_btn, 1, 0)
        layout.addWidget(self.destination_select_btn, 1, 1)
        return layout

    def create_scale_options(self):
        layout = QtWidgets.QGridLayout()
        self.min_lbl = QtWidgets.QLabel("Min")
        self.max_lbl = QtWidgets.QLabel("Max")
        self.scaleXCheck = QtWidgets.QCheckBox("X")
        self.scaleYCheck = QtWidgets.QCheckBox("Y")
        self.scaleZCheck = QtWidgets.QCheckBox("Z")

        self.scaleXMin = QtWidgets.QLineEdit("1")
        self.scaleXMin.setFixedWidth(50)
        self.scaleXMax = QtWidgets.QLineEdit("1")
        self.scaleXMax.setFixedWidth(50)
        self.scaleYMin = QtWidgets.QLineEdit("1")
        self.scaleYMin.setFixedWidth(50)
        self.scaleYMax = QtWidgets.QLineEdit("1")
        self.scaleYMax.setFixedWidth(50)
        self.scaleZMin = QtWidgets.QLineEdit("1")
        self.scaleZMin.setFixedWidth(50)
        self.scaleZMax = QtWidgets.QLineEdit("1")
        self.scaleZMax.setFixedWidth(50)

        self.scaleXMin.setEnabled(False)
        self.scaleYMin.setEnabled(False)
        self.scaleZMin.setEnabled(False)
        self.scaleXMax.setEnabled(False)
        self.scaleYMax.setEnabled(False)
        self.scaleZMax.setEnabled(False)

        layout.addWidget(self.min_lbl, 0, 1)
        layout.addWidget(self.max_lbl, 0, 2)
        layout.addWidget(self.scaleXCheck, 1, 0)
        layout.addWidget(self.scaleXMin, 1, 1)
        layout.addWidget(self.scaleXMax, 1, 2)
        layout.addWidget(self.scaleYCheck, 2, 0)
        layout.addWidget(self.scaleYMin, 2, 1)
        layout.addWidget(self.scaleYMax, 2, 2)
        layout.addWidget(self.scaleZCheck, 3, 0)
        layout.addWidget(self.scaleZMin, 3, 1)
        layout.addWidget(self.scaleZMax, 3, 2)
        return layout

    def create_rotation_options(self):
        layout = QtWidgets.QGridLayout()
        self.min_lbl = QtWidgets.QLabel("Min")
        self.max_lbl = QtWidgets.QLabel("Max")
        self.rotateXCheck = QtWidgets.QCheckBox("X")
        self.rotateYCheck = QtWidgets.QCheckBox("Y")
        self.rotateZCheck = QtWidgets.QCheckBox("Z")

        self.rotXMin = QtWidgets.QLineEdit("0")
        self.rotXMin.setFixedWidth(50)
        self.rotXMax = QtWidgets.QLineEdit("0")
        self.rotXMax.setFixedWidth(50)
        self.rotYMin = QtWidgets.QLineEdit("0")
        self.rotYMin.setFixedWidth(50)
        self.rotYMax = QtWidgets.QLineEdit("0")
        self.rotYMax.setFixedWidth(50)
        self.rotZMin = QtWidgets.QLineEdit("0")
        self.rotZMin.setFixedWidth(50)
        self.rotZMax = QtWidgets.QLineEdit("0")
        self.rotZMax.setFixedWidth(50)

        self.rotXMin.setEnabled(False)
        self.rotYMin.setEnabled(False)
        self.rotZMin.setEnabled(False)
        self.rotXMax.setEnabled(False)
        self.rotYMax.setEnabled(False)
        self.rotZMax.setEnabled(False)

        layout.addWidget(self.min_lbl, 0, 1)
        layout.addWidget(self.max_lbl, 0, 2)
        layout.addWidget(self.rotateXCheck, 1, 0)
        layout.addWidget(self.rotXMin, 1, 1)
        layout.addWidget(self.rotXMax, 1, 2)
        layout.addWidget(self.rotateYCheck, 2, 0)
        layout.addWidget(self.rotYMin, 2, 1)
        layout.addWidget(self.rotYMax, 2, 2)
        layout.addWidget(self.rotateZCheck, 3, 0)
        layout.addWidget(self.rotZMin, 3, 1)
        layout.addWidget(self.rotZMax, 3, 2)
        return layout

    def create_connections(self):
        self.scaleXCheck.stateChanged.connect(self._scale_x_disable)
        self.scaleYCheck.stateChanged.connect(self._scale_y_disable)
        self.scaleZCheck.stateChanged.connect(self._scale_z_disable)
        self.rotateXCheck.stateChanged.connect(self._rotate_x_disable)
        self.rotateYCheck.stateChanged.connect(self._rotate_y_disable)
        self.rotateZCheck.stateChanged.connect(self._rotate_z_disable)
        self.source_btn.clicked.connect(self._set_source)
        self.source_select_btn.clicked.connect(self._select_source)
        self.destination_btn.clicked.connect(self._set_destination)
        self.destination_select_btn.clicked.connect(self._select_destination)
        self.scatter_btn.clicked.connect(self._scatter)

    @QtCore.Slot()
    def _scale_x_disable(self):
        if self.scaleXCheck.isChecked():
            self.scaleXMax.setEnabled(True)
            self.scaleXMin.setEnabled(True)
        else:
            self.scaleXMax.setEnabled(False)
            self.scaleXMin.setEnabled(False)

    @QtCore.Slot()
    def _scale_y_disable(self):
        if self.scaleYCheck.isChecked():
            self.scaleYMax.setEnabled(True)
            self.scaleYMin.setEnabled(True)
        else:
            self.scaleYMax.setEnabled(False)
            self.scaleYMin.setEnabled(False)

    @QtCore.Slot()
    def _scale_z_disable(self):
        if self.scaleZCheck.isChecked():
            self.scaleZMax.setEnabled(True)
            self.scaleZMin.setEnabled(True)
        else:
            self.scaleZMax.setEnabled(False)
            self.scaleZMin.setEnabled(False)

    @QtCore.Slot()
    def _rotate_x_disable(self):
        if self.rotateXCheck.isChecked():
            self.rotXMax.setEnabled(True)
            self.rotXMin.setEnabled(True)
        else:
            self.rotXMax.setEnabled(False)
            self.rotXMin.setEnabled(False)

    @QtCore.Slot()
    def _rotate_y_disable(self):
        if self.rotateYCheck.isChecked():
            self.rotYMax.setEnabled(True)
            self.rotYMin.setEnabled(True)
        else:
            self.rotYMax.setEnabled(False)
            self.rotYMin.setEnabled(False)

    @QtCore.Slot()
    def _rotate_z_disable(self):
        if self.rotateZCheck.isChecked():
            self.rotZMax.setEnabled(True)
            self.rotZMin.setEnabled(True)
        else:
            self.rotZMax.setEnabled(False)
            self.rotZMin.setEnabled(False)

    @QtCore.Slot()
    def _scatter(self):
        self.set_properties_from_ui()
        self.scatter.instance_selection()

    @QtCore.Slot()
    def _set_source(self):
        self.scatter.set_selection_source()

    @QtCore.Slot()
    def _set_destination(self):
        self.scatter.set_destination()

    @QtCore.Slot()
    def _select_source(self):
        cmds.select(self.scatter.source)

    @QtCore.Slot()
    def _select_destination(self):
        cmds.select(self.scatter.vertices)

    def set_properties_from_ui(self):
        if self.scaleXCheck.isChecked():
            self.scatter.scaleRanges[0] = \
                [float(self.scaleXMin.text()), float(self.scaleXMax.text())]

        if self.scaleYCheck.isChecked():
            self.scatter.scaleRanges[1] = \
                [float(self.scaleYMin.text()), float(self.scaleYMax.text())]

        if self.scaleZCheck.isChecked():
            self.scatter.scaleRanges[2] = \
                [float(self.scaleZMin.text()), float(self.scaleZMax.text())]

        if self.rotateXCheck.isChecked():
            self.scatter.rotateRanges[0] = \
                [int(self.rotXMin.text()), int(self.rotXMax.text())]
            log.warning(self.scatter.rotateRanges[0])

        if self.rotateYCheck.isChecked():
            self.scatter.rotateRanges[1] = \
                [int(self.rotYMin.text()), int(self.rotYMax.text())]

        if self.rotateZCheck.isChecked():
            self.scatter.rotateRanges[2] = \
                [int(self.rotZMin.text()), int(self.rotZMax.text())]


class Scatter:

    def __init__(self):
        self.rotateRanges = [
            [0, 0],
            [0, 0],
            [0, 0]]
        self.scaleRanges = [
            [1.0, 1.0],
            [1.0, 1.0],
            [1.0, 1.0]]
        self.source = None

    def instance_selection(self):
        if self.source == None:
            selection = cmds.ls(orderedSelection=True)
            self.source = selection[0]
            self.vertices = cmds.filterExpand(sm=31)

        instance_group = cmds.group(empty=True, name=self.source + "_instanceGroup#")
        for vert in self.vertices:
            instance_result = cmds.instance(self.source, name=self.source + "_instance#")
            position = cmds.pointPosition(vert, world=True)
            cmds.xform(instance_result,
                       translation=position,
                       rotation=self.get_rotate_range(),
                       scale=self.get_scale_range())
            cmds.parent(instance_result, instance_group)
        cmds.xform(instance_group, centerPivots=True)
        self.rotateRanges = [
            [0, 0],
            [0, 0],
            [0, 0]]
        self.scaleRanges = [
            [1.0, 1.0],
            [1.0, 1.0],
            [1.0, 1.0]]

    def set_selection_source(self):
        selection = cmds.ls(orderedSelection=True)
        self.source = selection[0]
        if cmds.objectType(self.source) == "transform":
            return
        else:
            log.warning("Please make sure your first selection is an object.")
            self.source = None

    def set_destination(self):
        self.vertices = cmds.filterExpand(sm=31)

    def get_rotate_range(self):
        rotation = []
        for r in self.rotateRanges:
            if r[0] == r[1]:
                rotation.append(r[0])
            else:
                rotation.append(rand.randrange(r[0], r[1]))

        return rotation

    def get_scale_range(self):
        scale = []
        for r in self.scaleRanges:
            if r[0] == r[1]:
                scale.append(r[0])
            else:
                scale.append(float('%.2f' % rand.uniform(r[0], r[1])))

        return scale
