import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex08'
arcpy.env.overwriteOutput = True

infc = 'airports.shp'
outfc = 'airports_anchorage.shp'

delimiter_field = arcpy.AddFieldDelimiters(infc, "COUNTY") # or any other field in the attribute table
sql_exp = "{} = 'Anchorage Borough' ".format( delimiter_field )

# take a copy of the airports and create new feature classes 
# ontaining ONLY anchorage airports
arcpy.Select_analysis(infc, outfc, sql_exp)

