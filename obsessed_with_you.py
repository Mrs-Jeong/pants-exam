from librium import *

class Carrot (Vegetable):
    def alive (self):
        if self.water >= 300 and self.food >= 25 and self.light >= 25:
            print('its alive!!')  
            return True
        else:
              print('its bad')
              return False
class Tomato (Vegetable):
    def alive (self):
        if self.water >= 200 and self.food >= 25 and self.light >= 25:
            print('its alive!!')  
            return True
        else:
              print('its bad')
              return False
class Cucumber (Vegetable):
    def alive (self):
        if self.water >= 500 and self.food >= 25 and self.light >= 25:
            print('its alive!!')  
            return True
        else:
              print('its bad')
              return False
        
