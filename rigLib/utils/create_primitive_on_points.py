# Create primitive on the given point
# Do not use getAttr to get the transform location
# Always use xform to get the world space location
# And make sure to multiple the value with the unit (m = 100)

def createPoleVectorPoly(joints):
    points = []
    for joint in joints:
        position = mc.xform(joint + "_IK", a=1, q=1, ws=1, rp=1)
        multiply_position = []
        for i in position:
            i = i * 100
            multiply_position.append(i)
        points.append(multiply_position)
    print(points)


joints = ["l_humerus", "l_radius", "l_wrist"]
createPoleVectorPoly(joints)