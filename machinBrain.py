class MachineBrain():
    def __init__(self,drinks_list):
        self.drinks=drinks_list
        self.water=300
        self.milk=200
        self.coffee=100
        self.money=0
        self.machine_on=True
    def fill_water(self):
        self.water=300
    def fill_coffee(self):
        self.coffee=100
    def fill_milk(self):
        self.milk=200
    def report(self):
        """print resourses machine"""
        print(f"water: {self.water}ml")
        print(f"milk: {self.milk}ml")
        print(f"coffee: {self.coffee}g")
        print(f"money: {self.money}$")
    def turn_of(self):
        """turn of the machine"""
        self.machine_on=False
    def check_if_drink_exist(self,user_choice):
        """return true if the user choice is exist"""
        for drink in self.drinks:
            if drink.name==user_choice:
                return drink
        return "none"
    def exist_resourses(self,drink):
        if drink.ingredients["water"]>self.water:
            print("Sorry there is no enough water")
            return False
        if drink.ingredients["milk"]>self.milk:
            print("Sorry there is no enough milk")
            return False
        if drink.ingredients["coffee"]>self.coffee:
            print("Sorry there is no enough coffee")
            return False
        return True
    def enough_money(self,user_coin,drink):
        if user_coin>=drink.cost:
            return True
        else:
            return False
    def buy_drink(self,user_choice):
        drink=self.check_if_drink_exist(user_choice)
        if drink=="none":
            return print("The drink you choose not exist. Try again")
        if self.exist_resourses(drink):
            print(f"The drink you choose cost {drink.cost}")
            if input("If you want to continuous type 'y' to exit type any key").lower()=="y":
                quarters=int(input("How much quarters "))
                dimes=int(input("How much dimes "))
                nickel=int(input("How much nickel "))
                pennies=int(input("How much pennies "))
                user_coins=0.25*quarters+0.1*dimes+0.05*nickel+0.01*pennies
            else:
                return
            if self.enough_money(user_coins,drink):
                self.money+=drink.cost
                self.water-=drink.ingredients["water"]
                self.coffee-=drink.ingredients["coffee"]
                self.milk-=drink.ingredients["milk"]
                if user_coins>drink.cost:
                    print(f"Here is ${round(user_coins-drink.cost,2)} dollars in change.")
                print(f"Here is your {drink.name}. Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded. {user_coins}$")
        else:
            return print("choose another drink.")
