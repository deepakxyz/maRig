import maya.cmds as mc
import maya.mel as mm


class Base:

    """
    class for building rig base control
    """

    def __init__(self,
                 prefix="new",
                 scale=1.0,
                 translateTo="",
                 rotateTo="",
                 parent='',
                 lookChannels=['s', 'v']
                 ):

        pass

mc.polySphere()