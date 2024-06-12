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
    
    def __len__(self):
        return int(self.__a.distance(self.__b))

    def __eq__ (self,other):
            try:
                return self.__a == other.a and self.__b == other.b
            except:
                return False
            
    def length(self):
        return self.__a.distance(self.__b)
    
    def __lt__(self, other):
        return self.length() < other.length()
    
    def __gt__(self, other):
        return self.length() > other.length()
    
    def __le__(self, other):
        return self.length() <= other.length()
    
    def __ge__(self, other):
        return self.length() >= other.length()

v0 = Vector2D(7, 13)
v1 = Vector2D(10, 20)
v2 = Vector2D(2, 5)
l1 = Line2D(v1, v2)
l2 = Line2D(v0, v1)
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
print('l1의 길이: ', len(l1))
v12 = (l1 == l2) 
print('{} = {} = '.format(l1, l2), v12)
print('{} < {} = '.format(l1, l2), l1 < l2)
print('{} > {} = '.format(l1, l2), l1 > l2)
print('{} <= {} = '.format(l1, l2), l1 <= l2)
print('{} >= {} = '.format(l1, l2), l1 >= l2)
print('20200872 이다빈')