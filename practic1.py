import math 

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimetr(self):
        return 2 * math.pi * self.radius
    
r = int(input("Выведите радиус круга: "))
obj = Circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimetr(), 2))

# class Haxagon():
#     def __init__(self, ):

# class Rectangle():
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l
#         pass
#     def area(self):
#         return self.width * self.len
# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# rectangle
# class Data():
#     def __init__(self):
#         self.nums = [1,2,3,4,5]
#     def change_data(self, index, n):
#         self.nums[index] = n 

# one_data = Data()
# one_data.nums[0] = 100
# print(one_data.nums)

# data_two = Data()
# data_two.change_data(0, 100)
# print(data_two.nums)

# shapes = [trl,
#         swl,
#         crl
#         ]
# for a_shape in shapes:
#     a_shape.draw()

# class Shape():
#     def __init__(self, w, l):
#         self.width = w
#         self.len = l 
#     def print_size(self):
#         print(""" {} на {}""" .format(self.width, self.len)) 
# shape = Shape(50, 50)
# shape.print_size()