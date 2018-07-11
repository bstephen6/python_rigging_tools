import maya.cmds as cmds
import maya.mel as mel

#ALSO THE IK NEEDS TO BE BUILT AND NAMED CORRECTLY TOO
#AS WELL AS THE WRIST OR ANKLE CTL NEEDS TO BE  SET UP WITH AN ORIENT CONSTRAINT BEFORE YOU MAKE THE IK
# okay so this tool will create and IK handle on top of a rig with FK already constrained to the joints and IK FK Switch from the selection of 3 joints and then a pre-placed ctl as the 4th and last object selected (Update!: select a 4th curve for the ik handle, and a 5th for the PV triangle)
#	because that will serve as the location and rotation of the fk ik switch curve

#another quick note have you fk switch ctl named for this because I'm quick scripting
#quick note! this should have a pop up screen like the dynamics tool run before the actual script runs to imput the prefered angle to insert (for now keep it 90 on the x, ill have to switch this to the y or whatever for the arm)
				# have it show a message like "Please rotate the intended middle joint to find the intended preferred angle, and input the value"
#ANOTHER NOTE THIS WORKS ON joints that have "L_" or "R_" specifically at the start of their name, this wont work so well with tails n stuff that don't mirror.

#also for now you will have to set the 'zMV' variable for the pole vector ctl distance for setting that for now




#GETTING VARS





#get the selection, store it in an array
sA = cmds.ls(sl=True)
cmds.select(cl=True)
zMV = -2

#get the switch control from the third to the end of the selection array
cL = sA[3]
#now get the joints from the selection array and store them in an array 
jL = [sA[0], sA[1], sA[2]]

mJ = sA[1]


#setting the prefered angle to 90 degrees on X since its usually supposed to be the axis an elbow or knee turns on.
cmds.setAttr((mJ + '.preferredAngleX'), 90)

#store the name for the ik handle to be named as well as the group name
#parse for the first part of the name its usually six character for L_foot or L_Hand
ikP = sA[3][0:6]
locPre = (ikP +'_switch')
ikFinGrpN = (locPre + '_finger_group')
#add ik handel on the end of that
ikN = (ikP + '_IK_handle')

#Get the ik ctl from the second to end selection
ikC = sA[4]
#store a new name for the ik control
ikCN = (ikN + '_ctl')
#and store a name for the ik handle group
ikCG = (ikN + '_group')
ikG = ikN.replace('_handle', '_group')




#BASICALLY THE ACTUAL START OF THE PROCESS




#lets start with the FK Locator creating loop
#well also store them in a locator array for later use in the expressions
locA = []
ctlA = []

for j in jL:
    #whip up a locator name with the same
    #parse for the specific joint without the mirror prefix such as "shoulder", "elbow" for the name
    jName = j[2:]
    ctlN = (j + '_ctl')
    ctlA.append(ctlN)
    # sow it up into somethign like "L_hand_switch_shoulder_loc"
    locN = (locPre + '_' + jName + '_loc')
    
    #storing the position in an array or vector to plug into the locator position
    jPos = cmds.xform( j, q = True, ws = True, t = True)
    
    #create the locator and name it
    cmds.spaceLocator(n = locN, p =(0, 0, 0))
    cmds.xform(locN, ws=True, t = jPos)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1)
    cmds.select(cl=True)
    locA.append(locN)
    
    #with it being in position of the joint from the line above we should take this locator and put it under the correct group (the group of the ctl of the joint it needs to track)
    #and give it an orient constraint from the joint itselt, so the joint drives the orient but the translate comes from being moved by the ctl groups to keep it all copestetic
    
    #so real quick lets derive what the name would be bas
    gN = j + "_group"
    #now parent it to the group
    cmds.parent(locN, gN)
    #Give it the orient constraint from the joint
    cmds.orientConstraint( j, locN )

    #turn off the constraints
    cmds.select(j)
    #this little line grabs the constraints of an object
    jCon = cmds.ls(dag=1, ap=1, sl=1, type="constraint")
    jConL = (len(jCon) - 1)
    jConAttr = (jCon[jConL] + '.' + ctlN + 'W0')
    cmds.setAttr(jConAttr, 0)
    
    #I Think this is all thats needed for the joint locators up next after this loop should be making the ik and setting that part up then the scripts and expressions


