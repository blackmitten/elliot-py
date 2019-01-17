from backend.square import *

class AQuickTests:
    def square_equality():
        s1 = Square(0, 0)
        s2 = Square(0, 1)
        s3 = Square(0, 1)
        s4 = Square(1, 1)
        s5 = Square(1, 1)
        assert(s1==s1)
        assert(s1!=s2)
        assert(s2==s3)
        assert(s3!=s4)
        assert(s4==s5)

    def square_offset():
        s6 = Square(4, 4);
        s7 = Square(2, 6);
        s8 = s6.offset(-2, 2);
        assert(s6 != s7);
        assert(s7 == s8);

    def square_copy():
        s1 = Square(1, 1)
        s2 = s1
        assert(s1==s2)

    def square_construct_from_notation():
        assert( Square.from_notation("a1") == Square(1, 1))
        assert( Square.from_notation("h1") != Square(1, 1))
        assert( Square.from_notation("h1") == Square(8, 1))
        assert( Square.from_notation("h8") == Square(8, 8))
        assert( Square.from_notation("a8") == Square(1, 8))

    def square_to_string():
        assert( str(Square.from_notation("a1")) == "a1" )
        assert( str(Square.from_notation("h5")) == "h5" )

    def square_subtraction():
        s1 = Square(2, 5)
        s2 = Square(6, 2)
        v = s1 - s2
        assert(v.x == -4)
        assert(v.y == 3)
        pass

methods = [name for name in dir(AQuickTests) if callable(getattr(AQuickTests, name)) if not name.startswith('_')]
for method in methods:
    print(method)
    getattr(AQuickTests, method)()

print("All tests done")
