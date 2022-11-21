import arcpy # tell python to use the ArcPy library

# we need to tell Python it's ok to overwrite assets
arcpy.env.overwriteOutput = True # or False

# careful - we need to make sure the path is correct!
arcpy.env.workspace = 'c:/PythonPro/Ex03/Study.gdb' # point to any gdb asset we wish to use

# we will use the 'clip' too
# we can use single or double quotes
arcpy.Clip_analysis('lakes', 'basin', 'lakes_myClip')