###############################################################################################
#BIG EDIT I NEED TO TAKE NOTE OF, I NEED TO FIX THE CREATING OF THE IK HANDLE IT KEEPS BREAKING handle positioning
#BUT FOR SOME REASON IF I MAKE IT MYSELF IN the interface i get no problems LOOK INTO WHY THAT IS I NEED THIS TO MAKE IK HANDLES PROPERLY
#create the IK handle from the selection
#cmds.ikHandle(n= ikN, sj = jL[0], ee = jL[2], sol = 'ikRPsolver')
###############################################################################################


#make groups for ik and ik ctl and fix their pivots on the group for ik Handle and ctl
cmds.select(cl=True)
cmds.group(em =True, n=ikCG)
cmds.group(ikN, n = ikG)

#store the xform of the joint to snap the group to
ikGL = cmds.xform(ikN, q=True, ws=True, t=True)

#get the fk group world space rotation
fkG = (sA[2] + '_group')
ikGR =cmds.xform( fkG , q=True, ws=True, rotation=True)

#move the group pivots to the location
cmds.xform(ikCG, ws = True, sp = ikGL, rp = ikGL)

#select and clear the make identities
cmds.select(cl=1)
cmds.select(ikCG)
cmds.makeIdentity(apply=True, t=1, r=0, s=0)
cmds.select(cl=1)

#now set the rotation for the ctl group
cmds.setAttr((ikCG+ '.rotateX'), ikGR[0])
cmds.setAttr((ikCG+ '.rotateY'), ikGR[1])
cmds.setAttr((ikC+ '.rotateZ'), ikGR[2])






#set up the pole vector by creating a triangle greo and snapping the verts to the joints in the ik chain and then grabbing the one for the elbow or knee and moveing it in Z axis
#then moving the traingle Ctl to the space in component and I think grabbing the rotation off the middle vertex rotate pivot or something and putting that on to the Ctl
#then make it the pole vector constrainor of the ik handle

#lets make a plane and merge two of the verts the 3rd and 4th and then make a short loop to snap them to the joints
pN = 'pv_plane'
cmds.polyPlane(n = pN, sx=1,sy=1, w=1, h=1)

cmds.polyMergeVertex('pv_plane.vtx[2]', 'pv_plane.vtx[3]', d = 1.5)

#i wanted to come up with a more clever way of reading the names for the Vertex and matching them up with the number in the array they should correspond to
#but for time Im making it less dynamic and more just getting this done because this is a specific part of the tool I can hard code out a lil

#get the locations for the joints
jL1 = cmds.xform( jL[0], q = 1, ws = 1, t = 1)
jL2 = cmds.xform( jL[1], q = 1, ws = 1, t = 1)
jL3 = cmds.xform( jL[2], q = 1, ws = 1, t = 1)

#move the vertex to the locations
cmds.xform('pv_plane.vtx[0]', ws = True, t = jL1)
cmds.xform('pv_plane.vtx[1]', ws = True, t = jL3)
#this is for the merged vertex or the point and it should go on the jL2 because thats the knee number
cmds.xform('pv_plane.vtx[2]', ws = True, t = jL2) 

cmds.select(cl=True)
#then select the knee vertex
cmds.select('pv_plane.vtx[2]')
#set the move tool to object because I guess thats what i think works better on average
#then move the knee ctl some sort of way in Z

#this line changes the move tool's tool mode for component, local, world, object etc. object mode is = 0, and component = 9, local space is  = 1, and world space  is =2 (its also the default value)
#(actually i do not need this since move has an object space flag)
#cmds.manipMoveContext( "Move", e=True, m = 0)

#now move it in the Z(will have to variable it to change it for now to make it just work for these rigs i need to do. itll be either positive 2ish)
cmds.move(zMV, os = True, z = True)

#I wanted to query the rotation of the rotate tool in component when you're selecting the vert so it can rotate the elbows in the correct orientation
#but that doesnt seem to be working out so lets skip that step entirely but put a pin in it for later if thats possible (might need open maya for that process)

#store the name of the pole vector ctl curve
pvCN = (sA[5])
pvNN = (ikP +'_pv')

#Rename the pole vector control real quick
cmds.rename(pvCN, pvNN)

#so lets snap the ctl to the point in space and delete the plane and call this part of the script done
pvCL = cmds.xform('pv_plane.vtx[2]', q=1, ws=1, t=1)
print(pvCL)
cmds.xform( pvNN , ws = True, t = pvCL)

