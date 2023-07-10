# class Orange():
#     def __init__(self, weight, color):
#         self.weight = weight 
#         self.color = color
#         print("Создано!")
# orl = Orange(100, "темный апельсин")
# orl.weight == 100
# orl.color == 'темный апельсин'

# print(orl.color)
# print(orl.weight)

# class Orange():
#     def __init__(self, w, c,):
#         self.weight = w
#         self.color = c
#         self.mold = 0
#         print("Создано!")

#     def rot(self, days, temp):
#         self.mold = days * temp

# orange = Orange(6, "апельсин")
# print(orange.mold)
# orange.rot(10, 33)
# print(orange.mold)

# class Rectangle():
#     def __init__(self, w, l):
#         self.width = w 
#         self.len = l 
    
#     def area(self):
#         return self.width * self.len

#     def chanche_size(self, w, l):
#         self.width = w 
#         self.len = l 

# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# rectangle.chanche_size(20, 40)
# print(rectangle.area())

# class Apple():
#     def __init__(self, name, color, version, camera, model):
#         self.name = name 
#         self.color = color
#         self.version = version 
#         self.camera = camera 
#         self.model = model
#         print("Телефон: ")


# aple = Apple("iphone", "цвет: черный", "версия: {v16}", "камера: {3cam}", "модель: {13pro}")
# aple.name == "iphone"
# print(aple.name)
# aple.color == "цвет: черный"
# print(aple.color)
# aple.version == 16
# print(aple.version)
# aple.camera == 3
# print(aple.camera)
# aple.model == "13pro"
# print(aple.model)

# import math

# class Circle():
#     def __init__(self, count, width):
#         self.count = count
#         self.width = width

#     def area(self):
#         return self.count * self.width
    
#     def pi(self):
#         return self.width

    
# cirle = Circle(10, 20)
# print(cirle.area())
# print(cirle.pi())
# print(cirle.area)

# class Triangle():
#     def __init__(self, length, breadth):
#         self.length = length 
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth
    
# triangle = Triangle(50, 30)
# print(triangle.area())


from math import cos, tan, pi
 
 
class Triangle:
    @classmethod
    def get_area(cls, c, alpha):
        return 0.5 * c * c * tan(alpha * pi / 180)
 
    @classmethod
    def get_a(cls, c, alpha):
        return 0.5 * c / cos(alpha * pi / 180)
 
 
c = float(input("c="))
alpha = float(input("alpha="))
print(Triangle.get_area(c, alpha))
print(Triangle.get_a(c, alpha))


