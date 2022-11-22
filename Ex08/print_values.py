import arcpy
arcpy.env.workspace = r'c:\PythonPro\Ex08'
arcpy.env.overwriteOutput = True

# using an arcpy cursor
fc = 'airports.shp' # always best to include the extention
# the arcpy cursor uses a member of the collection
# cursor = arcpy.da.SearchCursor(fc, ['NAME'])
# for r in cursor:
#     print( f'Airport {r[0]}' )

# we can also use an SQL cursor as follows:
# sql_exp = ' "TOT_ENP" > 100000  ' # observe the types of quotation marks
# cursor = arcpy.da.SearchCursor(fc, ['NAME'], sql_exp) # here we filter the cursor to only work with results from SQL expression
# for r in cursor:
#     print(r[0]) # there are now only six matching airports

# write code to just show airpot names where   "AIRPRTX020" > 850
# sql_exp = ' "AIRPRTX020" > 850  ' # observe the types of quotation marks
# cursor = arcpy.da.SearchCursor(fc, ['NAME', 'COUNTY'], sql_exp) # here we filter the cursor to only work with results from SQL expression
# for r in cursor: # the values are in a tuple 
#     print( f'the airport named {r[0]} is in {r[1]} county' )

# we can use SQL statements with text parameters - be careful with quotes
sql_exp = ' "FEATURE" = \'Seaplane Base\' ' # here we 'escape' the single quotes
cursor = arcpy.da.SearchCursor(fc, ['NAME', 'COUNTY'], sql_exp) # here we filter the cursor to only work with results from SQL expression
for r in cursor: # the values are in a tuple 
    print( f'the seaplane base named {r[0]} is in {r[1]} county' )

# SQL is rather fussy about constructing SQL expressions
# arcpy has tools to help with this
delimiter_field = arcpy.AddFieldDelimiters(fc, "COUNTY") # or any other field in the attribute table
sql_exp = "{} = 'Anchorage Borough' ".format( delimiter_field )
cursor = arcpy.da.SearchCursor(fc, ['NAME', 'COUNTY'], sql_exp) # here we filter the cursor to only work with results from SQL expression
for r in cursor: # the values are in a tuple 
    print( f'the asset named {r[0]} is in {r[1]} county' )
