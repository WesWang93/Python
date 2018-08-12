import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return "Circle with radius: " + str(self._radius)
    def __repr__(self):
        return f"Circle({self._radius})"
    def __add__(self, other):
        total_radius = self._radius + other._radius
        return Circle(total_radius)
    def __mul__(self, other):
        if type(other) == Circle:
            mul_radius = self._radius * other._radius
        else:
            mul_radius = self._radius * other
        return Circle(mul_radius)
    def __rmul__(self, value):
        mul_radius = self._radius * value
        return Circle(mul_radius)
    def __eq__(self, other):
        return self._radius == other._radius
    def __ne__(self, other):
        return not self._radius == other._radius
    def __lt__(self, other):
        return self._radius < other._radius
    def __gt__(self, other):
        return not self._radius < other._radius
    def __le__(self, other):
        return self._radius >= other._radius
    def __ge__(self, other):
        return not self._radius >= other._radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, radius):
        self._radius = radius
    @property
    def diameter(self):
        return self._radius*2
    @diameter.setter
    def diameter(self, radius):
        self._radius /= 2
    @property
    def area(self):
        return self._radius**2 * math.pi
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2)
