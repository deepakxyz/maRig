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

    # Create controls
    def create(self, name="control", type="circle", scale=1.0, suffix="_ctrl", color=21, thickness=1.0, parent=""):
        '''
        @pram: name, str
        @pram: type, str
        @pram: scale, float
        @pram: suffix, str
        @pram: color, int
        @pram: thickness, float
        @pram: parent, str

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
            mc.makeIdentity(apply=True, t=True, r=True, s=True, n=False, pn=1)

        # Set color
        mc.select(control)
        self.setColorIndex(color)

        # Set thickness for the control shapes
        if thickness > 1.0:
            controlShape = mc.listRelatives(control, s=True)
            for c in controlShape:
                mc.setAttr('{0}.lineWidth'.format(c), thickness)

        # Set parent object
        if parent:
            if mc.objExists(parent):
                mc.parent(control, parent)

        # returns control object
        return control[0]

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
