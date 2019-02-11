
def run_tests_in_class( c ):
    methods = [name for name in dir( c ) if callable(getattr( c, name)) if not name.startswith('_')]
    for method in methods:
        print("Running " + c.__name__ + "." + method )
        getattr( c, method)()
        print( c.__name__ + "." + method + " PASSED")
    print( "All tests from class " + str(c) + " complete" )

