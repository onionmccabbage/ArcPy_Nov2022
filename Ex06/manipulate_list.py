import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex06'
arcpy.env.overwriteOutput = True

# the variable fclist is a pointer at the project, NOT the project
fclist = arcpy.ListFeatureClasses()

# the feature class list is an indexed collection
print(fclist[0]) # amtrack
print(fclist[1:3]) # [start:stop-before:step]
# we can reverse them!!
print(fclist[::-1]) # means start at default, stop-before default, but step in reverse

# we can delete members
print(f'Initially there are { len(fclist) } feature classes')
del fclist[2]
print(f'Now there are { len(fclist) } feature classes')

