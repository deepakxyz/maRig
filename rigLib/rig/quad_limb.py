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


def ik_fk_blender_set(constraint_list, joints, name, suffix, joint, loc, type, scale, color, attribName, fk_grps,
                      ik_grps):
    # switch node
    switch = placeHolder(name=name, suffix=suffix, joint=joint, loc=loc, type=type, aimAxis="Y", scale=scale,
                         color=color, parent="", constraintType="point")

    # create a IK_FK_blend attribute
    mc.addAttr(switch[1], keyable=True, longName=attribName, attributeType="double", min=0, max=1, dv=0)

    # create reverse node
    reverse_node = mc.createNode("reverse")

    # connect Reverse
    mc.connectAttr(switch[1] + "." + attribName, reverse_node + ".input.inputX")

    # IK FK Switch connection
    i = 0
    for constraint in constraint_list:
        mc.connectAttr(switch[1] + "." + attribName, constraint + "." + joints[i] + "_FKW1")
        # print(switch[1] + "." + attribName, constraint + "."+ joints[i]+ "_FKW1")
        mc.connectAttr(reverse_node + ".output.outputX", constraint + "." + joints[i] + "_IKW0")
        # print(switch[1]+".IK_FK_Switch",constraint + "."+ joints[i]+ "_FKW1")
        i = i + 1

    # IK FK Control Visiblity connection
    # FK visibility
    for fk_offset_grp in fk_grps[0]:
        mc.connectAttr(switch[1] + "." + attribName, fk_offset_grp + '.' + "visibility")
        # Connected l_hand_switch_ctrl.IK_FK_Switch to l_humerus_FK_offset_grp.visibility. //

    # IK visibility
    ik_offset_grp = ik_grps[0][0]
    pv_offset_grp = ik_grps[1][0]
    mc.connectAttr(reverse_node + ".output.outputX", ik_offset_grp + '.' + "visibility")
    mc.connectAttr(reverse_node + ".output.outputX", pv_offset_grp + "." + "visibility")


# data
constraint_list = [u'l_humerus_IF_FK_constraint', u'l_radius_IF_FK_constraint', u'l_wrist_IF_FK_constraint']
joints = ['l_humerus', 'l_radius', 'l_wrist']
FK_ctrls = [[u'l_humerus_FK_offset_grp', u'l_radius_FK_offset_grp', u'l_wrist_FK_offset_grp'],
            [[u'l_humerus_FK_ctrl'], [u'l_radius_FK_ctrl'], [u'l_wrist_FK_ctrl']]]
IK_grps = [[u'l_wrist_IK_offset_grp', u'l_wrist_IK_ctrl'], [u'l_radius_pv_offset_grp', u'l_radius_pv_ctrl']]

ik_fk_blender_set(constraint_list=constraint_list, joints=joints, name="l_hand_switch", suffix="_ctrl", joint="l_wrist",
                  loc=[-0.104, 0, 0.108], type="Sphere", scale=0.01, color=24, attribName="IK_FK_Switch",
                  fk_grps=FK_ctrls, ik_grps=IK_grps)


