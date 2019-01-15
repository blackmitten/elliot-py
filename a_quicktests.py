from square import *

def test_square_equality():
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

def square_copy_and_change():
    s1 = Square(1, 1)
    s2 = s1
    assert(s1==s2)
    s2.x += 1
    assert(s1!=s2)


def tests():
    test_square_equality()
    square_copy_and_change()

tests()
print("All tests done")
