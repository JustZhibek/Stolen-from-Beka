class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name_Superhero(self):
        print(f'name:{self.name}')

    def health_points(self):
        print(f'health: {self.health_points * 2}')

    def __str__(self):
        return f'name:{self.nickname}\n' \
               f'superpower: {self.superpower}\n' \
               f'health: {self.health_points}\n'

    def __len__(self):
        print('len_catchphrase: ', len(self.catchphrase))


Hero = SuperHero(name='Jack', nickname='Sparrow', superpower='motivate', health_points='100', catchphrase="I'll help u")
print(Hero.name)
print(Hero.nickname)
print(Hero.health_points)
Hero.__len__()
print(Hero)


# HomeWork №2

class IronMan(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

        self.fly = fly
        self.damage= damage
    def health_points(self):
        self.fly = False
        print(f'health: {self.health_points ** 2}')
    def fly2 (self):
        print ('fly in the True_phrase')



ironMan = IronMan('Alex', 'Iron', 'teacher', '40', 'hello')
print(ironMan.health_points)
ironMan.fly2()


# class IronMan1(SuperHero):
#     wings = 2
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, wings, tail):
#     super().__init__(name, nickname, superpower, health_points, catchphrase)
#
#     self.wings = wings
#     self.tail = tail
#
#
# IronMan = IronMan1('Alex', 'Iron', 'teacher', '40', 'hello', '2', '1', False)
# print(IronMan.wings)


class Villain(IronMan):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase,fly=False, damage=False)


    def gen_x (self):
       pass
    def crit(self, damage):
        self.damage
        print(self.damage * 2)

v=Villain('Toby','Iron','create','45','create sth')

v.crit(ironMan.damage)





