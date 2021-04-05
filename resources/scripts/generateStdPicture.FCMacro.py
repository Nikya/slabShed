"""

	Part of Slab Shed Project 
	
	To export a standard picture of a Slab or a Shed from FreeCad

	Use:
	- Import this script as FreeCad Macro (generateSlabShedStdPicture)
	- Select the object to export in the construction tree
	- Execute this macro
	Result: 
	- 2 pictures are available into the parent folder of te FreeCad file
	- In recomanded size : 480x360 4:3
	- Now keep only expected file and rename it (See CONTRIBUTING file)
"""

import FreeCAD

# 2 possible output files
filePathSlab = '../slab_renameMeColl_slabName.png'
filePathShed = '../shed_99_88x77_renameMeColl_shedName.png'

# Others
fileComment = 'Part of the Slab Shed Project\nhttps://github.com/Nikya/slabShed'

# Set 3D view to Isometric
Gui.activeDocument().activeView().viewIsometric()

# Fit Zoom to selected Part object
FreeCADGui.SendMsgToActiveView('ViewSelection')

# Save 2 files 
Gui.activeDocument().activeView().saveImage(filePathSlab,480,360,'Current',fileComment)
Gui.activeDocument().activeView().saveImage(filePathShed,480,360,'Current',fileComment)

# It's done!
print("File exported " + filePathSlab)
print("File exported " + filePathShed)