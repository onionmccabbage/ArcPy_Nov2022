import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex09'
arcpy.env.overwriteOutput = True

fc = 'hawaii.shp' # this is a multipart shape

# hawaii is multip[art so the cursor needs to know the aspects we want
with arcpy.da.SearchCursor(fc, ['SHAPE@', 'OID@']) as cursor:
    for r in cursor:
        # partCount is a number - cast it to a string
        print('Feature {} has {} parts'.format( r[1],  str(r[0].partCount)  ))