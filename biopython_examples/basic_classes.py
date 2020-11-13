#!/usr/bin/env python3
# basic_classes.py

class Circle():
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
    
    def diameter(self):
        return self.radius * 2

    def circmfrence(self):
        return (self.radius * 2) * 3.14

    def isRed(self):
        if self.color == "red"
        return True

class GraduateStudent():
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self, years_matriculated):
        return 2020 - self.year
        
