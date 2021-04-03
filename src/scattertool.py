import maya.cmds as cmds
import pymel.core as pmc
import logging

log = logging.getLogger(__name__)


class Scatter:

    def __init__(self):
        selection = cmds.ls(orderedSelection=True)
        self.source = selection[0]
        # vertices = cmds.filterExpand(sm=31)

        print "Source: %s" % self.source

        if cmds.objectType(self.source) == "transform":
            self.instance_selection()
        else:
            log.warning("Please make sure your first selection is an object.")

    def instance_selection(self):
        instance_result = cmds.instance(self.source, name=self.source + "_instance%")
        cmds.move(1, 1, 1, instance_result,)
