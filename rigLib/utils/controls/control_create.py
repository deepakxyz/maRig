'''

Control Shape Tool made by Deepak Rajan

Create control curves, change control curve colors and replace control curve shapes.
Change colors on the the shape level to avoid all children of the controls inheriting drawig overrides.

'''

import maya.cmds as mc
from control_shapes import ControlShapes


class Control:
    '''
    Class for create, update and set color to the controler
    '''

    # create controls
    def create(self, name="control", type="circle", suffix="_ctrl", thickness=1.0):
        '''
        @pram: name, str

        '''
        if type == "circle":
            control = mc.circle(name=name + suffix, d=3,
                                r=2, nr=[0, 1, 0], ch=False)
        else:
            contorl = mc.curve(name=name + suffix, d=1,
                               p=ControlShapes.cvTuples[type])

        # Set thickness for the control shapes
        if thickness > 1.0:
            controlShape = mc.listRelatives(control, s=True)
            for c in controlShape:
                mc.setAttr('{0}.lineWidth'.format(c), thickness)

        # returns control object
        return control[0]
