import util
import arcpy

def createUniqueBufferName(new_name):
    '''add a buffer with a unique name'''
    fc='airports.shp'
    # if the name already exists, a number is sequentialy added to the name
    unique_name = arcpy.CreateUniqueName(new_name)
    arcpy.Buffer_analysis(fc, unique_name, "5000 METERS")

if __name__ == '__main__':
    createUniqueBufferName('buffer.shp')
