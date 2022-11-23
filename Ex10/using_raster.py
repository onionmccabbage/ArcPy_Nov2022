# we could write our python here
import arcpy # not needed - we are in ArcGIS!!
# also no need to set a workspace
arcpy.env.workspace = r'c:\PythonPro\Ex10'

# we can list all radters in this project
r_list = arcpy.ListRasters()
for r in r_list:
    print(r)

# using the landcover.tif
raster = 'landcover.tif'
desc   = arcpy.da.Describe(raster)
print('Raster base name is {} data type is {} ext {}'.format(desc['baseName'], desc['dataType'], desc['extension']))