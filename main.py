from menu import menu
from drinkClass import Drink
from machinBrain import MachineBrain
drink_list=[]

for drink in menu:
    drink_list.append(Drink(drink["name"],drink["ingredients"],drink["cost"]))
machine=MachineBrain(drink_list)
while machine.machine_on:
    user_choice=input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice=="report":
        machine.report()
    elif user_choice=="off":
        machine.turn_of()
    elif user_choice=="fill":
        what_to_fill=input("Which  resourse to fill? (water/coffee/milk/all) ").lower()
        if what_to_fill=="water":
            machine.fill_water()
        elif what_to_fill=="coffee":
            machine.fill_coffee()
        elif what_to_fill=="milk":
            machine.fill_milk()
        elif what_to_fill=="all":
            machine.fill_milk()
            machine.fill_water()
            machine.fill_coffee()
    else:
        machine.buy_drink(user_choice)