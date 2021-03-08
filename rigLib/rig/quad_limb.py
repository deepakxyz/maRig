import maya.cmds as mc
from rigLib.utils.control_create import Control
# quadruped
control = Control()

# create IK control
def IKCtrl(joints):
    # IK control
    IK_control_joint_name = joints[2] + "_IK"
    IK_control = control.create(name=IK_control_joint_name, translateTo=joints[2], scale=0.05, type="Four Arrows")
    return IK_control


# create pole vector control with offset
def poleVectorCtrl(joint):
    # Create Pole Vector location using Locators.
    main_poleVector = mc.spaceLocator(n="main_loc", p=[0, 0, 0])
    sub_locator = mc.spaceLocator(n="sub_loc")
    # move -r -os -wd -1.088376 0 0 ;
    if joint.startswith('r_'):
        x = 0.365
        aimAxis = "-Z"
    elif joint.startswith("l_"):
        x = -0.365
        aimAxis = "Z"

    mc.move(x, 0, 0, sub_locator, wd=True)
    mc.parent(sub_locator, main_poleVector)
    temp = mc.parentConstraint(joint, main_poleVector)

    PV_control = control.create(name=joint + "_pv", aimAxis=aimAxis, translateTo=joint, scale=0.02, type="Sphere Pin")
    mc.delete(mc.parentConstraint(sub_locator, PV_control[0]))
    mc.delete(temp)
    mc.delete(main_poleVector)

    return PV_control


# create IK effector
def armIKEffector(joints):
    #  set IK effector
    sj = joints[0] + "_IK"
    ee = joints[2] + "_IK"
    ikHandle = mc.ikHandle(n=sj + "_Handle", sj=sj, ee=ee, sol="ikRPsolver")
    mc.parent(ikHandle[0], ee + "_ctrl")
    return ikHandle[0]


# armIK
def armIK(joints):
    ikControl = IKCtrl(joints)
    pole_v_ctrl = poleVectorCtrl(joints[1])
    ik_handle = armIKEffector(joints)
    # create pole vector control
    mc.poleVectorConstraint(pole_v_ctrl, ik_handle)


armIK(joints)

####################################
def ik_fk_blender(joint):
    # create placeholder locator
    main_loc = mc.spaceLocator(n = "main_loc", p=[0,0,0])
    sub_loc = mc.spaceLocator(n="sub_loc")
    # move sub loc
    x = -0.104
    z = 0.108

    mc.move(x,0,z,sub_loc,wd=True)
    mc.parent(sub_loc,main_loc)
    temp_constraint = mc.parentConstraint(joint,main_loc)

    ik_fk_blender_ctrl = control.create(name=joint + "_blender")


def placeholder_loc(joint,loc,ctrlType,ctrlColor,ctrlShape,aimAxis):
    # create placeholder locator
    main_loc = mc.spaceLocator(n = "main_loc", p = [0,0,0])
    sub_loc = mc.spaceLocator(n = "sub_loc")
    # move the sub loc
    location = loc
    mc.move(location[0],location[1],location[2],sub_loc,wd=True)
    mc.parent(sub_loc,main_loc)
    temp_constraint = mc.parentConstraint(joint,main_loc)
