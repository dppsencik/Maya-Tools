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
        self.scale_x_check = QtWidgets.QCheckBox("X")
        self.scale_y_check = QtWidgets.QCheckBox("Y")
        self.scale_z_check = QtWidgets.QCheckBox("Z")

        self.scale_x_min = QtWidgets.QLineEdit("1")
        self.scale_x_min.setFixedWidth(50)
        self.scale_x_max = QtWidgets.QLineEdit("1")
        self.scale_x_max.setFixedWidth(50)
        self.scale_y_min = QtWidgets.QLineEdit("1")
        self.scale_y_min.setFixedWidth(50)
        self.scale_y_max = QtWidgets.QLineEdit("1")
        self.scale_y_max.setFixedWidth(50)
        self.scale_z_min = QtWidgets.QLineEdit("1")
        self.scale_z_min.setFixedWidth(50)
        self.scale_z_max = QtWidgets.QLineEdit("1")
        self.scale_z_max.setFixedWidth(50)

        self.scale_x_min.setEnabled(False)
        self.scale_y_min.setEnabled(False)
        self.scale_z_min.setEnabled(False)
        self.scale_x_max.setEnabled(False)
        self.scale_y_max.setEnabled(False)
        self.scale_z_max.setEnabled(False)

        layout.addWidget(self.min_lbl, 0, 1)
        layout.addWidget(self.max_lbl, 0, 2)
        layout.addWidget(self.scale_x_check, 1, 0)
        layout.addWidget(self.scale_x_min, 1, 1)
        layout.addWidget(self.scale_x_max, 1, 2)
        layout.addWidget(self.scale_y_check, 2, 0)
        layout.addWidget(self.scale_y_min, 2, 1)
        layout.addWidget(self.scale_y_max, 2, 2)
        layout.addWidget(self.scale_z_check, 3, 0)
        layout.addWidget(self.scale_z_min, 3, 1)
        layout.addWidget(self.scale_z_max, 3, 2)
        return layout

    def create_rotation_options(self):
        layout = QtWidgets.QGridLayout()
        self.min_lbl = QtWidgets.QLabel("Min")
        self.max_lbl = QtWidgets.QLabel("Max")
        self.rotate_x_check = QtWidgets.QCheckBox("X")
        self.rotate_y_check = QtWidgets.QCheckBox("Y")
        self.rotate_z_check = QtWidgets.QCheckBox("Z")

        self.rot_x_min = QtWidgets.QLineEdit("0")
        self.rot_x_min.setFixedWidth(50)
        self.rot_x_max = QtWidgets.QLineEdit("0")
        self.rot_x_max.setFixedWidth(50)
        self.rot_y_min = QtWidgets.QLineEdit("0")
        self.rot_y_min.setFixedWidth(50)
        self.rot_y_max = QtWidgets.QLineEdit("0")
        self.rot_y_max.setFixedWidth(50)
        self.rot_z_min = QtWidgets.QLineEdit("0")
        self.rot_z_min.setFixedWidth(50)
        self.rot_z_max = QtWidgets.QLineEdit("0")
        self.rot_z_max.setFixedWidth(50)

        self.rot_x_min.setEnabled(False)
        self.rot_y_min.setEnabled(False)
        self.rot_z_min.setEnabled(False)
        self.rot_x_max.setEnabled(False)
        self.rot_y_max.setEnabled(False)
        self.rot_z_max.setEnabled(False)

        layout.addWidget(self.min_lbl, 0, 1)
        layout.addWidget(self.max_lbl, 0, 2)
        layout.addWidget(self.rotate_x_check, 1, 0)
        layout.addWidget(self.rot_x_min, 1, 1)
        layout.addWidget(self.rot_x_max, 1, 2)
        layout.addWidget(self.rotate_y_check, 2, 0)
        layout.addWidget(self.rot_y_min, 2, 1)
        layout.addWidget(self.rot_y_max, 2, 2)
        layout.addWidget(self.rotate_z_check, 3, 0)
        layout.addWidget(self.rot_z_min, 3, 1)
        layout.addWidget(self.rot_z_max, 3, 2)
        return layout

    def create_connections(self):
        self.scale_x_check.stateChanged.connect(self._scale_x_disable)
        self.scale_y_check.stateChanged.connect(self._scale_y_disable)
        self.scale_z_check.stateChanged.connect(self._scale_z_disable)
        self.rotate_x_check.stateChanged.connect(self._rotate_x_disable)
        self.rotate_y_check.stateChanged.connect(self._rotate_y_disable)
        self.rotate_z_check.stateChanged.connect(self._rotate_z_disable)
        self.source_btn.clicked.connect(self._set_source)
        self.source_select_btn.clicked.connect(self._select_source)
        self.destination_btn.clicked.connect(self._set_destination)
        self.destination_select_btn.clicked.connect(self._select_destination)
        self.scatter_btn.clicked.connect(self._scatter)

    @QtCore.Slot()
    def _scale_x_disable(self):
        if self.scale_x_check.isChecked():
            self.scale_x_max.setEnabled(True)
            self.scale_x_min.setEnabled(True)
        else:
            self.scale_x_max.setEnabled(False)
            self.scale_x_min.setEnabled(False)

    @QtCore.Slot()
    def _scale_y_disable(self):
        if self.scale_y_check.isChecked():
            self.scale_y_max.setEnabled(True)
            self.scale_y_min.setEnabled(True)
        else:
            self.scale_y_max.setEnabled(False)
            self.scale_y_min.setEnabled(False)

    @QtCore.Slot()
    def _scale_z_disable(self):
        if self.scale_z_check.isChecked():
            self.scale_z_max.setEnabled(True)
            self.scale_z_min.setEnabled(True)
        else:
            self.scale_z_max.setEnabled(False)
            self.scale_z_min.setEnabled(False)

    @QtCore.Slot()
    def _rotate_x_disable(self):
        if self.rotate_x_check.isChecked():
            self.rot_x_max.setEnabled(True)
            self.rot_x_min.setEnabled(True)
        else:
            self.rot_x_max.setEnabled(False)
            self.rot_x_min.setEnabled(False)

    @QtCore.Slot()
    def _rotate_y_disable(self):
        if self.rotate_y_check.isChecked():
            self.rot_y_max.setEnabled(True)
            self.rot_y_min.setEnabled(True)
        else:
            self.rot_y_max.setEnabled(False)
            self.rot_y_min.setEnabled(False)

    @QtCore.Slot()
    def _rotate_z_disable(self):
        if self.rotate_z_check.isChecked():
            self.rot_z_max.setEnabled(True)
            self.rot_z_min.setEnabled(True)
        else:
            self.rot_z_max.setEnabled(False)
            self.rot_z_min.setEnabled(False)

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
        if self.scale_x_check.isChecked():
            self.scatter.scale_ranges[0] = \
                [float(self.scale_x_min.text()), float(self.scale_x_max.text())]

        if self.scale_y_check.isChecked():
            self.scatter.scale_ranges[1] = \
                [float(self.scale_y_min.text()), float(self.scale_y_max.text())]

        if self.scale_z_check.isChecked():
            self.scatter.scale_ranges[2] = \
                [float(self.scale_z_min.text()), float(self.scale_z_max.text())]

        if self.rotate_x_check.isChecked():
            self.scatter.rotate_ranges[0] = \
                [int(self.rot_x_min.text()), int(self.rot_x_max.text())]
            log.warning(self.scatter.rotate_ranges[0])

        if self.rotate_y_check.isChecked():
            self.scatter.rotate_ranges[1] = \
                [int(self.rot_y_min.text()), int(self.rot_y_max.text())]

        if self.rotate_z_check.isChecked():
            self.scatter.rotate_ranges[2] = \
                [int(self.rot_z_min.text()), int(self.rot_z_max.text())]


class Scatter:

    def __init__(self):
        self.rotate_ranges = [
            [0, 0],
            [0, 0],
            [0, 0]]
        self.scale_ranges = [
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
        self.rotate_ranges = [
            [0, 0],
            [0, 0],
            [0, 0]]
        self.scale_ranges = [
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
        for r in self.rotate_ranges:
            if r[0] == r[1]:
                rotation.append(r[0])
            else:
                rotation.append(rand.randrange(r[0], r[1]))

        return rotation

    def get_scale_range(self):
        scale = []
        for r in self.scale_ranges:
            if r[0] == r[1]:
                scale.append(r[0])
            else:
                scale.append(float('%.2f' % rand.uniform(r[0], r[1])))

        return scale
