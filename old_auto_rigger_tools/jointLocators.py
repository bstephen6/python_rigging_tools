import maya.cmds as cmds


def importLocators():

	cmds.file( "D:\Users\BStephen6\Desktop\joint_locators.ma", i=True )

#cmds.namespace( set = ':' ) 
#cmds.namespace( rm = 'jointLocators' ) 