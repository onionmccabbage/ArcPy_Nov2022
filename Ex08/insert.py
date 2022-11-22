import util

import arcpy # .. so we get code hinting
# we can insert a new airport - this time, just give it a name
def newAirport(airport_name):
    '''take the airport name and amke a new airpot inserted into the fc'''
    fc = 'airports.shp' # we probalby should check it exists...
    # careful - there is an insertCursor on arcpy and there is also one on arcpy.da (data analysis)
    with arcpy.da.InsertCursor(fc, 'NAME') as cursor: # we have a cursor which lets us access the fc field called NAME
        cursor.insertRow([airport_name]) # use the provided name

if __name__ == '__main__':
    newAirport('Troon')