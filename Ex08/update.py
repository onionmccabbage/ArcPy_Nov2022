import util # this does all the preparation
import arcpy # delete this later!!!

# we may hit a problem with locks ...
# you can only do updates if ArcGIS is NOT looking at the same assets

# the plan: we need to find all missing 'STATE' values in the 'airports.shp'
# and populate them with 'AK'

def fixStateField(): # code in a function can be called repeatedly
    '''
    This is a Docstring - a place to document the code
    '''
    fc = 'airports.shp'
    delimiter_field = arcpy.AddFieldDelimiters(fc, "STATE")
    sql_exp = "{} <> 'AK' ".format(delimiter_field)
    # the 'with' operator lets us iterate over members of a collection
    # in this case, we iterate over every member returned by the cursor
    with arcpy.da.UpdateCursor(fc, ['STATE'], sql_exp) as cursor:
        for r in cursor:
            r[0] = 'AK' # set the 'STATE' field to 'AK' (for only missing values)
            # we must remember to commit the changes!!!!
            cursor.updateRow(r) # here we commit the change so it persists in the data structure
  
if __name__ == '__main__':
    fixStateField()