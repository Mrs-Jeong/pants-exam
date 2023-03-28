from obsessed_with_you import *
laborant = input('Введите имя лаборанта')

laborant = Laborant(laborant,'ученик')

carrot = Carrot('морковь',100,5,5)
tomato = Tomato('помидор',100,5,5)
cucumber = Cucumber('огурец',100,5,5)
#начало симуляции
print("The simulation of the working day has begun.")
time = 8 #время начала рабочего дня
end_time = 19 #время окончания рабочего дня
 
#цикл, который запрашивает у лаборанта действие каждый час
while time <= end_time:
    print("Time:", str(time)+':00') # выводим информацию о текущем времени
    sample = input("You went into the office with experimental samples. Select a sample:\n 1 - carrot\n 2 - tomato\n 3 - cucumuber  ") # спрашиваем у лаборанта, над каким опытным образцом будет совершаться действие
   
    if sample =='1':
        plant = carrot
    elif sample == '2':
        plant = tomato
    else:
        plant = cucumber
   
    action = input("Select an action:\n 1 - water\n 2 - food\n 3 - light ") # уточняем какое действие будет совершаться над образцом
    if action =='1':
        laborant.water(plant)
    if action =='2':
        laborant.food(plant)
    if action =='3':
        laborant.light(plant)
         
       
    time = time + 1 # увеличиваем время на час
    
 
#выводим информацию об опытных образцах и их текущем статусе
carrot.info()
result1 = carrot.alive()    
tomato.info()
result2 = tomato.alive()  
cucumber.info()
result3 = cucumber.alive()  
 
#выводим результаты симуляции. Допущен или нет лаборант до настоящих опытных образцов.
laborant.check_result(result1, result2, result3)
