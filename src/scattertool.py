import maya.cmds as cmds
import pymel.core as pmc
import logging

log = logging.getLogger(__name__)

class Scatter():

    def __init__(self):
        selection = cmds.ls(orderedSelection=True)
        print selection
        source = selection[0]
