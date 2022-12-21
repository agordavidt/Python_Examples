import random
import math

class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random() + .5)

        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)

        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) ==  "Game Over":
                print("Game Over")
                break
    
    #A function will receive each Warrior that will attack the other
    #have the attack and block amounts be integers to make the resuls lean
    #if a warrior dies return that result to end the looping in the above funtion

    #make this method static because we don't need to use self
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2warriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health = warriorB.health - damage2warriorB

        print(f"{warriorA.name} attacks {warriorB.name} and deals {damage2warriorB} damage")

        print(f"{warriorB.name} is down to {warriorB.health} health")

        if warriorB.health <= 0:
            print(f"{warriorB.name} has Died and {warriorA.name} is Victorious")
            return "Game Over"
        else:
            return "Fight Again"

def main():

    #create 2 warriors
    jade = Warrior("Jade", 50, 20, 10)
    sonya = Warrior("Sonya", 50, 20, 10)

    #create Battle object
    battle = Battle()

    #initiate Battle
    battle.startFight(jade,sonya)

main()