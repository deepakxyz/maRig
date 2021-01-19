import maya.cmds as mc
import maya.mel as mm

from rigLib.utils import control_create


class Base():

    """
    class for building rig base control
    """

    def __init__(self,
                 characterName="new",
                 scale=0.6,
                 ):
        '''

        '''
        self.topGrp = mc.group(n=characterName + '_rig_grp', em=1)
        self.rigGrp = mc.group(n='rig_grp', em=1, p=self.topGrp)
        self.modelGrp = mc.group(n='model_grp', em=1, p=self.topGrp)

        characterNameAt = 'characterName'
        sceneObjectTypeAt = 'sceneObjectType'

        for at in [characterNameAt, sceneObjectTypeAt]:
            mc. addAttr(self.topGrp, ln=at, dt='string')

        mc.setAttr(self.topGrp + "." + characterNameAt,
                   characterName, type="string", l=1)
        mc.setAttr(self.topGrp + "." + sceneObjectTypeAt,
                   'rig', type="string", l=1)

        # init control module
        Control = control_create.Control()

        # base control create
        self.baseControl = Control.create(
            scale=scale, name=characterName, thickness=1.2, parent=self.rigGrp)

        print('Reload working')


def baseControl():
    Control = control_create.Control()
    baseControl = Control.create(scale=0.5, name="Base")
    return baseControl


class BaseStructure():
    '''
    class for creating base rig structure
    '''

    def __init__(self,
                 characterName="new",
                 baseObj=None
                 ):
        '''
        @param characterName: str, name of the structure
        '''

        self.topGrp = mc.group(n=name + "_Rig_grp", em=1)

        self.controlGrp = mc.group(
            name=name + "_Control_grp", em=1, p=self.topGrp)
        self.jointsGrp = mc.group(
            name=name + "_Joints_grp", em=1, p=self.topGrp)
        self.partsGrp = mc.group(
            name=name + "_Parts_grp", em=1, p=self.topGroup)
        self.partsNoTransGrp = mc.group(
            n=name + "_PartsNoTrans_grp", em=1, p=self.topGrp)

        mc.hide(self.partsGrp, self.partsNoTransGrp)

        # parent module
        if baseObj:
            if mc.objExists(baseObj):
                mc.parent(self.topGrp, baseObj)
