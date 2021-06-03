"""
	Part of Slab Shed Project.
	
	A macro for FreeCad to bring some utils for the Slab Shed project.
"""

from PySide import QtGui
import os.path
from os import path

################################################################################
# region META DATA

__Name__ = 'Slab Shed utils for FreeCad' # Suggested macro name : SlabShedUtilsForFreeCad
__MeTag__ = '\nSlabShedUtils> '
__Comment__ = 'A FreeCad macro to provide utility for SlabShed project.'
__Author__ = 'Nikya'
__Version__ = '1.4-202105221617'
__Date__ = '2021-05-22'
__License__ = 'CreativeCommons BY-SA http://creativecommons.org/licenses/by-sa/4.0'
__Web__ = 'https://github.com/Nikya/slabShed'
__Help__ = """
Install:
- Import this script as a FreeCad Macro.

Use:
- Select the object to manage
- Execute this macro

Result: 
- One picture exported to ../resources folder

Know issues and solutions:
- Target folder nor found : close and reopen your Freecad file to force internal file paths refreshing.

See also
- The page CONTRIBUTING for more detail about project, structure and naming convention.
"""

# endregion
################################################################################
# region VARS

# Scene param path then object
paramViewPath = "User parameter:BaseApp/Preferences/View"
paramView = App.ParamGet(paramViewPath)

targetObject = None

# Scene configurations : Actual user config to save and restore after
bgUserCfgColor2 = None
bgUserCfgColor3 = None
bgUserCfgColor4 = None
bgUserCfgSimple = None
bgUserCfgGradient = None
bgUserCfgUseColorMid = None
userObjectColor = None

# Scene configurations : SlabShed values to apply
BG_SLABSHED_COLOR2 = 3038224127
BG_SLABSHED_COLOR3 = 1217785855
BG_SLABSHED_COLOR4 = 1913239551
BG_SLABSHED_SIMPLE = False
BG_SLABSHED_GRADIENT = True
BG_SLABSHED_USECOLORMID = True
SLAB_COLOR = (0.0, 0.76, 0.82, 0.0)
SHED_COLOR = (0.37, 0.99, 0.55, 0.0)

# output picture file
IMAGE_FILE_FOLDER = 'resources'
IMAGE_FILE_COMMENT = 'Part of the Slab Shed Project\nhttps://github.com/Nikya/slabShed'
IMAGE_FILE_WIDTH=480
IMAGE_FILE_HIGHT=360

fileNaming = (None, None, None)

# endregion
################################################################################
# region FUNCTIONS 

def warnAndFail(msg):
	QtGui.QMessageBox.warning(None, __Name__, msg + "\n" + __Help__)
	FreeCAD.Console.PrintWarning(__MeTag__ + msg)
	raise UserWarning(__MeTag__ + msg)

def prerequisitesCheck():
	global targetObject

	# Count object, to warn and stop if no one is selected
	if len(Gui.Selection.getSelection()) < 1:
		warnAndFail("No object selected !")

	targetObject = Gui.Selection.getSelection()[0]

	# Check the existence of target paths
	if path.exists(os.path.join('..', IMAGE_FILE_FOLDER)) != True:
		warnAndFail("The upper folder '{}' is not found!".format(IMAGE_FILE_FOLDER))

def askfileNaming():
	"""Ask for output file naming parts"""
	documentNameCurrent = App.ActiveDocument.Label

	msg = 'Prefix name'
	suggest = 'slab-shed_6_2x3'
	ask1, okDialog = QtGui.QInputDialog.getText(None, __Name__, msg, QtGui.QLineEdit.Normal, suggest)
	if okDialog == False: raise UserWarning("Cancel")

	msg = 'Collection name'
	suggest = documentNameCurrent
	ask2, okDialog = QtGui.QInputDialog.getText(None, __Name__, msg, QtGui.QLineEdit.Normal, suggest)
	if okDialog == False: raise UserWarning("Cancel")

	msg = 'Object name'
	suggest = ''
	ask3, okDialog = QtGui.QInputDialog.getText(None, __Name__, msg, QtGui.QLineEdit.Normal, suggest)
	if okDialog == False: raise UserWarning("Cancel")
	
	global fileNaming
	fileNaming = (ask1, ask2, ask3)

