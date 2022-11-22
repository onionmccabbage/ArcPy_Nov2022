import util

# Write code to create a duplicate of all the airports
infc = 'airports.shp'
outfc = 'airports_copy.shp'

def makeAirportCopy():
    # check if the copy already exists
    already_done = arcpy.Exists('airports_copy.shp')
    if already_done:
        print('a copy already exists - nothing to do')
    else:
        # take a copy of all the airports and create a new feature class 
        arcpy.Select_analysis(infc, outfc)
        print('a copy has been created, called {}'.format(outfc))

# change all Seaplane Bases to 'Sea'
def changeField(whichField, newValue):
    fc = 'airports_copy.shp'
    delimiter_field = arcpy.AddFieldDelimiters(fc, whichField) # or (fc, "FEATURE")
    sql_exp = "{} = 'Seaplane Base' ".format(delimiter_field)
    print('The SQL expression reads: {}'.format(sql_exp))
    try:
        with arcpy.da.UpdateCursor(fc, ['FEATURE'], sql_exp) as cursor:
            for r in cursor:
                print(r[0])
                r[0] = 'Sea' 
                print('A row has been updated with value {}'.format(r[0]))
                cursor.updateRow(r) 
    except Exception as err:
        print('There was a poblem: {}'.format(err))

def extractSmall(max_pax):
    # make an extract of all airports where TotalENP < 1000 (as a parameter in a function)
    infc = 'airports.shp'
    outfc = 'airports_small.shp'
    delimiter_field = arcpy.AddFieldDelimiters(infc, "TOT_ENP")
    # sql_exp = "{} < 1000 ".format( delimiter_field )
    sql_exp = "{} < {} ".format( delimiter_field, max_pax )
    print('The SQL expression reads {}'.format(sql_exp))
    arcpy.Select_analysis(infc, outfc, sql_exp)

if __name__ == '__main__':
    '''run the example code'''
    # makeAirportCopy()
    # changeField('FEATURE', 'Sea')
    # extractSmall(1000)