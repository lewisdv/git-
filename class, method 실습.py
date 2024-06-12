import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
                        
    def __add__(self,other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self,other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    
    def __neg__(self):
        return Vector2D(-self.x, -self.y)
    
    def __eq__ (self,other):
        try:
            return self.x == other.x and self.y == self.y
        except:
            return False
        
    def distance(self, other):
        return math.sqrt((self.x - other.y)**2 + (self.y - other.y)**2)

class Line2D:
    def __init__(self, a, b):
        if not isinstance(a, Vector2D) or not isinstance(b, Vector2D):
            raise TypeError
        self.__a = a
        self.__b = b
    
    def __str__(self):
        return "{} - {}".format(self.__a, self.__b)

v1 = Vector2D(10, 20)
v2 = Vector2D(2, 5)
v3 = v1 + v2
print('{} + {} ='.format(v1, v2), v3)
v4 = v1 - v2
print('{} - {} ='.format(v1, v2), v4)
v5 = v1 * v2
print('{} * {} ='.format(v1, v2), v5)
v6 = v1 / v2
print('{} + {} ='.format(v1, v2), v6)
v7 = -v1
print('{} = '.format(v1), v7)
v8 = (v1 == v2)
print('{} == {} = '.format(v1, v2), v8)
v9 = (v1 == v1)
print('{} == {} = '.format(v1, v1), v9)
v10 = (v1 == 10)
print('{} == 10 = '.format(v1), v10)
v11 = v1.distance(v2)
print('{}와 {}의 거리 ='.format(v1, v2), v11)
print('20200872 이다빈')