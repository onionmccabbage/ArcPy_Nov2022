import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex06'
arcpy.env.overwriteOutput = True

fieldlist = arcpy.ListFields('cities.shp')
# iterate over the fields
for field in fieldlist:
    print( 'The field name {} has field type {}'.format(field.name, field.type) )
    # print( f'The field name {field.name} has field type {field.type}' )