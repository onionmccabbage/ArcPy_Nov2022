import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex06'
arcpy.env.overwriteOutput = True

fc = 'cities.shp'

# check if a shape exists
if arcpy.Exists(fc):
    myshp = arcpy.da.Describe(fc)
    # we dont get any code help when trying to show the members of a structure
    print(myshp['datasetType'])
    print(myshp['file'])
    print(myshp['shapeType'])
    print(myshp['spatialReference'])

