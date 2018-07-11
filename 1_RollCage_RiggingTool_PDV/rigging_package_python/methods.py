#imported modules

import maya.cmds as cmds
import maya.OpenMaya as openMaya
import pymel.core as pm

#global variables

jArray = []

# classes set up

#base class item will be the super class
#stores basic attributes that every maya item has and


class Item(object):
	def __init__(self, name):
		
		#on creation takes and stores the current name and translate, rotate, and scale information from the object with
		#the corresponding name in maya
		self.name = str(name)
		
		#sets arrays to be used in the storing of object information using xfrom to store the vector3 array
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, t = 1)
		
		self.translateX = attrArray[0]
		self.translateY = attrArray[1]
		self.translateZ = attrArray[2]
		
		#same as the small block above
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, ro = 1)
		
		self.rotateX = attrArray[0]
		self.rotateY = attrArray[1]
		self.rotateZ = attrArray[2]
		
		#and again..
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, s = 1)
		
		self.scaleX = attrArray[0]
		self.scaleY = attrArray[1]
		self.scaleZ = attrArray[2]
		
		#finally setting the object attribute with getAttr in maya to store the visibility value
		self.visibility = cmds.getAttr((self.name) + '.visibility')
	
		
		
		
	#SIMPLE METHODS FOR SELF
		

	#basically repeats the init function to update the base attributes so I did not feel the need to comment this block further (see above for more details)
	def updateAttrs(self):
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, t = 1)
		
		self.translateX = attrArray[0]
		self.translateY = attrArray[1]
		self.translateZ = attrArray[2]
		
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, ro = 1)
		
		self.rotateX = attrArray[0]
		self.rotateY = attrArray[1]
		self.rotateZ = attrArray[2]
		
		attrArray = cmds.xform( (self.name), q = 1, ws = 1, s = 1)
		
		self.scaleX = attrArray[0]
		self.scaleY = attrArray[1]
		self.scaleZ = attrArray[2]
		
		self.visibility = cmds.getAttr((self.name) + '.visibility')
	
	#Moves object to the arguement object
	#takes 1 arguements, uses self, and the item to be move to
	def moveToItem(self, x):
		#stores a vector3 using xform under itemLoc to be used in the xform command to move the object
		itemLoc = cmds.xform( str(x.name), q = 1, ws = 1, t = 1)
		cmds.xform(self.name, ws = True, t = itemLoc)
		#updates the new attribute values in the object variables
		self.updateAttrs
	
	#move to point in maya 3d space method
	#takes 1 arguements, uses self, and a vector3 array for the world space location (x)
	def moveToPoint(self, x=[]):
		#simple xform command
		cmds.xform(self, ws = True, t = x)
		#update attrs as usual
		self.updateAttrs
	
	#simple move method that takes a float or int arguement for each move axis 
	def move(self, x=0, y=0, z=0):
		#stores the arugments in an array to be used as a vector 3 to drive the movement of the object
		moveVector = [x, y, z]
		#uses the new array as a vector 3 to move the object with xform
		cmds.xform('mesh', wd = True, t = moveVector, r = True)
		#update attrs as usual
		self.updateAttrs

	#simple rotate method utilizing just setAttr, because the xform rotate doesn't seeem to influence object rotation values
	#the lack of proper rotation information on an objects maya channels is concerning for overall good housekeeping to although it's
	#more code I feel It's more appropriate (although possibly just supersticious) to keep from incurring errors down the line of the tools operation
	def rotate(self, x=0, y=0, z=0):
		#adding the new rotation values to the object's rotation values
		self.rotateX +=(x)
		self.rotateY +=(y)
		self.rotateZ +=(z)
		
		#setting the new rotation values in maya with setAttr using the object's new rotation values
		cmds.setAttr((self.name + '.rotateX'), float(self.rotateX))
		cmds.setAttr((self.name + '.rotateY'), float(self.rotateY))
		cmds.setAttr((self.name + '.rotateZ'), float(self.rotateZ))
		#update attrs as usual
		self.updateAttrs

	#simple scale Method that takes float or int arguements for each axis of scale to be used with xform scaling
	def scale(self, x=0, y=0, z=0):
		cmds.xform(str(self.name), s=(x, y, z))
		#updating attrs again
		self.updateAttrs
	
	#simple Delete Method
	def delete(self):
		#pretty self explanitory but it clears any current selection
		cmds.select(cl = True)
		#selects the object 
		cmds.select(self.name)
		#deletes the selected object
		cmds.delete()
		
	#simple Select Method
	def select(self):
		#clears current selection before selection
		cmds.select(cl = True)
		cmds.select(self.name)
	
		
	#simple rename Method
	def rename(self, name):
		cmds.rename(str(self.name), name)
		#updates object name variable value to the new name
		self.name = name
		
	# swaps the visibility attr in maya
	def visSwitch(self):
		#stores visibility as an int under the var x
		x = int(cmds.getAttr(self.name + ".visibility"))
		#if and else statements to swap visibility based on x value
		if x == 0:
			cmds.setAttr((self.name + ".visibility"), 1)
		else:
			cmds.setAttr((self.name + ".visibility"), 0)
	
	
	#simple snap pivots Method
	#takes the arguement a string arguement of x for the name of the item to be snapped to
	def snapPivsToItem(self, x):
		itemLoc = cmds.xform(x, q = 1, ws = 1, t = 1)
		cmds.xform(self, ws = True, piv = pivLoc)
	
	#simple snap pivots method that snaps specifically other item's pivots
	#like the method above this method takes an arguement (x) for a string of the name of the item whos pivots the object will be snapped to
	def snapPivsToPiv(self, x):
		pivLoc = cmds.xform( (x + '.scalePivot'), q = 1, ws = 1, t = 1)
		cmds.xform(self, ws = True, piv = pivLoc)
	
		
	
	#takes arguement of self and the to be child in string from(X)
	def parent(self, x):
		cmds.parent(self.name, str(x))
	
	#maybe redundant but Might be useful down the line
	#like the parent arguement but I takes a string for the name of the parent for the object to be under (x)
	def childUnder(self, x):
		cmds.parent(str(x), self.name)
	
	#freeze transform method, pretty self explanitory, doesn't take arguements just freezes the transforms for the object the method is called for
	def freezeTransforms(self):
		cmds.makeIdentity(self, apply=True, t=1, r=1, s=1)
	
	
		
	
	
	
