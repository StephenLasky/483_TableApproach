import math
import random

# This class provides the detail of a "unit"
# For example, it could describe a unit of length
# class Unit:

# This class provides the details and functionality of the shape of a theme class
# It is then subclassed into the specific shape that it is
# For example, a car would be a rectangular prism
# Required functions:
#   volume:         returns the volume of the shape
#   surface_area:   returns the surface area of the shape
class Shape(object):
    RECTANGULAR_PRISM = 0
    SPHERE = 1
    CYLINDER = 2

    SHAPE_NAMES = { RECTANGULAR_PRISM: "Rectangular Prism", SPHERE: "Sphere", CYLINDER: "Cylinder" }

    def __init__(self, shape):
        self.shape = shape
        self.name = self.SHAPE_NAMES[shape]

# These are all extensions of the shape class
class Rectnagular_prism(Shape):
    def __init__(self, length, width, height):
        super(Rectnagular_prism,self).__init__(self.RECTANGULAR_PRISM)
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.length + self.length * self.height)
class Sphere(Shape):
    def __init__(self, radius):
        super(Sphere, self).__init__(self.SPHERE)
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
class Cylinder(Shape):
    def __index__(self, radius, height):
        super(Cylinder,self).__init__(self.CYLINDER)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height


# This is the UNIT class, it specifies the details and functionality of a unit of measurement
# Some examples include, money, length, time ... these are all UNITs
# Functions:
#   get_name: returns the name of the unit... e.g. "Money"
class Unit(object):
    MONEY = 0
    LENGTH = 1
    TIME = 2
    MASS = 3
    OTHER = 4

    UNIT_NAMES = { MONEY: "Money", LENGTH: "Length", TIME: "Time", MASS: "Mass", OTHER: "Other Name" }

    def __init__(self, unit):
        self.CONVERSION = {}
        self.unit = unit

    def get_name(self):
        return self.UNIT_NAMES[self.unit]


# This is the LENGTH class, it extends the UNIT class
# base unit: meter
class Length(Unit):
    CONVERSION = { "meter": 1, "decimeter": 10, "centimeter": 100, "millimeter": 1000, "kilometer": 0.001 }

    def __init__(self):
        super(Length,self).__init__(self.LENGTH)
    # def get_name(self):
    #     return super.get_name()

# This is the TIME class, it extends the UNIT class
# base unit: second
class Time(Unit):
    CONVERSION = { "second": 1 , "minute": 1/60, "hour": 1/3600, "day": 1/86400, "week": 1/604800 }

    def __init__(self):
        super(Time,self).__init__(self.TIME)
    # def get_name(self):
    #     return super.get_name()

# This is the MONEY class, it extends the UNIT class
# base unit: dollar
class Money(Unit):
    CONVERSION = { "dollar": 1, "cent": 1/100 }

    def __init__(self):
        super(Money,self).__init__(self.MONEY)
    # def get_name(self):
    #     return super.get_name()

# This is the MASS class, it extends the UNIT class
class Mass(Unit):
    CONVERSION = { "gram": 1/1000}

    def __init__(self):
        super(Mass,self).__init__(self.MASS)

# This is the OTHER class, it extends the UNIT class
class Other(object):
    CONVERSION = {}

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name



# This is the AREA class, it extends the UNIT class
# Base unit: meters squared
# TODO


class Ratio(object):
    def __init__(self, name, numerator, denominator):
        self.name = name
        self.numerator = numerator
        self.denominator = denominator

    def get_name(self):
        return self.name
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator


# terms should be a list of subclassed units of length N
# operators should be a list of characters, which are opertaors, of length N-1
class Equation(object):
    def __init__(self, name, terms, operators):
        self.name = name
        self.terms = terms
        self.operators = operators





# This is the THEME class, it is the structure by which future theme classes are stored
# Three primary properties:
#   1. names are all possible names for the theme class, names[0] is considered the official name of the class; example: [car, sedan, truck]
#   2. the shape is the shape of the theme class in quesiton, for example a car is a rectangular prism
#   3. the ratios argument is a list of ratios that are relevant to the theme class, for example a car might have: money:distance, distance:time
class Theme(object):
    # initialization function for the theme class
    # argument:     names are all possible names for the theme class, names[0] is considered the official name of the class; example: [car, sedan, truck]
    # argument:     the shape is the shape of the theme class in quesiton, for example a car is a rectangular prism
    # argument:     the ratios argument is a list of ratios that are relevant to the theme class, for example a car might have: money:distance, distance:time
    #               these ratios are passed as a LIST of TUPLES, where (money, time) would indicate money : time
    #               the tuple contains two UNIT objects; unit objects are defined above
    #               thus, the ratios list should appear formatted as follows: [ (UNIT, UNIT), (UNIT, UNIT), (UNIT, UNIT) ... (UNIT, UNIT) ]
    def __init__(self, names, shape, ratios):
        self.names = names
        self.shape = shape
        self.ratios = ratios


    def get_random_ratio(self):
        number_of_ratios = len(self.ratios)
        random_index = random.randint(0, number_of_ratios-1)
        return self.ratios[random_index]

    def get_random_name(self):
        if len(self.names) > 1:
            number_of_names = len(self.names)
            random_index = random.randint(1, number_of_names-1)
            return self.names[random_index]
        else:
            return self.names[0]


### Sample run ###
# generate a theme class
car_names = ["automobile", "car", "sedan", "truck"]
car_shape = Rectnagular_prism(5, 5, 5)
car_ratios = [ Ratio("speed", Length(), Time()), Ratio("cost per time", Money(), Time()), Ratio("cost per distance", Money(), Length())]
car_theme = Theme(car_names, car_shape, car_ratios)

# generate a different theme class
# NEW THEME CLASS HERE
# school_theme = xyz!!!

school_names = ["elementary school", "middle school", "high school", "school", "university"] school_shape = Rectnagular_prism(50,50,50) school_ratios = [ Ratio("seats per table", Other("seats"), Other("tables")), Ratio("students per room", Other("students"), Other("rooms"))] school_theme = Theme(school_names, school_shape, school_ratios)
















