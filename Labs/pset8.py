# Name:         Jillian Quinn
# Course:       CPE 101       
# Instructor:   Kauffman
# Assignment:   Problem Set 8
# Term:         Winter 2019


class Point:


    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)


    def distance(self, to):
        return ((to.x - self.x) ** 2 + (to.y - self.y) ** 2) ** 0.5


class Circle:


    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def __eq__(self, other):
        return self.center == other.center and self.radius == other.radius


    def __repr__(self):
        return "{0}r @ ({1}, {2})".format(self.radius, self.center.x, \
            self.center.y)


    def overlaps(self, other):
        return self.center.distance(other.center) < (self.radius + \
            other.radius)


class Integer:


    def __init__(self, i):
        self.abs_val = abs(i)
        self.is_pos = i > 0


    def __eq__(self, other):
        return self.abs_val == other.abs_val and self.is_pos == other.is_pos


    def __repr__(self):
        if self.is_pos or self.abs_val == 0:
            return "{0}".format(self.abs_val)
        else:
            return "-{0}".format(self.abs_val)


    def add(self, other):
        if self.is_pos:
            integer_self = self.abs_val
        else:
            integer_self = self.abs_val * -1
        if other.is_pos:
            integer_other = other.abs_val
        else:
            integer_other = other.abs_val * -1
        return Integer(integer_other + integer_self)


def point_distance_all(points):
    return [i.distance(Point(0, 0)) for i in points]


def are_in_first_quadrant(points):
    return [i for i in points if i.x > 0 and i.y > 0]


def circle_distance_all(points):
    return [i.center.distance(Point(0, 0)) for i in points]


def overlaps_all(circles):
    return [i for i in circles if i.overlaps(Circle(Point(0, 0), 1))]


def add_n_all(ints, n):
    return [i.add(Integer(n)) for i in ints]


def are_greater_than_n(ints, n):
    return [i for i in ints if int(i.__repr__()) > n]











