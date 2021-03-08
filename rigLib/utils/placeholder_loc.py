from rigLib.utils.control_create import Control
import maya.cmds as mc
control = Control()


def placeHolder(name,suffix,joint,loc,type,aimAxis,scale,color,parent,constraintType):
    # create placeholder locator
    main_loc = mc.spaceLocator(n="main_loc",p=[0,0,0])
    sub_loc = mc.spaceLocator(n="sub_loc")

    # move the sub loc
    mc.move(loc[0],loc[1],loc[2],sub_loc,wd=True)
    mc.parent(sub_loc,main_loc)
    if constraintType == "point":
        temp_con = mc.parentConstraint(joint, main_loc)
    else:
        temp_con = mc.parentConstraint(joint, main_loc)

    # create control
    ctrl = control.create(name=name,suffix=suffix,type=type, aimAxis=aimAxis, scale=scale, color=color,parent=parent)
    mc.delete(mc.parentConstraint(sub_loc,ctrl[0]))
    mc.delete(temp_con)
    mc.delete(main_loc)
    return ctrl
