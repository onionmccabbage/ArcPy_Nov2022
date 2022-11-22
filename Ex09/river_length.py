import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex09'
arcpy.env.overwriteOutput = True

def findLen():
    '''measure the cumulative lenght of some rivers'''
    fc = 'rivers.shp'
    # we can use TOKENS to grab the individual data members
    with arcpy.da.SearchCursor( fc, ['SHAPE@LENGTH'] ) as cursor:
        length = 0 # begoin with a zero length measurement
        for r in cursor:
            # length = length + r[0]
            # or use shorthand
            length += r[0] # increment the length by each row in turn
            # print(f'Cumulative length has reached {length}')
        # or just show the final length
        # find what inits of measurement are being used
        desc = arcpy.da.Describe(fc)
        units = desc['spatialReference'].linearUnitName
        # print(f'Total length of all rivers is {length} {units}')
        #           we can format numbers to 2dp
        print('Total length of all rivers is {:.2f} {}'.format(length, units))

if __name__ == '__main__':
    findLen()