import pymel.core as pmc
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
        self.setMinimumWidth(500)
        self.setMaximumHeight(500)
        self.setWindowFlags(self.windowFlags() ^
                            QtCore.Qt.WindowContextHelpButtonHint)
        self.title_lbl = QtWidgets.QLabel("Scatter")
        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.title_lbl)
        self.setLayout(self.main_lay)

class Scatter:

    def __init__(self):
        selection = cmds.ls(orderedSelection=True)
        self.source = selection[0]
        self.vertices = cmds.filterExpand(sm=31)
        self.rotateRanges = [[0, 0], [0, 360], [0, 0]]
        self.scaleRanges = [[1.0, 2.0], [1.0, 2.0], [1.0, 2.0]]
        if cmds.objectType(self.source) == "transform":
            self.instance_selection()
        else:
            log.warning("Please make sure your first selection is an object.")

    def instance_selection(self):
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





