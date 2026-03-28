class Animal:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
    def sleep(self) -> None:
        print(f"{self.name} is sleeping")
    def eat(self) -> None:
        print(f"{self.name} is eating")
    
class Dog(Animal): # inheritance
    def __init__(self,breed:str,name:str,age:int):
        self.breed=breed
        super().__init__(name,age) # passing to parent function
    def introduce(self) -> None:
        print(f"Hi my name is {self.name}, my age is {self.age} and my breed is {self.breed}")

dog=Dog('Inidie','Kalu',16)
dog.introduce()
dog.eat()