# when a module is imported, EVEYTHING in that module runs
import arcpy

arcpy.env.overwriteOutput = True # Python is Capital T for True

def fn():
    print('all ok')


# every module is given a name when it is run
# the module that is directly run is always given the name
# __main__
if __name__ == '__main__':
    # exercise this module of code
    fn()
    fn()
    fn()
    print(__name__)