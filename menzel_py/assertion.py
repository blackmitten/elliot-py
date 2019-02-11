class Assert:
    @staticmethod
    def are_equal(o1, o2, delta = None, msg=""):
        if not delta is None:
            if(abs(o1 - o2) > delta ):
                raise AssertionError
        elif(o1 != o2):
            raise AssertionError
            
    @staticmethod
    def are_not_equal(o1, o2, msg=""):
        if(o1 == o2):
            raise AssertionError
    
    @staticmethod
    def is_true(b, msg=""):
        if not b:
            raise AssertionError
            
    @staticmethod
    def is_false(b, msg=""):
        if b:
            raise AssertionError
            