#now lets delete the plane real quick since we've exhausted its use 
cmds.select(cl=True)
cmds.select(pN)
cmds.delete()
cmds.select(cl=True)

#now lets set the pole vector control to be the pole vector constraint for the ik handle
cmds.poleVectorConstraint( pvNN, ikN )


#move the ik control to the ik handel before constraining it
#store both rotation and location in vars
ikX = cmds.xform( ikN, q = True, ws = True, t = True)
#move ik control it to the location
cmds.rename(sA[4], ikCN)
cmds.xform(ikCN, ws = True, t = ikX)



#freeze the ctl
cmds.select(cl=True)
cmds.select(ikCN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)

### AND MAYBE HERE TOO OR AROUND THIS AREA TAKE A LOOK


#so now ill throw the ik control and pv control into the group
cmds.parent(ikCN, ikCG)
cmds.parent(pvNN, ikCG)


#now set the ctls to zero through set attr, then freeze
#ikControl being set
cmds.setAttr(ikCN + '.rotateX', 0)
cmds.setAttr(ikCN + '.rotateY', 0)
cmds.setAttr(ikCN + '.rotateZ', 0)
cmds.select(cl=True)
cmds.select(ikCN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)


#PV being set
cmds.setAttr(pvNN + '.rotateX', 0)
cmds.setAttr(pvNN + '.rotateY', 0)
cmds.setAttr(pvNN + '.rotateZ', 0)
cmds.select(cl=True)
cmds.select(pvNN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)


 
#need to constrainor the control to the constrainee's ik handle and joint orient
cmds.select(cl=True)
cmds.select(ikCN)
cmds.select(ikN, add=True)
cmds.pointConstraint(mo=True)
cmds.select(cl=True)
cmds.select(ikCN)
cmds.select(jL[2], add=True)
cmds.orientConstraint(mo=True)



#NOW the IK is set up as an IK with pole vector and stuff    with      LOCATORS IN ALL THE fk groups with their orient constraints
#also by now the fk locators should be set up under their respective grounds and have their constraints all thats needed is the ones for the ik i think


#Next I need to group and set up the locators and and constraints  and enumerations or and scripts 







#Set up the locator for the ik tracking
ikLN = ikG.replace('group', '_loc')
cmds.spaceLocator(n = ikLN, p = (0, 0, 0))
cmds.xform(ikLN, ws =True, t = ikGL)
locA.append(ikLN)

#freeze the loc now that its in place of the ik control group
cmds.select(cl=True)
cmds.select(ikLN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)

#now group zero rotations and freeze
cmds.parent(ikLN, ikCG)
cmds.setAttr(ikLN + '.rotateX', 0)
cmds.setAttr(ikLN + '.rotateY', 0)
cmds.setAttr(ikLN + '.rotateZ', 0)
cmds.select(cl=True)
cmds.select(ikLN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)

#make the L Wrist joint be the parent contrainor of the constrainee ikLocator 
cmds.parentConstraint(ikLN, sA[2], mo = True)

#MAKE THE CTL ATTRIBUTES FOR FK SWITCH AND CONSTRAINTS
#selecting the ctl
cmds.select(cl=True)
cmds.select(sA[3])

#heres the two lines of code for making the attributes 
cmds.addAttr(ln='constraints', at=  'long' , defaultValue=0, minValue=0, maxValue=1, k=True )
cmds.addAttr(ln='fk_ik_switch', at=  'enum' , en = 'fk:ik', k=True )
#store these names of the attributes for later in expression
sAttr1= (sA[3]+'.fk_ik_switch') 
sAttr2= (sA[3]+'.constraints')

#deselect for good housekeeping
cmds.select(cl=True)



#QUICKLY THROW THE FINGERS INTO A GROUP THAT's snapped and frozen to the ik/ LATER ON MAKE THIS WORK FOR FOOT AND BALL
cmds.group(em =True, n=ikFinGrpN)
cmds.xform(ikFinGrpN, ws = True, sp = ikGL, rp = ikGL)
cmds.select(cl=True)
cmds.select(ikFinGrpN)
cmds.makeIdentity(apply=True, t=1, r=1, s=1)
cmds.select(cl=True)

