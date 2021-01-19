import maya.cmds as mc
import maya.mel as mm

from rigLib.utils.controls import control_create


class Base():

    """
    class for building rig base control
    """

    def __init__(self,
                 characterName="new",
                 scale=0.6,
                 ):
        '''
        @pram chracterName: str, character name
        @pram scale: float, general scale of the rig
        @return: None
        '''
        # init control module
        Control = control_create.Control()

        # base control create
        self.baseControl = Control.create(
            scale=scale, name=characterName, thickness=1.2)


def baseControl():
    Control = control_create.Control()
    baseControl = Control.create(scale=0.5, name="Base")
    return baseControl


# Creating base structure for the rig
def BaseStruct():
    topGrp = mc.group(n=prefix + 'Module_grp', em=1)
