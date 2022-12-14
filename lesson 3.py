# инкапсуляция (защитить)
# git clone
# __скрыть
class Zhibek:
       head = 1
       hands=1
       foots=2
       def __init__(self,name='Zhibek',age=18):
           self.__name=name
           self._age=age
       def __str__(self):
           return f'{self.__name}' \
                  f'{self._age}'
       def run(self):
           self.__run()
           self.__g()
           print(self._age - 1)

       def _run(self):
            print(self.__name, 'run')

       def __g(self):

e=Zhibek()
e.run()
e._run()