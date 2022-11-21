# from utility import * 
import utility # we now have EVERYTHING from the utility.py module

# explore the names of the modules
print(__name__) # the name of the running module, i.e. __main__
print(utility.__name__) # ah ----

if __name__ == '__main__':
    # explore Python data structures
    # basic data types
    a = 3   # int
    b = 7.2 # float
    c = False # boolean
    d = None  # represents nothing
    # collection data types
    e = 'ArgGIS uses Python version 3' # this is a string of characters (immutable)
    print(e[0]) # A
    # members of an indexed collection are ordinal from zero, 1, 2, ... etc.
    print(e[12:18]) # [start:stop-before]
    # we can cast one data type to another data type
    str_e = int(e[27]) # or float etc.
    print( type(str_e), type(e[27])  )
    # lists and tuples
    l = [3, 2, 1, 'hi', b, e] # a list is a mutable collection of ANY data types
    l[2] = 'changed'
    print(l, type(l))
    # tuples are immutable - we are not permitted to change hte vlaues once they have been set
    t = (3, 2, 1, 'hi', b, e) # a tuple is an immutable collection of ANY data types
    print(t, type(t))
    # t[2] = 'no can do' # this throws an exception
    # member access
    print(t[1:4:2]) # (2, 1, 'hi) (start:stop-before:step)
    # dictionary is a non-indexed mutable collection
    my_dict = {'Eileen':'some value', 'age':32, 'member':False} # arbitrary members - NOT indexed
    print(type(my_dict), my_dict['age']) # we can access members by their key