#SUPER AND SUBCLASS EXAMPLES FOR WORKING ON PACKAGE
	
# if you're gunna call an init for a subclass you have to call the super's init
#class subClass(superClass):
#	def __init__(self, *args, **kwargs):
#		super(subClass, self).__init__(*args, **kwargs)
#		self.attr = attrValue
#		self.attr2 = attrValue2
#
		

		
		
		
		
		
class Joint(Item):
	def __init__(self, name, ):
		super(Joint).__init__(name)
		#store the joint orients in the object attributes
		self.jointOrientX = cmds.getAttr((self.name)+ '.jointOrientX')
		self.jointOrientY = cmds.getAttr((self.name)+ '.jointOrientY')
		self.jointOrientZ = cmds.getAttr((self.name)+ '.jointOrientZ')
	
	#orient takes three arguements, one for each axis for orientation
	def orient(self, x=0, y=0, z=0):
		#sets attribute to the arguements
		cmds.setAttr((self.name) + '.jointOrientX', x)
		cmds.setAttr((self.name) + '.jointOrientY', y)
		cmds.setAttr((self.name) + '.jointOrientZ', z)
		
	#freezes the orient of the object
	def clearOrient(self):
		cmds.makeIdentity(self, apply=True, jo=True)
		
	#runs the orient method to what the rotation is, clears rotations, 
	def orientToRotation(self):
		self.orient(self.rotateX, self.rotateY, self.rotateZ)
		self.rotateX = 0.0
		self.rotateY = 0.0
		self.rotateZ = 0.0
		
		cmds.setAttr((self.name + '.rotateX'), float(self.rotateX))
		cmds.setAttr((self.name + '.rotateY'), float(self.rotateY))
		cmds.setAttr((self.name + '.rotateZ'), float(self.rotateZ))

	
class Loc(Item):
	def __init__(self, name):
		super(Loc).__init__(name)
			
	#add group method to expidite grouping and pivot snapping while changing the name of the new group to the propper name
	#this uses the snap piv to piv function
	
	# NOTE TO SELF I double checked and this is the most simple and correct way of doing this (yes you can call string methods for an object attribute like that)
	def addGroup(self):
		newGroup = self.name.replace("_loc","_group")
		cmds.group(self.name, n=(newGroup)))
		self.snapPivsToPiv(newGroup))
		str(newGroup) = Group(str(newGroup))
		

	
	
	
