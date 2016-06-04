import random

class Barrack:
    factories = {}
    def addFactory(id, Barrack):
        Barrack.factories.put[id] = barrack
    addFactory = staticmethod(addFactory)
    def createTroop(id):
        if not Barrack.factories.has_key(id):
            Barrack.factories[id] = \
              eval(id + '.Factory()')
        return Barrack.factories[id].create()
    createTroop = staticmethod(createTroop)

class Troop(object): pass

class Giant(Troop):
    def train(self): print("Giant.train")
    def remove(self): print("Giant.remove")
    class Factory:
        def create(self): return Giant()

class Wizard(Shape):
    def train(self):
        print("Wizard.train")
    def remove(self):
        print("Wizard.remove")
    class Factory:
        def create(self): return Wizard()

def troopNameGen(n):
    types = Troop.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

troops = [ Barrack.createTroop(i)
           for i in troopNameGen(7)]

for troop in troops:
    troop.train()
    troop.remove()
