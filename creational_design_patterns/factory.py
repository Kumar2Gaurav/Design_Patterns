from enum import Enum
from abc import ABC, abstractmethod


class Burgers(Enum):
    CHEESEBURGER = "CHEESE"
    VEGANBURGER = "VEGANBURGER"
    DELUXE_CHEESEBURGER = "DELUXE_CHEESEBURGER"
    VEGAN = "VEGAN"


class Burger(ABC):
    def __int__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def get_name(self):
        return self.name


class CheeseBurger(Burger):
    def __int__(self):
        super().__int__()
        self.name = "Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

class VeganBurger(Burger):
    def __int__(self):
        super().__int__()
        self.name = "Vegan Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

class DeluxCheeseBurger(Burger):
    def __int__(self):
        super().__int__()
        self.name = "Delux Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

class DeluxVeganBurger(Burger):
    def __int__(self):
        super().__int__()
        self.name = "Delux Vegan Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass

class BurgerStore(ABC):

    @abstractmethod
    def create_burger(self, item: Burgers) -> Burger:
        pass

    def order_burger(self,type:Burgers) -> Burger:
        burger = self.create_burger(type)
        print(f"---Making a {burger.get_name()}")
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger

class CheeseBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.CHEESE:
            return CheeseBurger()
        elif item == Burgers.DELUXECHEESE:
            return DeluxCheeseBurger()
        else:
            return None


class VeganBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.VEGAN:
            return VeganBurger()
        elif item == Burgers.DELUXEVEGAN:
            return DeluxVeganBurger()
        else:
            return None


cheese_store = CheeseBurgerStore()
vegan_store = VeganBurgerStore()

burger = cheese_store.order_burger(Burgers.CHEESE)
print(f"Ethan ordered a {burger.get_name()}")
burger = vegan_store.order_burger(Burgers.VEGAN)
print(f"Joel ordered a {burger.get_name()}")
