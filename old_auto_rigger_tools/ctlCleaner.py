import maya.cmds as cmds



def ctlCleaning():


	mirrorArray = cmds.ls(sl=True)
	print (mirrorArray)

	ctlArray = cmds.ls( type ='nurbsCurve')
		
	for center in ctlArray:
		#print(center)
		cmds.setAttr(center + '.overrideEnabled', 1)
		cmds.setAttr(center + '.overrideColor', 17)
		freezeTar = cmds.listRelatives( center, allParents=True )
		cmds.makeIdentity(freezeTar, apply=True, s=1,)
		
	for mirror in mirrorArray:
		#clear in case of dupes
		cmds.select(clear=True)
		print(mirror)
		# getting the base-est Dag object for that ctl
		ctlShapes = cmds.listRelatives( mirror, ad = True )
	   #freeze scale to its all 1,1,1,
		cmds.makeIdentity(mirror, apply=True, s=1,)
	   #creating a string for the new name of the Mirror dupe ctl
		ctlDup = mirror.replace('L_', 'R_')
	   
	   
	   #setting up some names as variables to stick into functions
		mirrorCtlGroup = mirror.replace('_ctl', '_group')
		mirrorLeftCtlGroup = ctlDup.replace('_ctl', '_group')
		ctlCurveGScalePiv = (mirrorLeftCtlGroup + ".scalePivot")
		ctlCurveGRotPiv = (mirrorLeftCtlGroup + ".rotatePivot")
	   

		#setting up some float casted numbers as variables
		ctlGroupRotateTransferXFlipper = float(1)
		ctlGroupRotateTransferYFlipper = float(-1)
		ctlGroupRotateTransferZFlipper = float(-1)


	   #dropping the _ctl to make it the mirrored joint name
		mirrorJointTarget = ctlDup.replace('_ctl', '')
	   #then getting its location in world space
		targetLocation = cmds.xform(mirrorJointTarget, q=True, ws=True, t=True)

	   #the dupe
		cmds.select(mirror)
		cmds.Duplicate( mirror)
		print('duplicated')
	   #clear selection
		cmds.select( clear = True )
		dupelicate = ( mirror + "1" )
		cmds.rename(dupelicate, ctlDup)

	   
		#parent to the world to get it out of any hierarchy for the original ctl
		cmds.parent( ctlDup, w=True )
	   #move to the center of the scene
		cmds.move(0, 0, 0, rpr =True)

		#zeroing out rotation because its probaby set the prior groups rotation onto the ctl curve after being removed
		cmds.setAttr( ctlDup + ".rotateX", 0 ) 
		cmds.setAttr( ctlDup + ".rotateY", 0 ) 
		cmds.setAttr( ctlDup + ".rotateZ", 0 ) 
		#freeze transforms
		cmds.makeIdentity(ctlDup, apply=True, t=1, r=1, s=1)
		#move to the mirrored joint location
		cmds.xform(ctlDup, ws = True, t = targetLocation)

		#Grouping the New Mirrored CTL 
		cmds.group( ctlDup, n = mirrorLeftCtlGroup )
		#Moving the group center pivot(s) to the new location 
		cmds.xform(mirrorLeftCtlGroup, ws = True, sp = targetLocation, rp = targetLocation)
		cmds.makeIdentity(ctlDup, apply=True, t=1, r=1, s=1)


		#getting the rotate values from the original ctl group and storing them as variables
		ctlGroupRotateTransferX = cmds.getAttr( mirrorCtlGroup + ".rotateX" )
		ctlGroupRotateTransferY = cmds.getAttr( mirrorCtlGroup + ".rotateY" )
		ctlGroupRotateTransferZ = cmds.getAttr( mirrorCtlGroup + ".rotateZ" )

		#multiplying the rotation values by the flip values to get the negative version for a mirroring MAKE SURE THIS IS CORRECT
		ctlGroupRotateTransferX = (ctlGroupRotateTransferX * ctlGroupRotateTransferXFlipper) 
		ctlGroupRotateTransferY = (ctlGroupRotateTransferY * ctlGroupRotateTransferYFlipper)
		ctlGroupRotateTransferZ = (ctlGroupRotateTransferZ * ctlGroupRotateTransferZFlipper)

		#Setting the new multiplied value and slapping that onto the mirrored ctl group MAKE SURE THIS IS CORRECT
		cmds.setAttr( mirrorLeftCtlGroup + ".rotateX", ctlGroupRotateTransferX)
		cmds.setAttr( mirrorLeftCtlGroup + ".rotateY", ctlGroupRotateTransferY) 
		cmds.setAttr( mirrorLeftCtlGroup + ".rotateZ", ctlGroupRotateTransferZ)


		# Set rotation of ctl group with the flipped rotation with the added 180
		print("PRE 180 Mirror control group variable is " + str(mirrorLeftCtlGroup))
		print("the mirror ctl group rotation values before adding 180 onto the X is " + str(ctlGroupRotateTransferZ) )
		cmds.setAttr(mirrorLeftCtlGroup + ".rotateX", ((ctlGroupRotateTransferX) + 180) )
		print()
		newGroupRot = cmds.getAttr(mirrorLeftCtlGroup + ".rotateX" )
		print( "added 180 to the group now the rotation is " + str(newGroupRot))
		cmds.select(cl=True)
	   #TURNING THE ROTATE AXIS SO THE MOVE MIRRORS TOO!
		#cmds.xform(ctlDup, r = True, ra = [180,0,0])
		cmds.setAttr(ctlDup + ".rotateAxisX", 180)
		
		newCtlShapes = cmds.listRelatives( ctlDup, ad = True) 

		for newShapes in newCtlShapes:
	   
			cmds.setAttr(newShapes + '.overrideEnabled', 1)
			cmds.setAttr(newShapes + '.overrideColor', 13)
	   
		for shapes in ctlShapes:
			cmds.setAttr(shapes + '.overrideEnabled', 1)
			cmds.setAttr(shapes + '.overrideColor', 6)
	   
