"""
	Part of Slab Shed Project 
	
	To export a standard picture of a Slab or a Shed from FreeCad

	Use:
	- Import this script as FreeCad Macro (generateSlabShedStdPicture)
	- Select the object to export in the construction tree
	- Execute this macro
	Result: 
	- 2 pictures are available into the parent/resources folder of te FreeCad file
	- In recomanded size : 480x360 4:3
	- Now keep only expected file (Slab or Shed) and rename it (See CONTRIBUTING file)
"""

import FreeCAD

#####  OUTPUT FILES PROPERTIES
#  2 possible output files names
filePathSlab = '../resources/slab_myNewCollectionName_mySlabName.png'
filePathShed = '../resources/shed_99_88x77_myNewCollectionName_myShedName.png'
fileComment = 'Part of the Slab Shed Project\nhttps://github.com/Nikya/slabShed'
fileWidth=480
fileHight=360

##### FRAMING & DISPLAY
# Set 3D view to Isometric+Orthographic
Gui.activeDocument().activeView().viewIsometric()
Gui.activeDocument().activeView().setCameraType("Orthographic")
# Fit Zoom to selected Part object
FreeCADGui.SendMsgToActiveView('ViewSelection')
# TODO : Change background color, change shape color, then restore color
# Now unselect all
Gui.Selection.clearSelection()

##### GENERATE
Gui.activeDocument().activeView().saveImage(filePathSlab, fileWidth, fileHight, 'Current', fileComment)
Gui.activeDocument().activeView().saveImage(filePathShed, fileWidth, fileHight, 'Current', fileComment)

# DONE!
print("File exported " + filePathSlab)
print("File exported " + filePathShed)