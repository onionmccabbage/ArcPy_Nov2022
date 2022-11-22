import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex06'
arcpy.env.overwriteOutput = True

# we can introspect the current project to find all the feature classes
fclist = arcpy.ListFeatureClasses()
# print(fclist)
# we can iterate over the feature classes
for fc in fclist:
    fcdesc = arcpy.da.Describe(fc)
    dtype  = fcdesc['dataType']
    name   = fcdesc['name']
    stype  = fcdesc['shapeType']
    # we can format these in a nicely printed statement (using Python formatting)
    # we use curly brackets as placeholders
    # print( 'The {} called {} is a shape type {}'.format(dtype, name, stype) )
    # print( 'The shape type {2} is in {0} called {1}'.format(dtype, name, stype) )
    # or
    print( f'The {dtype} called {name} is a shape type {stype}' )

