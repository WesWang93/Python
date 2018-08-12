from circle import Circle
import pytest

c1 = Circle(3)
c2 = Circle(4)

def test_attr():
    rad = c1.radius
    assert rad == 3
    dia = c1.diameter
    assert dia == 6
    area = int(c1.area)
    assert area == 28
    
    c = Circle.from_diameter(10)
    assert c.radius == 5
    assert c.diameter == 10

#Test add, multiplication
def test_math():
    add = c1 + c2
    assert add == Circle(7) 
    mul = c1 * c2
    assert mul == Circle(12)
    rmul = 5 * c1
    assert rmul == Circle(15)

#Test Comparison
def test_comparison():
    assert c1 == c2 is False
    assert c1 != c2 is True
    assert c1 < c2 is True
    assert c1 <= c2 is True
    assert c1 > c2 is False
    assert c1 >= c2 is False

def test_sort():
    clist = [Circle(5), Circle(12), Circle(7), Circle(9), Circle(1), Circle(4), Circle(2)]
    assert clist[0] == Circle(1)
    assert clist[3] == Circle(5)
    assert clist[-1] == Circle(12)