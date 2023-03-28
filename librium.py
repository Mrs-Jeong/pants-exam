class Vegetable():
    def __init__(self,plant,water,food,light):
        self.plant = plant # тип растения
        self.water = water
        self.food = food
        self.light = light
    def info(self):
        print('вид растения:', self.plant)
        print('вода:', self.water,'мл')
        print('удобрения:', self.food,'грамм')
        print('свет:', self.light,'ч')

class Laborant():
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def info(self):
        print('имя:', self.name)
        print('позиция:', self.position)
    def water(self,vegetable):
        vegetable.water = vegetable.water + 200
    def food(self,vegetable):
        vegetable.food = vegetable.food + 20
    def light(self,vegetable):
        vegetable.light = vegetable.light + 20
    def check_result(self,result1,result2,result3):
        if result1 == True and result2 == True and result3 == True:
            self.info()
            print('Экзамен сдан')
        else:
            self.info()
            print('Экзамен провален')
