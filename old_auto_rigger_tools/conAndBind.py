import maya.cmds as cmds

def conAndBinding():

	mesh= cmds.ls(sl=True)
	
	
	if cmds.objExists('L_ankle_group'):	
		cmds.parent( 'L_ankle_group', 'L_knee_ctl' )
	else: 
		pass
	if cmds.objExists('L_knee_group'):
		cmds.parent( 'L_knee_group', 'L_thigh_ctl' )
	else: 
		pass
	if cmds.objExists('L_thigh_group'):
		cmds.parent( 'L_thigh_group', 'hip_ctl' )
	else: 
		pass
	if cmds.objExists('R_ankle_group'):
		cmds.parent( 'R_ankle_group', 'R_knee_ctl' )
	else: 
		pass
	if cmds.objExists('R_knee_group'):	
		cmds.parent( 'R_knee_group', 'R_thigh_ctl' )
	else: 
		pass
	if cmds.objExists('R_thigh_group'):	
		cmds.parent( 'R_thigh_group', 'hip_ctl' )
	else: 
		pass

	if cmds.objExists('L_pinky_3_group'):
		cmds.parent( 'L_pinky_3_group', 'L_pinky_2_ctl' )
	else:
		pass
	if cmds.objExists('L_pinky_2_group'):
		cmds.parent( 'L_pinky_2_group', 'L_pinky_1_ctl' )
	else:
		pass
	if cmds.objExists('L_pinky_1_group'):
		cmds.parent( 'L_pinky_1_group', 'L_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('L_ring_3_group'):
		cmds.parent( 'L_ring_3_group', 'L_ring_2_ctl' )
	else:
		pass
	if cmds.objExists('L_ring_2_group'):
		cmds.parent( 'L_ring_2_group', 'L_ring_1_ctl' )
	else:
		pass
	if cmds.objExists('L_ring_1_group'):
		cmds.parent( 'L_ring_1_group', 'L_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('L_middle_3_group'):
		cmds.parent( 'L_middle_3_group', 'L_middle_2_ctl' )
	else:
		pass
	if cmds.objExists('L_middle_2_group'):
		cmds.parent( 'L_middle_2_group', 'L_middle_1_ctl' )
	else:
		pass
	if cmds.objExists('L_middle_1_group'):
		cmds.parent( 'L_middle_1_group', 'L_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('L_index_3_group'):
		cmds.parent( 'L_index_3_group', 'L_index_2_ctl' )
	else:
		pass
	if cmds.objExists('L_index_2_group'):
		cmds.parent( 'L_index_2_group', 'L_index_1_ctl' )
	else:
		pass
	if cmds.objExists('L_index_1_group'):
		cmds.parent( 'L_index_1_group', 'L_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('L_thumb_3_group'):
		cmds.parent( 'L_thumb_3_group', 'L_thumb_2_ctl' )
	else:
		pass
	if cmds.objExists('L_thumb_2_group'):
		cmds.parent( 'L_thumb_2_group', 'L_thumb_1_ctl' )
	else:
		pass
	if cmds.objExists('L_thumb_1_group'):
		cmds.parent( 'L_thumb_1_group', 'L_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('L_wrist_group'):
		cmds.parent( 'L_wrist_group', 'L_elbow_ctl' )
	else:
		pass
	if cmds.objExists('L_elbow_group'):
		cmds.parent( 'L_elbow_group', 'L_shoulder_ctl' )
	else:
		pass
	if cmds.objExists('L_shoulder_group'):
		cmds.parent( 'L_shoulder_group', 'L_clav_ctl' )
	else:
		pass
	if cmds.objExists('L_clav_group'):
		cmds.parent( 'L_clav_group', 'spine_3_ctl' )
	else:
		pass
	
	if cmds.objExists('R_pinky_3_group'):
		cmds.parent( 'R_pinky_3_group', 'R_pinky_2_ctl' )
	else:
		pass
	if cmds.objExists('R_pinky_2_group'):
		cmds.parent( 'R_pinky_2_group', 'R_pinky_1_ctl' )
	else:
		pass
	if cmds.objExists('R_pinky_1_group'):
		cmds.parent( 'R_pinky_1_group', 'R_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('R_ring_3_group'):
		cmds.parent( 'R_ring_3_group', 'R_ring_2_ctl' )
	else:
		pass
	if cmds.objExists('R_ring_2_group'):
		cmds.parent( 'R_ring_2_group', 'R_ring_1_ctl' )
	else:
		pass
	if cmds.objExists('R_ring_1_group'):
		cmds.parent( 'R_ring_1_group', 'R_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('R_middle_3_group'):
		cmds.parent( 'R_middle_3_group', 'R_middle_2_ctl' )
	else:
		pass
	if cmds.objExists('R_middle_2_group'):
		cmds.parent( 'R_middle_2_group', 'R_middle_1_ctl' )
	else:
		pass
	if cmds.objExists('R_middle_1_group'):
		cmds.parent( 'R_middle_1_group', 'R_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('R_index_3_group'):
		cmds.parent( 'R_index_3_group', 'R_index_2_ctl' )
	else:
		pass
	if cmds.objExists('R_index_2_group'):
		cmds.parent( 'R_index_2_group', 'R_index_1_ctl' )
	else:
		pass
	if cmds.objExists('R_index_1_group'):
		cmds.parent( 'R_index_1_group', 'R_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('R_thumb_3_group'):
		cmds.parent( 'R_thumb_3_group', 'R_thumb_2_ctl' )
	else:
		pass
	if cmds.objExists('R_thumb_2_group'):
		cmds.parent( 'R_thumb_2_group', 'R_thumb_1_ctl' )
	else:
		pass
	if cmds.objExists('R_thumb_1_group'):
		cmds.parent( 'R_thumb_1_group', 'R_wrist_ctl' )
	else:
		pass
	
	if cmds.objExists('R_wrist_group'):
		cmds.parent( 'R_wrist_group', 'R_elbow_ctl' )
	else:
		pass
	if cmds.objExists('R_elbow_group'):
		cmds.parent( 'R_elbow_group', 'R_shoulder_ctl' )
	else:
		pass
	if cmds.objExists('R_shoulder_group'):
		cmds.parent( 'R_shoulder_group', 'R_clav_ctl' )
	else:
		pass
	if cmds.objExists('R_clav_group'):
		cmds.parent( 'R_clav_group', 'spine_3_ctl' )
	else:
		pass
	
	if cmds.objExists('head_group'):
		cmds.parent( 'head_group', 'neck_ctl' )
	else:
		pass
	if cmds.objExists('neck_group'):
		cmds.parent( 'neck_group', 'spine_3_ctl' )
	else:
		pass
	
	if cmds.objExists('spine_3_group'):
		cmds.parent( 'spine_3_group', 'spine_2_ctl' )
	else:
		pass
	if cmds.objExists('spine_2_group'):
		cmds.parent( 'spine_2_group', 'spine_1_ctl' )
	else:
		pass
	if cmds.objExists('spine_1_group'):
		cmds.parent( 'spine_1_group', 'root_ctl' )
	else:
		pass

	if cmds.objExists('tail_1_group'):
		cmds.parent( 'tail_1_group', 'hip_ctl' )
	else:
		pass
	if cmds.objExists('hip_group'):
		cmds.parent( 'hip_group', 'root_ctl' )
	else:
		pass
	if cmds.objExists('root_group'):
		cmds.parent( 'root_group', 'base_ctl' )
	else:
		pass


	jointArray = cmds.ls( typ='joint')
	print(jointArray)
	for joints in jointArray:
		constrainor = (joints + "_ctl")
		if cmds.objExists(constrainor):
			cmds.parentConstraint( constrainor, joints, mo=True)
		else:
			pass


	cmds.skinCluster( 'base', mesh, dr=4, mi=2)
	cmds.select(mesh)
	cmds.skinCluster(edit=True,ri='base')
	cmds.skinCluster(edit=True,ri='root')

