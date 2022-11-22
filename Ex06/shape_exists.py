import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex06'
arcpy.env.overwriteOutput = True

# we can use logic to only run tools if there are shapes we can actually use
fc = 'cities.shp'
newfc = 'cities_copy.shp'
brokenfc = None # oops

# check if a shape exists
if arcpy.Exists(fc):
# shp_exists = arcpy.Exists('cities.shp') # we MUST include the extension (we're not in ArcGIS Pro)
    # print(shp_exists) # True  - it does exist inthis workspace
    arcpy.CopyFeatures_management(fc, newfc)

# we could also use exception handling
try:
    arcpy.CopyFeatures_management(fc, brokenfc)
except Exception as err:
    print( f'Something went wrong: {err}' )


# we can describe data structures
mylyr = arcpy.da.Describe('cities')
# print(mylyr['dataType']) # ShapeFile is one of the many key attributes within a shape file
# a shape file is a DICTIONARY - made up of key-value pairs
# we can iterate over the members of a dictionary like this
for (k, v) in mylyr.items(): # ALWAYS .items if we want everything
    print(k, v) # show the key then show the value of that key
