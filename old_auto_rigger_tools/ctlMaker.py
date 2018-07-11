import maya.cmds as cmds


def makeCube():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\cube.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'curve1', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	
	cmds.select(selectArray)

def makeSphere():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\sphere.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'sphere1', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )

	cmds.select(selectArray)
def makeCircle():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\circle.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'nurbsCircle1', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)

def makeBase():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\Base_ctl_curve.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'base_ctl', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)

def makeDumbell():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\clav_ctl_curve.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'curve1', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)

def makeFoot():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\Foot.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'curve1', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)

def makeHead():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\head_ctl_curve.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'head_ctl', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)

def makeDiamond():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\diamond_curve.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'diamond_curve', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)




def makeFinger():



	jointArray = cmds.ls( sl = True )
	selectArray = []

	for ctlLoc in jointArray:
		 print(ctlLoc)
		 ctlName = (ctlLoc + "_ctl")
		 ctlGroup = (ctlLoc + "_group")
		 selectArray.append(ctlName)
		 print (ctlName)
		 print (selectArray)
		 jointLocation = cmds.xform( ctlLoc, q = 1, ws = 1, t = 1)
		 jointOrientX = cmds.getAttr(ctlLoc + ".jointOrientX")
		 jointOrientY = cmds.getAttr(ctlLoc + ".jointOrientY")
		 jointOrientZ = cmds.getAttr(ctlLoc + ".jointOrientZ")
		 ctlTX = (ctlName + ".translateX")
		 ctlTY = (ctlName + ".translateY")
		 ctlTZ = (ctlName + ".translateZ")
		 ctlRX = (ctlGroup + ".rotateX")
		 ctlRY = (ctlGroup + ".rotateY")
		 ctlRZ = (ctlGroup + ".rotateZ")
		 
		 cmds.file( 'D:\Users\BStephen6\Desktop\Finger_ctl_curve.mb', i=True )
		 
		 #cmds.namespace( set=':' )
		 #cmds.namespace( rm='cube' )
		 cmds.rename( 'finger_ctl', ctlName )

		 
		 cmds.xform(ctlName, ws = True, t = jointLocation)
		 
		 cmds.makeIdentity(ctlName, apply=True, t=1, r=1, s=1)
		 
		 cmds.group( ctlName, n = ctlGroup )
		 
		 cmds.makeIdentity(apply=True, t=1, r=1, s=1)
		 
		 cmds.xform(ctlGroup, ws = True, sp = jointLocation, rp = jointLocation)
		 
		 cmds.setAttr( ctlRX, jointOrientX )
		 cmds.setAttr( ctlRY, jointOrientY )
		 cmds.setAttr( ctlRZ, jointOrientZ )
	cmds.select(selectArray)
