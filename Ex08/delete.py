import util
import arcpy # delete this later!!!

def clearAnchorageAirports(numpax):
    '''
    Here we take the number of pasengers (numpax) and delete ALL
    Anchorage airports with less than that many passengers
    NB make sure ArcGIS is not also running (to avoid locks)
    '''
    try:
        fc = 'airports_anchorage.shp'
        # the list of fields is indexed    0          1       2       etc.
        with arcpy.da.UpdateCursor(fc, ['TOT_ENP', 'STATE', 'NAME']) as cursor:
            for r in cursor:
                if r[0] < numpax:
                    cursor.deleteRow() # this deletes the row IRRETRIEVABLY
    except Exception as err:
        print(f'There was a problem {err}')
    finally:
        pass

if __name__ == '__main__':
    clearAnchorageAirports(100000)