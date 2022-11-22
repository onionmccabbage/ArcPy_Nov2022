import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex09'
arcpy.env.overwriteOutput = True

fc = 'dams.shp'
# find all the x-y for the points
with arcpy.da.SearchCursor(fc, ['SHAPE@XY']) as cursor:
    for r in cursor:
        # here we us Python to easily assign values
        # print(r[0])
        x, y = r[0] # split the x and y from the resulting row
        # print them nicely
        print('X:{:.2f} Y:{:.2f}'.format(x,y))
