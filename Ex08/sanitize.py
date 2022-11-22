import util
import arcpy

# we will add field names
fc = 'airports.shp'
# new_field = 'HasDecentTea'
new_field = 'oops!&%'
newFieldType = 'TEXT'
fieldName = arcpy.ValidateFieldName(new_field) # replace illegal characters with an underscore
fieldLength = 12 # let this field contain twelve characters
#                                           often we must skip members
arcpy.AddField_management(fc, fieldName, newFieldType, "", "", fieldLength)
# we can look at the existing fields
fieldList = arcpy.ListFields(fc)
for f in fieldList:
    print(f.name) # just show the name of the field