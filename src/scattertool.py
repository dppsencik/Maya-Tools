import maya.cmds as cmds
import pymel.core as pmc
import logging
import random as rand

log = logging.getLogger(__name__)


def get_random_numbers(num_range):
    result = []
    if num_range[1]-num_range[0] <= 5:
        for x in range(3):
            result.append(float('%.2f' % rand.uniform(num_range[0], num_range[1])))
    else:
        for x in range(3):
            result.append(rand.randrange(num_range[0], num_range[1]))
    return result


class Scatter:

    def __init__(self):
        selection = cmds.ls(orderedSelection=True)
        self.source = selection[0]
        self.vertices = cmds.filterExpand(sm=31)
        self.rotateRange = 0, 360                           # Values need to be checked elsewhere
        self.scaleRange = 1.0, 2.0                          # as to not cause errors with random
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
                       rotation=get_random_numbers(self.rotateRange),
                       scale=get_random_numbers(self.scaleRange))
            cmds.parent(instance_result, instance_group)
        cmds.xform(instance_group, centerPivots=True)





