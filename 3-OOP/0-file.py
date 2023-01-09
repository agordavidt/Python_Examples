class Animal:

    def __int__(self, sturcture="Unknown", feeding="Unknown"):
        self.structure = sturcture
        self.feeding = feeding
    @property
    def structure(self):
        return self.__structure

    @structure.setter
    def structure(self, structure):
        self.__structure = structure

    @property
    def feeding(self):
        return self.__feeding

    @feeding.setter
    def feeding(self, feeding):
        self.__feeding = feeding

class Mammal(Animal):
       pass