def stagingSave():
	"""Extract the user scene configuration"""
	global bgUserCfgColor2, bgUserCfgColor3, bgUserCfgColor4, bgUserCfgSimple, bgUserCfgGradient, bgUserCfgUseColorMid, userObjectColor

	bgUserCfgColor2 = paramView.GetUnsigned("BackgroundColor2")
	bgUserCfgColor3 = paramView.GetUnsigned("BackgroundColor3")
	bgUserCfgColor4 = paramView.GetUnsigned("BackgroundColor4")
	bgUserCfgSimple = paramView.GetBool("Simple")
	bgUserCfgGradient = paramView.GetBool("Gradient")
	bgUserCfgUseColorMid = paramView.GetBool("UseBackgroundColorMid")
	userObjectColor = targetObject.ViewObject.ShapeColor

def stagingMake():
	"""Setup the SlabShed scene configuration"""
	paramView.SetUnsigned("BackgroundColor2", BG_SLABSHED_COLOR2)
	paramView.SetUnsigned("BackgroundColor3", BG_SLABSHED_COLOR3)
	paramView.SetUnsigned("BackgroundColor4", BG_SLABSHED_COLOR4)
	paramView.SetBool("Simple", BG_SLABSHED_SIMPLE)
	paramView.SetBool("Gradient", BG_SLABSHED_GRADIENT)
	paramView.SetBool("UseBackgroundColorMid", BG_SLABSHED_USECOLORMID)

	# Setup the 3D view to Isometric, Orthographic, fit zoom to selected, draw style wire+shadow
	Gui.activeDocument().activeView().viewIsometric()
	Gui.activeDocument().activeView().setCameraType("Orthographic")
	FreeCADGui.SendMsgToActiveView('ViewSelection')
	Gui.runCommand('Std_DrawStyle',6)
	
	# Change object color 
	if fileNaming[0] == "slab":
		targetObject.ViewObject.ShapeColor = SLAB_COLOR
	else:
		targetObject.ViewObject.ShapeColor = SHED_COLOR

	Gui.Selection.clearSelection()
	Gui.runCommand('Std_DrawStyle',6)

def stagingRestore():
	"""Restore the user scene configuration"""
	if bgUserCfgColor2 == 0 or bgUserCfgColor3 == 0:
		paramView.RemUnsigned("BackgroundColor2")
		paramView.RemUnsigned("BackgroundColor3")
		paramView.RemUnsigned("BackgroundColor4")
		paramView.RemBool("Simple")
		paramView.RemBool("Gradient")
		paramView.RemBool("UseBackgroundColorMid")
	else: # Restore user preferences
		paramView.SetUnsigned("BackgroundColor2", bgUserCfgColor2)
		paramView.SetUnsigned("BackgroundColor3", bgUserCfgColor3)
		paramView.SetUnsigned("BackgroundColor4", bgUserCfgColor4)
		paramView.SetBool("Simple", bgUserCfgSimple)
		paramView.SetBool("Gradient", bgUserCfgGradient)
		paramView.SetBool("UseBackgroundColorMid", bgUserCfgUseColorMid)
	
	targetObject.ViewObject.ShapeColor = userObjectColor

def takePicture():
	"""Take a picture of the current selected object"""
	fileName = '_'.join(fileNaming)
	imageFileFullpath = os.path.join('..', IMAGE_FILE_FOLDER, fileName + ".png") 

	FreeCAD.Console.PrintMessage(__MeTag__ + "Save an image to file : '{}'".format(imageFileFullpath))

	try:
		Gui.activeDocument().activeView().saveImage(imageFileFullpath, IMAGE_FILE_WIDTH, IMAGE_FILE_HIGHT, 'Current', IMAGE_FILE_COMMENT)
	except:
		eMsg = "Fail to generate image file : " + sys.exc_info()[0]
		FreeCAD.Console.PrintError(__MeTag__ + eMsg)
		raise

# endregion
################################################################################
# region Main

FreeCAD.Console.PrintMessage(__MeTag__ + "Started")

prerequisitesCheck()
askfileNaming()
stagingSave()
stagingMake()
takePicture()
stagingRestore()

FreeCAD.Console.PrintMessage(__MeTag__ + "Done!")

# endregion