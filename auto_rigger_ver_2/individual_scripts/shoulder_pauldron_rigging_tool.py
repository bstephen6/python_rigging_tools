#shoulder pauldron rigger tool
import maya.cmds as cmds
import maya.mel as mel


#---------------------------- functions to be used ---------------------------

#base pop-up window function to be used down the line to call windows for..
#.. various reasons
def basicPopUp(*args):

#function to make a pop up to que selecting the pauldron mesh then run..
# .. a skin bind to the the pauldron joint 
def selectPauldronPopUp( *args):


#a basic function to create a locator between two joints
def locAlongJointChain( _sel, ): 

#--------------------------- actual tool starts here -------------------------

#start of with a selection of the clav and shoulder (or possibly hips and thigh?? check on this later)..
#.. ps the last item should be the elbow.
sel = cmds.ls(sl=True)

for index, x in enumerate(sel):
    if index == 0:
        jName = cmds.joint()
        cmds.joint

#--------------------------- UI and Window Elements --------------------------
