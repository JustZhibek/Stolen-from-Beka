# Парадигмы ООП наследование,полиморфизм-изменение поведение наследованных объектов
# инкапсуляция

#супер класс
class Robot:
    brain = True


    def __init__(self, name, model, color, destination):
        self.name = name
        self.model = model
        self.color = color
        self.destination = destination


    def __str__(self):
        return f'name is {self.name}\n' \
               f'color is {self.color}\n' \
               f'model is {self.model}\n '

    def desti(self):

        print(self.destination)


robot = Robot('Влад', 'А4', 'blue', 'снимать видео')
print(robot)
print(robot.desti)


# наследование #дочерний класс
class Robot2(Robot):
    brain = True
    def __init__(self, name, model, color, destination, fly):
        super().__init__( name, model, color, destination)
        Robot.__init__(self, name, model, color, destination)
        self.fly = fly

    def desti(self):
        self.fly=False
        print(self.fly)
robot2 = Robot2('terminator', '1001', 'pink', 'отбирает одежду', True)
print(robot2.fly)
robot2.desti()
print(robot2.fly)

robot2.desti()
robot.desti()
print(robot2.brain,robot.brain)


class Robot3(Robot2):
    def desti(self):
        print(f'{self} теперь  летает')


MegaTron=Robot3('TRANSformer','Desipticon','red','WARS',False)
MegaTron.desti()



