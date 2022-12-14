class Human:
    #атрибуты уровня класса
    head=1
    body=1

    #метод:конструктор
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #метод
    def run(self):
        print(f'{self.name} is run')

    def __str__(self):
        return f'{self.name} {self.age}'
hum = Human('жибек',18)
hum.run()
print(hum)