class Curve(Item):
	def __init__(self, name):
	super(Curve).__init__(name)
	
	
	#add group method to expidite grouping and pivot snapping while changing the name of the new group to the propper name
	#this uses the snap piv to piv function
	def addGroup(self):
		newGroup = self.name.replace("_ctl","_group")
		cmds.group(self.name, n=(newGroup)))
		self.snapPivsToPiv(newGroup))
		str(newGroup) = Group(str(newGroup))
	
	
	#function to set a new color for the control curve
	#takes a string arguement for the name of the color the user wants their curves to be
	# the acceptable arguements
	def overideColor(self, color):
		#get all the sub control curves that make up the control curve
		ctlShapes = cmds.listRelatives( mirror, ad = True )
		#enables color overiding to be able to set the color 
		#loop to set all the controls that make up the control curve to a color

		if color == 'yellow':
			for shapes in ctlShapes:
				cmds.setAttr(shapes + '.overrideEnabled', 1)
				cmds.setAttr(shapes + '.overrideColor', 17)
		elif color == 'red':
			for shapes in ctlShapes:
				cmds.setAttr(shapes + '.overrideEnabled', 1)
				cmds.setAttr(shapes + '.overrideColor', 13)
		elif color == 'blue':
			for shapes in ctlShapes:
				cmds.setAttr(shapes + '.overrideEnabled', 1)
				cmds.setAttr(shapes + '.overrideColor', 6)
		elif color == 'green':
			for shapes in ctlShapes:
				cmds.setAttr(shapes + '.overrideEnabled', 1)
				cmds.setAttr(shapes + '.overrideColor', 14)
		elif color == 'purple':
			for shapes in ctlShapes:
				cmds.setAttr(shapes + '.overrideEnabled', 1)
				cmds.setAttr(shapes + '.overrideColor', 9)
		else:
			print('INVALID COLOR NAME! PLEASE USE A MAYA INDEX COLOR NAME!')

	

	
	
class Mesh(Item):
	def __init__(self, name):
		super(Mesh).__init__(name)
	
	#basic add group funciton like all the rest just working with another suffix for the group name
	# also uses snap pivs to piv to make for an easy group
	def addGroup(self):
		newGroup = (self.name + "_group")
		cmds.group(self.name, n=(newGroup)))
		self.snapPivsToPiv(newGroup))
		str(newGroup) = Group(str(newGroup))
		
	def deleteHistory(self):
		cmds.delete(str(self.name), ch=1)

class GroupOfItems(Item):
	#init takes a string arguement for the group name and an array of strings for the childen	
	def __init__(self, name, children = []):
	super(GroupOfItems)__init__(name)
		self.name = name
		self.children = [children]
		
	def addGroup(self, oldSuff, newSuff):
		newGroup = self.name.replace(str(oldSuff), str(newSuff))
		cmds.group(self.name, n=(newGroup)))
		self.snapPivsToPiv(newGroup))
		str(newGroup) = Group(str(newGroup))		
		
	
		
	



class IKHandle(Item):
	#init takes String arguements for Start and End Join args, floats for the vector values, by default the poles fill Zero and are optional
	def __init__(self,name, startJoint, endJoint, poleVecDriver = none, ikBlend = 1)
		super(IKHandle).__init__(name)
		self.startJoint = startJoint
		self.endJoint = endJoint
		self.poleVecDriver = poleVecDriver
		self.ikBlend = ikBlend
		
		








#BASE FUNCTIONS


#base expression function to be used to make expression code more easily in other functions
def createExpr(): 
	





#EXPRESSION FUNCTIONS
#These will take Arguements similar to the arguements for the functions they are a part of and will make it more modular
#while simultaneously less hard coded to increase ease of rigging functions















		
#RIGGING FUNCTIONS

#step 1 function import controls
#take arguement for ctl name and imports the ctl with that name
def importCtlsNClean(ctlName):
	cmds.file(str(ctlName), i=1)
	
#step 2 function change name to joint ctl
#take the name of the Ctl and joint it will be named after

def renameToJoint(obj, joint):
	x = str(obj.name)
	newName = (str(joint.name)+ "_ctl")
	cmds.rename(x, newName)

	
	
	
	
	


	
	
#Last Step of brinding skin
# the binding skin function take 5 arguements:
#base arguement is OPTIONAL and is for the name of the base joint and auto fills to 'base' if not filled
#mesh arguement is to hold the name of the mesh and must be filled in some way
#dontBind arguement is an array arguement that takes an array of joints not to be included in the skin cluster (usually the base and root but more could be needed)
#

def bindSkin(baseJoint='base', mesh, dontBind=[], dropOffRate =4, maxInfluences =2):
	cmds.skinCluster( baseJoint, mesh, dr=int(dropOffRate), mi=int(maxInfluences))
	cmds.select(mesh)
	for j in dontBind:
		cmds.skinCluster(edit=True,ri=str(j))
