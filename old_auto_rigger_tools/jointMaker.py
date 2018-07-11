import maya.cmds as cmds


def makeJoints():
	locArray = cmds.ls ( type = 'locator' )
	jointArray = []
	
	for jointPlace in locArray:
		print (jointPlace)
		locatorUp = jointPlace.replace("Shape", "")
		print (locatorUp)
		jointLocation = cmds.xform( locatorUp, q = 1, ws = 1, rp = 1)
		jointRotationX = cmds.getAttr(locatorUp + ".rotateX")
		jointRotationY = cmds.getAttr(locatorUp + ".rotateY")
		jointRotationZ = cmds.getAttr(locatorUp + ".rotateZ")
		newName = locatorUp.replace("_locator", "")
		jointArray.append(newName)
	   
		cmds.joint( n= newName, p = jointLocation)
		cmds.setAttr ((newName + ".jointOrientX"), jointRotationX)
		cmds.setAttr ((newName + ".jointOrientY"), jointRotationY)
		cmds.setAttr ((newName + ".jointOrientZ"), jointRotationZ)
		cmds.select(clear=True)
		cmds.delete(locatorUp) 
	
	for name in jointArray:
		if name == "L_ankle":
			cmds.parent( 'L_ankle', 'L_knee' )
		elif name == "L_knee":
			cmds.parent( 'L_knee', 'L_thigh' )
		elif name == "L_thigh":
			cmds.parent( 'L_thigh', 'hip' )
		elif name == "hip":
			cmds.parent( 'hip', 'root' )
		elif name == "root":
			cmds.parent( 'root', 'base' )
		elif name == "spine_1":
			cmds.parent( 'spine_1', 'root' )
		elif name == "spine_2":
			cmds.parent( 'spine_2', 'spine_1' )
		elif name == "spine_3":
			cmds.parent( 'spine_3', 'spine_2' )
		elif name == "L_clav":
			cmds.parent( 'L_clav', 'spine_3' )
		elif name == "L_shoulder":
			cmds.parent( 'L_shoulder', 'L_clav' )
		elif name == "L_elbow":
			cmds.parent( 'L_elbow', 'L_shoulder' )
		elif name == "L_wrist":
			cmds.parent( 'L_wrist', 'L_elbow' )
		elif name == "L_thumb_1":
			cmds.parent('L_thumb_1','L_wrist')
		elif name == "L_thumb_2":
			cmds.parent('L_thumb_2','L_thumb_1')
		elif name == "L_thumb_3":
			cmds.parent('L_thumb_3','L_thumb_2')
		elif name == "L_index_1":
			cmds.parent('L_index_1','L_wrist')
		elif name == "L_index_2":
			cmds.parent('L_index_2','L_index_1')
		elif name == "L_index_3":
			cmds.parent('L_index_3','L_index_2')
		elif name == "L_middle_1":
			cmds.parent('L_middle_1','L_wrist')
		elif name == "L_middle_2":
			cmds.parent('L_middle_2','L_middle_1')
		elif name == "L_middle_3":
			cmds.parent('L_middle_3','L_middle_2')
		elif name == "L_ring_1":
			cmds.parent('L_ring_1','L_wrist')
		elif name == "L_ring_2":
			cmds.parent('L_ring_2','L_ring_1')
		elif name == "L_ring_3":
			cmds.parent('L_ring_3','L_ring_2')
		elif name == "L_pinky_1":
			cmds.parent('L_pinky_1','L_wrist')
		elif name == "L_pinky_2":
			cmds.parent('L_pinky_2','L_pinky_1')
		elif name == "L_pinky_3":
			cmds.parent('L_pinky_3','L_pinky_2')
		elif name == "neck":
			cmds.parent( 'neck', 'spine_3' )
		elif name == "head":
			cmds.parent( 'head', 'neck' )
		else:
			print(name + 'DID NOT GET PUT IN THE TREE PROPERLY')
			continue
	if cmds.objExists('L_thigh'):
		cmds.mirrorJoint('L_thigh', mirrorYZ = True, mirrorBehavior= True, searchReplace =('L_', 'R_') )
	else:
		pass
	if cmds.objExists('L_thigh'):
		cmds.mirrorJoint('L_clav', mirrorYZ = True, mirrorBehavior= True, searchReplace =('L_', 'R_') )
	else:
		pass
