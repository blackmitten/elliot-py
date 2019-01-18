class Assert:
    @staticmethod
    def are_equal(o1, o2):
        if(o1 != o2):
            raise AssertionError
            
    @staticmethod
    def are_not_equal(o1, o2):
        if(o1 == o2):
            raise AssertionError
            