import maya.cmds as mc
import maya.mel as mm

from rigLib.utils.controls import control_create


class Base():

    """
    class for building rig base control
    """

    def __init__(self, name="Base", scale=0.6, thickness=1.2):
        Control = control_create.Control()

        # base control create
        self.baseControl = Control.create(
            scale=scale, name=name, thickness=thickness)


def baseControl():
    Control = control_create.Control()
    baseControl = Control.create(scale=0.5, name="Base")
    return baseControl
