import maya.cmds as cmds
import pymel.core as pmc
import logging
import random as rand

log = logging.getLogger(__name__)


class Scatter:

    def __init__(self):
        selection = cmds.ls(orderedSelection=True)
        self.source = selection[0]
        self.vertices = cmds.filterExpand(sm=31)
        if cmds.objectType(self.source) == "transform":
            self.instance_selection()
        else:
            log.warning("Please make sure your first selection is an object.")

    def instance_selection(self):
        instance_group = cmds.group(empty=True, name=self.source + "_instanceGroup#")
        for vert in self.vertices:
            instance_result = cmds.instance(self.source, name=self.source + "_instance#")
            position = cmds.pointPosition(vert, world=True)
            cmds.xform(instance_result, translation=position)
            cmds.parent(instance_result, instance_group)
        cmds.xform(instance_group, centerPivots=True)