if jL[2] == 'L_wrist':
    cmds.parent(ikFinGrpN, 'L_wrist_group')
    if cmds.objExists('L_thumb_1')
        cmds.parent('L_thumb_1_group', ikFinGrpN)
    if cmds.objExists('L_index_1')
        cmds.parent('L_index_1_group', ikFinGrpN)
    if cmds.objExists('L_middle_1')
        cmds.parent('L_middle_1_group', ikFinGrpN)
    if cmds.objExists('L_ring_1')
        cmds.parent('L_ring_1_group', ikFinGrpN)
    if cmds.objExists('L_pinky_1')
        cmds.parent('L_pinky_1_group', ikFinGrpN)
    else:
        pass

if jL[2] == 'R_wrist':
    cmds.parent(ikFinGrpN, 'L_wrist_group')
    if cmds.objExists('R_thumb_1')
        cmds.parent('R_thumb_1_group', ikFinGrpN)
    if cmds.objExists('R_index_1')
        cmds.parent('R_index_1_group', ikFinGrpN)
    if cmds.objExists('R_middle_1')
        cmds.parent('R_middle_1_group', ikFinGrpN)
    if cmds.objExists('R_ring_1')
        cmds.parent('R_ring_1_group', ikFinGrpN)
    if cmds.objExists('R_pinky_1')
        cmds.parent('R_pinky_1_group', ikFinGrpN)
    else:
        pass



#THEN MAKE THE AND EXPRESSIONS and GLOBAL PROC and then we should be done




#but first lets make the strings for this
#name for the expression using this string
eN1 = (locPre + '_constraints')

#this needs fixing later i had to swap the orient and parents per the joint array because it filled up backwards for some reason starting at the wrist then going to the shoulder
constraintsES = ( (jL[0] + '_parentConstraint1.' + ctlA[0] + 'W0 = ! ' + sA[3] + '.constraints;') + '\n' +
(jL[1] + '_parentConstraint1.' + ctlA[1] + 'W0 = ! ' + sA[3] + '.constraints;') + '\n' +
(jL[2] + '_orientConstraint1.' + ctlA[2] + 'W0 = ! ' + sA[3] + '.constraints;') + '\n' +
(ikN + '_pointConstraint1.' + ikCN + 'W0 = ' + sA[3] + '.constraints;') + '\n' +
(jL[2] + '_orientConstraint1.' + ikCN + 'W1 = ' + sA[3] + '.constraints;')+ '\n' +
(ikN + '.ikBlend = '+ sA[3] + '.constraints;'))
#end of this string






#quickly store a var with the name of the proc script name for the fkikES
eN2 = locPre.replace('switch', 'ik_fk_switch_node_script')
sN = (locPre + '_Node()')
#save out spaces for indent because apparently ill need to for this
indent1 = ('    ')
indent2 = ('        ')
indent3 = ('            ')

