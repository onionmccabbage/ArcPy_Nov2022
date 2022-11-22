# Python lets us try some code, and catch exceptions so they dont crash our program
def divideValues(x, y):
    try:
        return x/y
    except ZeroDivisionError as err: # we should handle specific exception first
        print( f'Doh! you cant divide by zero you numpty: {err}' )
    except Exception as err:
        print( f'Something went wrong: {err}' )
    finally:
        print('the finally block always runs, even if there is no exception')


if __name__ == '__main__':
    result = divideValues(8, 0) # 4.0
    print(result)