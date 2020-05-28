# QUestion 1: Write a class called Blouse, that inherits from the Clothing class
# and has the the following attributes and methods:
#   attributes: color, size, style, price, country_of_origin
#     where country_of_origin is a string that holds the name of a 
#     country
#
#   methods: triple_price, which has no inputs and returns three times
#     the price of the blouse
#
#
from Clothing import Clothing

class Blouse(Clothing):
    def __init__(self, color, size, style, price, country_of_origin):
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin
    

    def triple_price(self):
        return 3 * self.price


