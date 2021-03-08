'''
Create control curves, change control curve colors and replace control curve shapes.
Change colors on the the shape level to avoid all children of the controls inheriting drawig overrides.

'''

import maya.cmds as mc
from control_shapes import ControlShapes

'''
Joint orient axis 
Aim axis = Y
Up axis = X
World Up axis = Z
'''


class Control:
    '''
    Class for create, update and set color to the controler
    '''

    # reload test command
    print("Reloaded 10")

    # Create controls
    def create(self, name="control", type="circle", translateTo="", aimAxis="Y", scale=1.0, suffix="_ctrl", color=21, thickness=1.0, parent=""
               ):
        '''
        @param name: str, name of the controller, @default: control
        @param type: str, shape of the controller, @default: circle
        @param translateTo: str, snap or move to the selected object
        @param aimAxis: str, Controler aim axis, @default: "Y"
        @param scale: float, scale of the controller, @default: 1.0
        @param suffix: str, contoller suffix, @default: "_ctrl"
        @param color: int, controller color index, @default: 21
        @param thickness: float, thickness of the controller, @default: 1
        @param parent: str, parent of the current locator, @default: None
        @param constraint: bool, add a constraint or not
        @param constraintType: str, type of constraint from the control to the control object.
        @param return: str, controllerer

        '''
        # Create control
        if type == "circle":
            control = mc.circle(name=name + suffix, d=3,
                                r=scale, nr=[0, 1, 0], ch=False)
        else:
            control = mc.curve(name=name + suffix, d=1,
                               p=ControlShapes.cvTuples[type])

            # Set scale
            mc.scale(scale, scale, scale, a=True)

        # Change control aimAxis
        if aimAxis == "Z":
            mc.setAttr(control + '.rz', 90)
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)
        elif aimAxis == "-Z":
            mc.setAttr(control + '.rz', -90)
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)
        elif aimAxis == "X":
            mc.setAttr(control + '.rx', 90)
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)
        elif aimAxis == "-X":
            mc.setAttr(control + '.rx', -90)
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)
        elif aimAxis == "-Y":
            mc.setAttr(control + '.ry', -90)
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)
        else:
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)

        # Set color
        mc.select(control)

        # if name.startswith('l_') and color == 21:
        #     color = 20
        #     self.setColorIndex(color)
        # elif name.startswith('r_') and color == 21:
        #     color = 23
        #     self.setColorIndex(color)
        # else:
        self.setColorIndex(color)

        # Set thickness for the control shapes
        if thickness > 1.0:
            controlShape = mc.listRelatives(control, s=True)
            for c in controlShape:
                mc.setAttr('{0}.lineWidth'.format(c), thickness)

        # Create control offset group
        controlOffset = mc.group(n=name + "_offset_grp", em=1)
        mc.parent(control, controlOffset)

        # Set parent object
        if parent:
            if mc.objExists(parent):
                mc.parent(controlOffset, parent)

        # Translate and rotate the controller to the joint
        if mc.objExists(translateTo):
            mc.delete(mc.pointConstraint(translateTo, controlOffset))
            mc.delete(mc.orientConstraint(translateTo, controlOffset))

        # returns control object
        return [controlOffset,control]

    # Function to set the color of the selected shapes.

    def setColorIndex(self, color):
        sel = mc.ls(sl=True, l=True)

        for objs in sel:
            # Getting and checking node type to act on shape level
            nType = mc.nodeType(objs)

            if nType == 'transform':
                objs = mc.listRelatives(objs, s=True)
            elif nType == 'shape':
                pass
            else:
                mc.error('Selected objects(s) is not a nurbs curve.')

            # Changing drawing override color on multiple shapes.
            for obj in objs:
                override = mc.getAttr('{0}.overrideEnabled'.format(obj))
                if override == 0:
                    mc.setAttr('{0}.overrideEnabled'.format(obj), 1)

                display = mc.getAttr('{0}.overrideDisplayType'.format(obj))
                if display != 0:
                    mc.setAttr('{0}.overrideDisplayType'.format(obj), 0)

                mc.setAttr('{0}.overrideColor'.format(obj), color)
