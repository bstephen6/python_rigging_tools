#quick broken FK/IK SwitchBlend Creator

import maya.cmds as cmds

#make a selection array to store the joint chain selected
sel = cmds.ls(sl=True)

#a healthy good house keeping selection clearing
cmds.select(cl=True)

#first loop: loops the joints for thier positions and orient values and creates..
#.. the joints for both of the extra blend joint chains
#   use an enumerate to get index to make parenting them a little easier.
for index, x in enumerate(sel):
    #save the name modified names of the joint in the loop to name the duplicates with
    fkJointName = x + '_fk_driver'
    ikJointName = x + '_ik_driver'
    
    #store the postiion and orient values for the joint in the loop
    bindJointPos = cmds.xform( x, q = True, ws = True, t = True)
    bindJointOrientX = cmds.getAttr(x + '.jointOrientX')
    bindJointOrientY = cmds.getAttr(x + '.jointOrientY')
    bindJointOrientZ = cmds.getAttr(x + '.jointOrientZ')

    #the joint creation lines
    cmds.joint( n = fkJointName, p = bindJointPos)
    #seperate with a healthy house keeping selection clear
    cmds.select(cl=True)
    
    cmds.joint( n = ikJointName, p = bindJointPos)
    #seperate with a healthy house keeping selection clear
    cmds.select(cl=True)

    #set the orient values for the FK joint
    cmds.setAttr(fkJointName + '.jointOrientX', bindJointOrientX)
    cmds.setAttr(fkJointName + '.jointOrientY', bindJointOrientY)
    cmds.setAttr(fkJointName + '.jointOrientZ', bindJointOrientZ)

    #set the orient values for the IK joint
    cmds.setAttr(ikJointName + '.jointOrientX', bindJointOrientX)
    cmds.setAttr(ikJointName + '.jointOrientY', bindJointOrientY)
    cmds.setAttr(ikJointName + '.jointOrientZ', bindJointOrientZ)

    #check the enumeration index, if it's 0 then nothing needs to be done..
    #.. if its 1 then parent the object to index 0.. if it's 2 then parent to index 1
    #.. use try and excepts to catch errors
    if index == 0:
        print('index is 0, do nothing to see here')
        continue
    if index == 1:
        try:
            cmds.parent(fkJointName, (str(sel[0] + '_fk_driver')))
            cmds.parent(ikJointName, (str(sel[0] + '_ik_driver')))
        except:
            print('Index is 1, but the parenting did not work for whatever reason')
            pass
    if index == 2:
        try:
            cmds.parent(fkJointName, (str(sel[1] + '_fk_driver')))
            cmds.parent(ikJointName, (str(sel[1] + '_ik_driver')))
        except:
            print('Index is 2, but the parenting did not work for whatever reason')
            pass


#store the would be names of groups for the duplicate joint chains
fkGrp = (str(sel[0] + '_fk_chain_group'))
ikGrp = (str(sel[0] + '_ik_chain_group'))

#now to create a group to store each of the duplicate joint chains..
#.. also freeze the transforms and
cmds.group((str(sel[0] + '_fk_driver')), n = fkGrp)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)
cmds.group((str(sel[0] + '_ik_driver')), n = ikGrp)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)

#store the position of the base joint of the the bind chain
baseLoc = cmds.xform((str(sel[0])), q = 1, ws = 1, rp = 1)

#change the rotate and scale pivots for both chain groups to the..
#.. location of the base joint in the bind chain 
cmds.xform(fkGrp, ws = True, sp = baseLoc, rp = baseLoc)
cmds.xform(ikGrp, ws = True, sp = baseLoc, rp = baseLoc)

#a healthy selection clearing for good house keeping
cmds.select(cl=True)

#select the base of the skin bind joint chain and pickwalk up to the parent joint
cmds.select((str(sel[0])))
cmds.pickWalk(direction='up')

#save that selection in a string to call in a parent constrain command
pConst = cmds.ls(sl=True)

#parent constrain the joint chain groups (contrainee/child) to the parent of the..
#.. bind skin joint chain base joint (constrainor/parent).
cmds.parentConstraint( pConst, fkGrp, mo=True)
cmds.parentConstraint( pConst, ikGrp, mo=True)

#create the IK handle for the IK joint chain

#create ctl curves, spheres, that can be used to drive the fk chain and ik handle

#snap fk ctls to the corresponding joint locations (preferably through a loop)

#set the rotations for the ctls curves to match the joint orientations

#snap the IK handle ctl to the ik handle position

#set the rotation for the IK handle Ctl

#snap the PV ctl to its needed pos (use the polyplane method)

#constrain the ctls to the fk joints

#constain the IK handle ctls to the IK handle, and the PV constrain the PV ctl..
#.. for the ik handle

#Loop through the bind joint chain and then orient constain the bind joints(constrainee/child)..
#.. to the fk and ik joint chaints(constrainor/parents) so that it's doubled up like..
#.. in my previous fk/ik switches

#Create and Drop in a text "FK/IK" ctl curve and position it 2 paces back from..
#.. the wrist controls, group it and parentconstrain the group (constrainee/child)..
#.. to the brind shoulder 

#Create the fk/ik blend attr in the ctl curve

#then set up the set driven key connection