#here goes the biggest string ever for the proc script
globalProcES =( ('global proc ' + sN + '{') + '\n' + 
(indent1 + 'int $switchDetect = `getAttr ' + sAttr1 + '`;') + '\n' + 
(indent1 + 'if ($switchDetect == 0)') + '\n' +
(indent2 + '{') + '\n' +
(indent3 + 'print("fk is on");') + '\n' +

(indent3 + 'float $shoulderRotateX = `getAttr ' + locA[0] + '.rotateX`;') + '\n' +
(indent3 + 'float $shoulderRotateY = `getAttr ' + locA[0] + '.rotateY`;') + '\n' +
(indent3 + 'float $shoulderRotateZ = `getAttr ' + locA[0] + '.rotateZ`;') + '\n' +
(indent3 + 'setAttr ' + jL[2] + '.rotateX ' + '$shoulderRotateX;') + '\n' +
(indent3 + 'setAttr ' + jL[2] + '.rotateY ' + '$shoulderRotateY;') + '\n' +
(indent3 + 'setAttr ' + jL[2] + '.rotateZ ' + '$shoulderRotateZ;') + '\n' +

(indent3 + 'float $elbowRotateX = `getAttr ' + locA[1] + '.rotateX`;') + '\n' +
(indent3 + 'float $elbowRotateY = `getAttr ' + locA[1] + '.rotateY`;') + '\n' +
(indent3 + 'float $elbowRotateZ = `getAttr ' + locA[1] + '.rotateZ`;') + '\n' +
(indent3 + 'setAttr ' + jL[1] + '.rotateX ' + '$elbowRotateX;') + '\n' +
(indent3 + 'setAttr ' + jL[1] + '.rotateY ' + '$elbowRotateY;') + '\n' +
(indent3 + 'setAttr ' + jL[1] + '.rotateZ ' + '$elbowRotateZ;') + '\n' +

(indent3 + 'float $wristRotateX = `getAttr ' + locA[2] + '.rotateX`;') + '\n' +
(indent3 + 'float $wristRotateY = `getAttr ' + locA[2] + '.rotateY`;') + '\n' +
(indent3 + 'float $wristRotateZ = `getAttr ' + locA[2] + '.rotateZ`;') + '\n' +
(indent3 + 'setAttr ' + jL[0] + '.rotateX ' + '$wristRotateX;') + '\n' +
(indent3 + 'setAttr ' + jL[0] + '.rotateY ' + '$wristRotateY;') + '\n' +
(indent3 + 'setAttr ' + jL[0] + '.rotateZ ' + '$wristRotateZ;') + '\n' +

(indent3 + 'setAttr ' + ikCN + '.visibility' + ' 0;') + '\n' +
(indent3 + 'setAttr ' + pvNN + '.visibility' + ' 0;') + '\n' +
(indent3 + 'setAttr ' + jL[2] + '_ctl.visibility' + ' 1;') + '\n' +
(indent3 + 'setAttr ' + jL[1] + '_ctl.visibility' + ' 1;') + '\n' +
(indent3 + 'setAttr ' + jL[0] + '_ctl.visibility' + ' 1;') + '\n' +

(indent3 + 'setAttr ' + sA[3] + '.constraints' + ' 0;') + '\n' +
(indent2 + '}') + '\n' +


(indent1 + 'if ($switchDetect == 1)') + '\n' +
(indent2 + '{') + '\n' +
(indent3 + 'print("IK is on");') + '\n' +

(indent3 + 'float $ikMoveX = `getAttr ' + locA[3] + '.translateX' + '`;') + '\n' +
(indent3 + 'float $ikMoveY = `getAttr ' + locA[3] + '.translateY' + '`;') + '\n' +
(indent3 + 'float $ikMoveZ = `getAttr ' + locA[3] + '.translateZ' + '`;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.translateX ' + '$ikMoveX;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.translateY ' + '$ikMoveY;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.translateZ ' + '$ikMoveZ;') + '\n' +

(indent3 + 'float $ikLocRotateX = `getAttr ' + locA[3] + '.rotateX' + '`;') + '\n' +
(indent3 + 'float $ikLocRotateY = `getAttr ' + locA[3] + '.rotateY' + '`;') + '\n' +
(indent3 + 'float $ikLocRotateZ = `getAttr ' + locA[3] + '.rotateZ' + '`;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.rotateX ' + '$ikLocRotateX;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.rotateY ' + '$ikLocRotateY;') + '\n' +
(indent3 + 'setAttr ' + ikCN + '.rotateZ ' + '$ikLocRotateZ;') + '\n' +

(indent3 + 'setAttr ' + ikCN + '.visibility' + ' 1;') + '\n' +
(indent3 + 'setAttr ' + pvNN + '.visibility' + ' 1;') + '\n' +
(indent3 + 'setAttr ' + jL[2] + '_ctl.visibility' + ' 0;') + '\n' +
(indent3 + 'setAttr ' + jL[1] + '_ctl.visibility' + ' 0;') + '\n' +
(indent3 + 'setAttr ' + jL[0] + '_ctl.visibility' + ' 0;') + '\n' +


(indent3 + 'setAttr ' + (sA[3] + '.constraints') + ' 1;') + '\n' +
(indent2 + '}') + '\n' +('}'))

#thats the end of this string



#the connecting expression
eN3 = (locPre + '_ik_fk_switch')
fkIkES = ( 'int $index = ` scriptJob - attributeChange "' + sAttr1 + '" "' +  sN + '" `;')
#end of this string

#then lets make them
#well go in order the strings were made above
cmds.expression(s = constraintsES, n = eN1)
cmds.scriptNode(bs = globalProcES, n = eN2, stp ='mel')
cmds.expression(s = fkIkES, n = eN3)


##
##THIS MIGHT BE DONE NOW THATS LEFT IS TO TEST IT OUT AND DEBUGG
##